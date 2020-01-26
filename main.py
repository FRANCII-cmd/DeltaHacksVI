###########################################################################
#  The project was developed based upon the idea introduced               # 
#  by Michael Francis, Aiden Aqui, Zayaan Khan, Adil Feroz                #  
#                                                                         #
#  Copyright (C) 2020 Ian Michael Francis, Aiden Aqui, Zayaan Khan,       #
#  and Adil Feroz                                                         #
#  The following packages must be installed:							  #
#  soundfile, scipy.io.wavfile, os, librosa, sys						  #
###########################################################################
import TInterpreter, AInterpreter, os, open_audio, shutil

basePath = os.path.dirname(__file__)
audioPath = basePath + "/Audio/SampleVoices-KimBorge.wav"

# First, convert and analyze the audio
shutil.copy(audioPath,"tmp")
os.system("ffmpeg.exe -i tmp -ar 44k -ac 2 "+audioPath+" -y")
os.unlink("tmp")

AInterpreter.analyzer(audioPath)
print("Workings complete!")