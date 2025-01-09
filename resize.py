from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

# Ruta del archivo MP4 de entrada (video apaisado)
input_file = 'octo_octa.mp4'

# Definir las coordenadas de recorte (izquierda, arriba, derecha, abajo)
crop_area = (380, 0, 920, 1920)  # Reemplaza con las coordenadas que desees

# Nombre del archivo de salida
output_file = 'octo_vertical.mp4'

# Extraer un subclip del video
start_time = 0  # Tiempo de inicio en segundos
end_time = 120   # Tiempo de finalización en segundos (ajusta según tus necesidades)

ffmpeg_extract_subclip(input_file, start_time, end_time, targetname='waitaa.mp4')

# Cargar el subclip resultante
video_clip = VideoFileClip('waitaa.mp4')

# Recortar al área deseada
cropped_video = video_clip.crop(x1=crop_area[0], y1=crop_area[1], x2=crop_area[2], y2=crop_area[3])

# Mantener el audio original
cropped_video = cropped_video.set_audio(video_clip.audio)

# Guardar el video recortado con audio
cropped_video.write_videofile(output_file, codec='libx264', audio_codec='aac')


# Eliminar el archivo temporal
video_clip.close()
cropped_video.close()
