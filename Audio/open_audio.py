import soundfile as sf
from scipy.io.wavfile import read as read_wav
import os, librosa, sys
def convertAudio(audioPath):
    os.system("ffmpeg.exe -i "+audioPath+" -f s16le -ar 44.1k -ac 2 "+audioPath+" -y")
    # try:
    #     basePath = os.path.dirname(__file__)
    #     # opens .wav file and converts to numpy array
    #     data, fs = sf.read(basePath + audioPath)
    #     print(data)
    #     ob = sf.SoundFile(basePath + audioPath)
    #     bit_depth = ob.subtype
    #     print(bit_depth)
    #     sf.SoundFile.close(ob)
    #     if bit _depth != "PCM_16":
    #         sf.write(basePath + audioPath[:-4] +"1.wav", data, fs, subtype='PCM_16') #need to figure out what new file name will be called/where to save to
    #         deletePath = basePath + audioPath
    #         os.system("del /f " + deletePath)
    #         os.system("mv " + basePath + audioPath[:-4] +"1.wav " + deletePath)
    #         print("Audio converted successfully.")
    #     # determines sampling frequency of .wav file 
    #     filePath = basePath + audioPath
    #     os.chdir(filePath)
    #     sampling_rate, data=read_wav(filePath) #would need to 
    #     print(sampling_rate)
    #     # changes samplying frequency of the.wav file
    #     if sampling_rate != 44000:
    #         y, s = librosa.load(filePath, sr= 44000)
    #     print(s)
    # except Exception as e:
    #     print("Audio conversion failed. Reason=", e)