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