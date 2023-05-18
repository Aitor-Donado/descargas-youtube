from pytube import YouTube


audio = input("¿Quieres gurdar sólo el audio? [s]: ") == "s"
enlaces = [
    "https://www.youtube.com/watch?v=dokH3xc26iY",
    ]
for enlace in enlaces:
    yt = YouTube(enlace)
    if audio:
        print("Guardando el audio: ", yt.title)
        audio = yt.streams.get_audio_only()
        audio.download("/home/laptop/Música")
    else:
        print("Guardando el video: ", yt.title)
        video = yt.streams.get_by_resolution("720p")
        video.download("/home/laptop/Vídeos")
