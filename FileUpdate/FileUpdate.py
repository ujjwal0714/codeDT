import os
import sys
import shutil

og = os.listdir(r"C:\Users\ujjwa\Desktop\codeDT\FileUpdate\Music")
total_files = len(og)

def write_to_np():
    filePath = "ogList.txt"
    with open(filePath,"w") as file:
        for i in og:
            file.write(i + "\n")
def loadFileNames():
    txtFile = r"C:\Users\ujjwa\Desktop\codeDT\FileUpdate\ogList.txt"
    ogFileNames = []
    with open(txtFile,"r") as file:
        for line in file:
            ogFileNames.append(line.strip("\n"))
    if len(ogFileNames) == total_files):
        return (newFileNames)
    else:
        print("check file names for unsupported characters.")
        return()

def newFilesName():
    og2 = os.listdir(r"C:\Users\ujjwa\Desktop\codeDT\FileUpdate\Music")
    newFilesList = []
    ogFilesList = loadFileNames()
    for i in og2:
        if i not in ogFilesList:
            newFilesList.append(i)
    return(newFilesList)

def newVersion():
    try:  # Delete Music2 Folder if already exists else continue
        os.rmdir(r"C:\Users\ujjwa\Desktop\codeDT\FileUpdate\Music2")
    except:
        pass
    os.mkdir(r"C:\Users\ujjwa\Desktop\codeDT\FileUpdate\Music2")
    newFiles = newFilesName()
    for i in newFiles:
        src = os.path.join(r"C:\Users\ujjwa\Desktop\codeDT\FileUpdate\Music",i)
        dst = os.path.join(r"C:\Users\ujjwa\Desktop\codeDT\FileUpdate\Music2",i)
        shutil.copyfile(src,dst)

newVersion()

if input("write_to_og? 1|0: ") == 1:
    write_to_np()

input("Done.\nEnter to Leave.")

