from pytube import YouTube

# URL del video de YouTube que deseas descargar
url="https://www.youtube.com/watch?v=lJoBZRPUo58"

# Crear un objeto YouTube
yt = YouTube(url)

# Obtener la corriente de audio en el formato más alto disponible
audio_stream = yt.streams.filter(only_audio=True).first()

# Ruta donde deseas guardar el audio
download_path = "./"

# Descargar el audio
audio_stream.download(output_path=download_path)

print("Descarga de audio completa.")
