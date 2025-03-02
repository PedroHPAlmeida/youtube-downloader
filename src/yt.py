import yt_dlp
import subprocess

YDL_OPTS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }],
    'outtmpl': '-',
    'quiet': True,
}

def download_audio_from_youtube(url):
    with yt_dlp.YoutubeDL(YDL_OPTS) as ydl:
        result = ydl.extract_info(url, download=False)
        audio_url = result['url']

        process = subprocess.Popen(
            ['ffmpeg', '-i', audio_url, '-f', 'mp3', 'pipe:1'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        audio_bytes, _ = process.communicate()
        
        return audio_bytes, f"{result['title']}.mp3"
