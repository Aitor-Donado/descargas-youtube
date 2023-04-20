from pytube import YouTube

direccion = input("Dirección del vídeo:")
audio = input("¿Quieres gurdar sólo el audio? [s]: ") == "s"
yt = YouTube(direccion)



if audio:
    print("Guardando el audio: ", yt.title)
    audio = yt.streams.get_audio_only()
    audio.download("/home/laptop/Música")
else:
    print("Guardando el video: ", yt.title)
    video = yt.streams.get_by_resolution("720p")
    video.download("/home/laptop/Vídeos")

#comentario absurdo