#!/usr/bin/python3
import speech_recognition as sr
import base64
from pydub import AudioSegment
from pydub.silence import split_on_silence
from src.main.utils.core import Controller
from src.main.utils.core import ConfigDTO
#https://hackernoon.com/how-to-convert-speech-to-text-in-python-q0263tzp
class Controller1(Controller):
    def __init__(self, config: ConfigDTO = None):
        Controller.__init__(self, config)
        self.recognizer = sr.Recognizer()

    def loadChunks(self, filename):
        long_audio = AudioSegment.from_mp3(filename)
        audio_chunks = split_on_silence(long_audio, min_silence_len=1800, silence_thresh=-17)
        return audio_chunks
    def speechToText(self, payload):
        #voiceData = payload["voice"]
        #with open('dest_audio_file.mp3', 'wb') as file_to_save:
        #    file_content=base64.b64decode(voiceData)
        #    file_to_save.write(file_content)
        #chunks = self.loadChunks('./dest_audio_file.mp3')
        #print("1", len(chunks))
        #for audio_chunk in chunks:
            #audio_chunk.export("temp", format="wav")
        with sr.AudioFile("./src/resources/AUDIO-2021-08-11-20-11-56.wav") as source:
            try:
                audio = self.recognizer.listen(source)
                text = self.recognizer.recognize_google(audio, language="es-ES")
                print("Chunk : {}".format(text))
                #text = self.recognizer.recognize_sphinx(audio, language="es-ES")
                #print("Chunk : {}".format(text))
                #text = self.recognizer.recognize_bing(audio, language="es-ES")
                #print("Chunk : {}".format(text))
                #text = self.recognizer.recognize_houndify(audio, language="es-ES")
                #print("Chunk : {}".format(text))
                #text = self.recognizer.recognize_ibm(audio, language="es-ES")
                #print("Chunk : {}".format(text))
            except Exception as ex:
                print("Error occured")
                print(ex)
        #speech_as_text = self.recognizer.recognize_google(file_content, 'en-US')
        #ecognizer.recognize_google(audio, language=cls.main_lang).lower()
