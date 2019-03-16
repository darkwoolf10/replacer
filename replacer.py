import os

# take all js files in current dir
def getFilesInCurrentDir():
    files = os.listdir()
    jsFiles = []
    for key in files:
        if key[-2:] == "js":
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
            if line[:2] != "//":
                currentFile.write(line)
        currentFile.close() 