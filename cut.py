from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

input_file = './files/videos/ArgyatJungfraujoch-TopofEuropeSwitzerlandforCercle.mp4'
start_time = (55, 32)  # 1 minuto y 30 segundos
end_time = (57, 42)    # 2 minutos y 45 segundos
output_file = 'argya.mp4'
start_time_seconds = start_time[0] * 60 + start_time[1]
end_time_seconds = end_time[0] * 60 + end_time[1]


ffmpeg_extract_subclip(input_file, start_time_seconds, end_time_seconds, targetname=output_file)

print(f'Archivo recortado y guardado como {output_file}')
