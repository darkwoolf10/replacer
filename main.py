import replacer 

# my types for clear
types = ["js", "php"]
# get file in dir
jsFiles = replacer.getFilesInCurrentDir(types)   
# clear
replacer.replace(jsFiles)    