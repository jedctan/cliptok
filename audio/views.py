import os
import subprocess
import uuid
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Audio
from django.views.generic import View

# Create your views here.

class ShowHomeView(View):
    template_name = 'audio/home.html'

    def get(self, request):
        audios = Audio.objects.all().order_by('-created_at')
        return render(request, self.template_name, {'audios': audios})

    def post(self, request):
        url = request.POST.get('url')
        if not url:
            return render(request, self.template_name, {
                'audios': Audio.objects.all(),
                'error': 'No URL provided'
            })

        try:
            filename = f"{uuid.uuid4()}.%(ext)s"
            output_path = os.path.join(settings.MEDIA_ROOT, 'audio', filename)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            subprocess.run([
                'yt-dlp',
                '-x', '--audio-format', 'mp3',
                # pass arg to ffmpeg to delete video file after conversion
                '--postprocessor-args', '-delete_input true',
                '-o', output_path,
                url
            ], check=True)

            final_file = max(
                [os.path.join(settings.MEDIA_ROOT, 'audio', f) for f in os.listdir(os.path.join(settings.MEDIA_ROOT, 'audio'))],
                key=os.path.getctime
            )
            rel_path = os.path.relpath(final_file, settings.MEDIA_ROOT)

            Audio.objects.create(
                title=os.path.basename(final_file),
                file=rel_path
            )

        except Exception as e:
            return render(request, self.template_name, {
                'audios': Audio.objects.all(),
                'error': str(e)
            })

        return redirect('home')
