import os
from pytube import YouTube
from dotenv import load_dotenv

url="https://www.youtube.com/watch?v=lJoBZRPUo58"

# Crear un objeto YouTube
yt = YouTube(url)

# Seleccionar la corriente de mayor calidad
stream = yt.streams.get_highest_resolution()

# Ruta donde deseas guardar el video
download_path = "./files/videos/"

# Descargar el video
stream.download(output_path=download_path)

print("Descarga completa.")
