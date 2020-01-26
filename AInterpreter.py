# some_file.py
import sys, os
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, os.path.dirname(__file__) + "/Audio")

import open_audio

def analyzer(audioFile):
	
	open_audio.convertAudio(audioFile)

	#Gender recognition and mood of speech
	mysp=__import__("my-voice-analysis")
	p=audioFile # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspgend(p,c)
	#Pronunciation posteriori probability score percentage
	p=audioFile # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.mysppron(p,c)
	#Detect and count number of syllables
	p=audioFile # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspsyl(p,c)
	#Detect and count number of fillers and pauses
	p=audioFile # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.mysppaus(p,c)
	#Count the syllables per second
	p=audioFile # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspsr(p,c)
	#Measure the articulation (speed): 
	p=audioFile # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspatc(p,c)
	#Measure speaking time (excl. fillers and pause): 
	p=audioFile # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspst(p,c)
	#Measure total speaking duration (inc. fillers and pauses): 
	p=audioFile # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory 
	mysp.myspod(p,c)
	#Measure ratio between speaking duration and total speaking duration
	p=audioFile # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory
	mysp.myspbala(p,c)
	#Overview: Function 
	p=audioFile # Audio File title
	c=r"C:\Users\adilf\Desktop\DeltaHacksVI\Audio" # Path to the Audio_File directory  
	
	#Prints gender recognition, mood, etc
	print(mysp.myspgend(p,c))

	#Prints pronounciation rate
	print(mysp.mysppron(p,c))
	
	#Prints results for speech rate
	if mysp.myspsr(p,c) < 2: print("It seems that you are speaking slowly. Try speaking a little faster.")
	
	elif mysp.myspsr(p,c) > 3: print("Looks like you're going too fast. Try slowing down your speech.")
	else: print("You're speaking at a good rate. Try not to slow down or speed up!")

	#Measure ratio between speaking duration and total speaking time
	if mysp.myspbala(p,c) < 0.8: print("You seem to have a lot of silence in your presentation. Try taking shorter pauses.")
	elif mysp.myspbala(p,c) > 0.95: print("You're talking more than 95 percent of the time! Try taking some pauses.")
	else: print("You have a good balance between moments of speech and pauses. Keep it up!")


print(mysp.myspbala(p,c))