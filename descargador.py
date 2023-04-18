from pytube import YouTube

direccion = input("Escribe la dirección del vídeo: ")

yt = YouTube(direccion)

print(yt.title)

musical = input("¿Es un vídeo de música? [y/n]: ")

if musical == "y":
    audio = yt.streams.get_audio_only()
    pais = input("Alemán, griego, ruso: [a/g/r]: ")
    print("Imprimiendo el vídeo: ", yt.title)
    if pais == "g":
        audio.download("/home/laptop/Música/Griega")
    elif pais == "a":
        audio.download("/home/laptop/Música/Alemana")
    elif pais == "r":
        audio.download("/home/laptop/Música/Rusa")
    else:
        audio.download("/home/laptop/Música")
else:
    video = yt.streams.get_by_resolution("720p")
    video.download("/home/laptop/Vídeos")
