import soundfile as sf
from scipy.io.wavfile import read as read_wav
import os, librosa, sys


def convertAudio(audioPath):
    try:
        basePath = os.path.dirname(__file__)
        # opens .wav file and converts to numpy array
        data, fs = sf.read(basePath + audioPath)
        print(data)
        ob = sf.SoundFile(basePath + audioPath)
        bit_depth = ob.subtype
        print(bit_depth)
        sf.SoundFile.close(ob)
        if bit_depth != "PCM_16":
            sf.write(basePath + audioPath[:-4] +"1.wav", data, fs, subtype='PCM_16') #need to figure out what new file name will be called/where to save to
            deletePath = basePath + audioPath
            os.system("del /f " + deletePath)
            sf.write(deletePath, data, fs, subtype='PCM_16')
            deletePath = basePath + audioPath[:-4] +"1.wav"
            os.system("del /f " + deletePath)
            print("Audio converted successfully.")


        # determines sampling frequency of .wav file 
        os.chdir(basePath)
        sampling_rate, data=read_wav("file_example_WAV_5MG.wav") #would need to 
        print(sampling_rate)
        # changes samplying frequency of the.wav file
        if sampling_rate != 44000:
          y, s = librosa.load('file_example_WAV_5MG.wav', sr= 44000)
        print(s)
    except Exception as e:
        print("Audio conversion failed. Reason=", e)