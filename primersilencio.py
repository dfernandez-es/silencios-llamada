from pydub import AudioSegment,silence
import pathlib
for file in pathlib.Path('/home/s3v3n/Escritorio/Nueva carpeta (1)/').glob('*.mp3'):
	myaudio = intro = AudioSegment.from_mp3(file)
	dBFS=myaudio.dBFS
	silences = silence.detect_silence(myaudio, min_silence_len=1000, silence_thresh=dBFS-16)
	silences = [((start/1000),(stop/1000)) for start,stop in silences]
	print(str(file) + " " + str(silences[0]))