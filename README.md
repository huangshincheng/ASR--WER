# ASR--WER
## install
### [Automatic-Speech-Recognition](https://realpython.com/python-speech-recognition/)

    pip3 install SpeechRecognition
  

### [Word-Error-Rate](https://github.com/belambert/asr-evaluation)

    pip3 install asr-evaluation
  

## usage
First, convert the audio file (.wav) into text format (.txt).
  
    python3 ConvertAudio.py [original.wav] [0cm-unprocessed.wav] [0cm-processed.wav] [60cm-unprocessed.wav] [60cm-processed.wav]

###### You have to make the reference.txt before testing the WER.
Second, evaluate the WER.
  
    wer -i -a reference.txt hypothesis.txt
  
