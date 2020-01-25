# Tedxt Based Interpreter base off of the Natural Language Toolkit 
#NLTK ONLY Please 
import os #nltk
basePath = os.path.dirname(__file__)

#Open and read text files
def openFileString(Testfile):
    myfile = open(Testfile, "r")
    return ''.join(myfile.readlines())

myFile = openFileString(basePath + "/Text/Sample_Text.txt")

#Once the file is opened in the above function it will run through the bellow NLTK functions to analyze 

tokens = myFile.split()
print(tokens)
tagged = nltk.pos_tag(tokens)
#This is a test comment.