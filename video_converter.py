import moviepy.editor as mp

clip = mp.VideoFileClip("video.mkv")
clip.audio.write_audiofile("theaudio.wav")
