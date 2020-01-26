# some_file.py
import sys, os
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, os.path.dirname(__file__) + "/Audio")

import open_audio

def analyzer(audioFile):
	
	open_audio.convertAudio(audioFile)

	#Gender recognition and mood of speech
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspgend(p,c)
	#Pronunciation posteriori probability score percentage
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.mysppron(p,c)
	#Detect and count number of syllables
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspsyl(p,c)
	#Detect and count number of fillers and pauses
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.mysppaus(p,c)
	#Detect and count number of fillers and pauses
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspsr(p,c)
	#Measure the articulation (speed): 
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspatc(p,c)
	#Measure speaking time (excl. fillers and pause): 
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspst(p,c)
	#Measure total speaking duration (inc. fillers and pauses): 
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspod(p,c)
	#Measure ratio between speaking duration and total speaking duration
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory
	mysp.myspbala(p,c)
	#Measure fundamental frequency distribution mean
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspf0mean(p,c)
	#Measure fundamental frequency distribution SD
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspf0sd(p,c)
	#Measure fundamental frequency distribution median
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspf0med(p,c)
	#Measure fundamental frequency distribution minimum
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspf0min(p,c)
	#Measure fundamental frequency distribution maximum
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspf0max(p,c)
	#Measure 25th quantile fundamental frequency distribution
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspf0q25(p,c)
	#Measure 75th quantile fundamental frequency distribution
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspf0q75(p,c)
	#Overview: Function 
	mysp=__import__("my-voice-analysis")
	p="sample2" # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory  
	mysp.mysptotal(p,c)
	print(mysp.mysptotal(p,c))