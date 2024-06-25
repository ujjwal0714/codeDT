import os

path=input("Path: ")  # folder path containing items.

directory = os.listdir(path) # list all filenames in given directory.
print("opening directory......") # printed means directory is accessed.
os.startfile(path) # opens folder containing files.

def fileExtension(x): # get file extension from file name
    try:
        x=x[::-1]
        a=x.index(".")
        return(x[:a+1][::-1])
    except:
        pass


##newDirectory=[]
##tempName=1
##for name in directory:
##    try:
##        extension=fileExtension(name)
##        oldName=path+"\\{}".format(name)
##        newName=path+"\\{}".format(str(tempName)+"y"+extension)
##        newDirectory.append(str(tempName)+"y"+extension)
##        tempName+=1
##        os.rename(oldName,newName)
##    except:
##        pass
##count = 0
##if input("Sure? ")=="1":
##    for name in newDirectory:
##       extension=fileExtension(name)
##       count+=1
##       oldName=path+"\\{}".format(name)
##       newName=path+"\\{}".format(str(bin(count))+extension)
##       os.rename(oldName,newName)
##       print("Done")
##else:
##    print("aborted")
##    
##input()

count = 0
newDirectory=[]
tempName=1

if input("Sure? ")=="1":
    for name in directory:
        try:
            extension=fileExtension(name)
            oldName=path+"\\{}".format(name)
            newName=path+"\\{}".format(str(tempName)+"y"+extension)
            newDirectory.append(str(tempName)+"y"+extension)
            tempName+=1
            os.rename(oldName,newName)
        except:
            pass
        for name in newDirectory:
            extension=fileExtension(name)
            count+=1
            oldName=path+"\\{}".format(name)
            newName=path+"\\{}".format(str(count)+extension)
            os.rename(oldName,newName)
            print("Done")
    else:
        print("aborted")
    
input()

