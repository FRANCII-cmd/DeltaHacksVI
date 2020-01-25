# Tedxt Based Interpreter base off of the Natural Language Toolkit 
#NLTK ONLY Please 

def FileOpenFunctions(Testfile):                                 #This for file reading 
    file = open(Testfile, "r")
    file = ''.join(file.readlines())
    return(file)

FileOpenFunctions("Sample_Text.txt")
