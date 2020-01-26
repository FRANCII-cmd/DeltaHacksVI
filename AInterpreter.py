# some_file.py
import sys, os, open_audio
basePath = os.path.dirname(__file__)
audioPath = basePath + "/Audio/SampleVoices-KimBorge.wav"
#Audio filr must be only 3 minutes or less 
def analyzer(audioFile):
	#open_audio.convertAudio(audioFile)
	
	#Gender recognition and mood of speech
	mysp=__import__("my-voice-analysis")
	
	p=audioFile # Audio File title
	c= basePath + "/Audio" # Path to the Audio_File directory 
	mysp.myspgend(p,c)
	
	#Pronunciation posteriori probability score percentage
	mysp.mysppron(p,c)
	
	#Detect and count number of syllables
	mysp.myspsyl(p,c)
	
	#Detect and count number of fillers and pauses
	mysp.mysppaus(p,c)
	
	#Count the syllables per second
	mysp.myspsr(p,c)
	
	#Measure the articulation (speed): 
	mysp.myspatc(p,c)
	
	#Measure speaking time (excl. fillers and pause): 
	mysp.myspst(p,c)
	
	#Measure total speaking duration (inc. fillers and pauses): 
	mysp.myspod(p,c)
	
	#Measure ratio between speaking duration and total speaking duration
	mysp.myspbala(p,c)
	
	#Overview: Function 
	
	#Prints gender recognition, mood, etc
	print(mysp.myspgend(p,c))
	
	#Prints pronounciation rate
	print(mysp.mysppron(p,c))
	print(mysp.myspsr(p,c))
	
	#Prints results for speech rate
	if mysp.myspsr(p,c) < 2: print("It seems that you are speaking slowly. Try speaking a little faster.")
	elif mysp.myspsr(p,c) > 3: print("Looks like you're going too fast. Try slowing down your speech.")
	else: print("You're speaking at a good rate. Try not to slow down or speed up!")
	
	#Measure ratio between speaking duration and total speaking time
	if mysp.myspbala(p,c) < 0.8: print("You seem to have a lot of silence in your presentation. Try taking shorter pauses.")
	elif mysp.myspbala(p,c) > 0.95: print("You're talking more than 95 percent of the time! Try taking some pauses.")
	else: print("You have a good balance between moments of speech and pauses. Keep it up!")