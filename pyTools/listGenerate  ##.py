file=open("Explore.txt","a+")
exp="q"
while exp!="":
    exp=input("Enter Topic: ")
    file.write(exp+"\n")
file.close()
print("success")
input()
    
