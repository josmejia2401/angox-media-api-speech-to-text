#!/usr/bin/python3
import speech_recognition as sr
import base64
import sys
import pathlib
import uuid
from pydub import AudioSegment
from pydub.silence import split_on_silence
from src.main.utils.core import Controller
from src.main.utils.core import ConfigDTO
#https://hackernoon.com/how-to-convert-speech-to-text-in-python-q0263tzp
class Controller1(Controller):
    def __init__(self, config: ConfigDTO = None):
        Controller.__init__(self, config)
        self.recognizer = sr.Recognizer()

    def checkFile(self, payload) -> bytes:
        voiceData = payload['voice']
        file_content = base64.b64decode(voiceData)
        sizeContent = sys.getsizeof(file_content)
        if sizeContent > 5 * 1024 * 1024:
            raise Exception('File too big size')
        return file_content

    def checkExtension(self, payload):
        fileName = payload['fileName']
        extension = pathlib.Path(fileName).suffix
        if extension == '.wav' or extension == '.WAV':
            return 
        elif extension == '.mp3' or extension == '.MP3':
            pass
        raise Exception('Extension not valid')
    
    def removeFile(self, fileName):
        try:
            file_to_rem = pathlib.Path(fileName)
            file_to_rem.unlink()
        except Exception as e:
            print(e)

    def saveFile(self, fileContent, payload):
        try:
            fileNameUnique = str(uuid.uuid4())
            fileName = payload['fileName']
            extension = pathlib.Path(fileName).suffix
            lastFileName = './{}{}'.format(fileNameUnique, extension)
            with open(lastFileName, 'wb') as file_to_save:
                file_to_save.write(fileContent)
            if extension == '.mp3' or extension == '.MP3':
                chunks = self.loadChunks(lastFileName, payload["advanced"])
                for audio_chunk in chunks:
                    audio_chunk.export('{}{}'.format(fileNameUnique, '.wav'), format="wav")
                return './{}{}'.format(fileNameUnique, '.wav')
        except Exception as e:
            print(e)
            raise e
        finally:
            self.removeFile(lastFileName)

    def loadChunks(self, filename, advanced = None):
        long_audio = AudioSegment.from_mp3(filename)
        if not advanced or advanced is None or 'min_silence_len' not in advanced:
            return [long_audio]
        #{ "min_silence_len": 4000, "silence_thresh": int(-36), "keep_silence": 200 }
        min_silence_len = advanced['min_silence_len']
        silence_thresh = advanced['silence_thresh']
        keep_silence = advanced['keep_silence']
        audio_chunks = split_on_silence(long_audio, 
            # split on silences longer than 1000ms (1 sec)
            min_silence_len=min_silence_len,
            # anything under -16 dBFS is considered silence
            silence_thresh=silence_thresh,
            # keep 200 ms of leading/trailing silence
            keep_silence=keep_silence
        )
        if len(audio_chunks) > 0:
            return audio_chunks
        else:
            return [long_audio]
    
    def sourceWav(self, fileContent):
        harvard = sr.AudioFile(fileContent)
        with harvard as source:
            #self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.record(source, duration=180)
        return audio

    def speechToText(self, payload):
        fileName = None
        try:
            fileContent = self.checkFile(payload=payload)
            fileName = self.saveFile(fileContent, payload)
            source = self.sourceWav(fileName)
            text = self.recognizer.recognize_google(source, language="es-ES", show_all=True)
            print("Chunk : {}".format(text))
        except Exception as e:
            print(e)
            raise e
        finally:
            if fileName:
                self.removeFile(fileName)