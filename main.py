###########################################################################
#  The project was developed based upon the idea introduced               # 
#  by Michael Francis, Aiden Aqui, Zayaan Khan, Adil Feroz                #  
#                                                                         #
#  Copyright (C) 2020 Ian Michael Francis, Aiden Aqui, Zayaan Khan,       #
#  and Adil Feroz                                                         #
#  The following packages must be installed:							  #
#  soundfile, scipy.io.wavfile, os, librosa, sys						  #
###########################################################################

import TInterpreter, AInterpreter, os

basePath = os.path.dirname(__file__)

#First, convert and analyzer audio
AInterpreter.analyzer(basePath + "/Audio/McMasterUniversity.wav")
print("Workings complete!")