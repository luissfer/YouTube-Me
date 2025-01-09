from moviepy.video.io.VideoFileClip import VideoFileClip

output_path='./files/music/'
# video_path='./files/videos/lucialuhor.mp4'
file_name='KIKI  Boiler Room x AVA Festival 2024.mp4'
video_path=f'./files/videos/' + file_name

video_clip = VideoFileClip(video_path)
audio_clip = video_clip.audio
audio_clip.write_audiofile(f"{output_path}/{video_clip}.mp3")
