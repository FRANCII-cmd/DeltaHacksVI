''' 
import os, image, pytesseract 
basePath = os.path.dirname(__file__)

#Open and read text files
def openFileString(Testfile):
    myfile = open(Testfile, "r")
    close()
    return ''.join(myfile.readlines())

myFile = openFileString(basePath + "/Text/Sample_Text.txt")

def Imageread(x):
	imgtxt = pytesseract.image_to_string(image.open(x))
	return imgtxt

	from nltk.corpus import treebank
	t = treebank.parsed_sent
'''