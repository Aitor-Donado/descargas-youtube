from pytube import YouTube

direccion = input("Dirección del vídeo:")

yt = YouTube(direccion)

print(yt.title)
"""
audio = yt.streams.get_audio_only()
audio.download("/home/laptop/Música")
"""

video = yt.streams.get_by_resolution("720p")
video.download("/home/laptop/Música")

