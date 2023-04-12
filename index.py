from pytube import YouTube

direccion = input("Dirección del vídeo:")
audio = input("¿Quieres gurdar sólo el audio? [s]: ") == "s"
yt = YouTube(direccion)

print(yt.title)

if audio:
    audio = yt.streams.get_audio_only()
    audio.download("/home/laptop/Música")
else:
    video = yt.streams.get_by_resolution("720p")
    video.download("/home/laptop/Vídeos")
