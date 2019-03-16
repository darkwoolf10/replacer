import os
import sys

# take all js files in current dir
# types is the file types
def getFilesInCurrentDir(types=[]):
    if types == []:
        print("No file types specified for getFilesInCurrentDir function")
        sys.exit()
    files = os.listdir()
    jsFiles = []
    for key in files:
        file = key.split(".")
        file = file[-1:]
        for type in types:
            if file[0] == type:
                jsFiles.append(key)
    return jsFiles

def outputFiles(jsFiles):
    for file in jsFiles:
        currentFile = open(file, 'r')
        for line in currentFile:
            print(line)
        currentFile.close() 
        print("=================+>")    

def replace(jsFiles):
    for file in jsFiles:
        currentFile = open(file, 'r')
        lines = currentFile.readlines()
        currentFile = open(file, "w")
        for line in lines:
            if '//' not in line:
                currentFile.write(line)
        currentFile.close()