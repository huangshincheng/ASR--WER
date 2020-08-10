import sys
import speech_recognition as sr
# sys.argv[1] ==> original wave
# sys.argv[2] ==> 0 cm unprocessed wave
# sys.argv[3] ==> 0 cm processed wave
# sys.argv[4] ==> 60 cm unprocessed wave
# sys.argv[5] ==> 60 cm processed wave

# txt
text_file = open("hypothesis.txt", "w")

sr.__version__
r = sr.Recognizer()
for i in sys.argv[1:6]:
	harvard = sr.AudioFile(i)
	with harvard as source:
		print(source)
		audio = r.record(source)
		r.recognize_google(audio)
		text_file.write(r.recognize_google(audio))
		text_file.write("\n")
text_file.close()

