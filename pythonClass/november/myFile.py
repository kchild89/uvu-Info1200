myFile = open("info.txt", "r")
content = myFile.read()

print(content)
myFile.close


with open("info2.txt", "w") as myfile2:
    myfile2.write("Hellooooo!!!!!")















    


members = ["John Cleese", 
           "Eric Idle"]

with open("member.txt", "w") as file:
    for m in members:
        file.write(f"{m}/n")    


members = []    
with open("members.txt") as file:
    for line in file:
        line =line.replace("/n", "")
        members.append(line)
                       
print(members)        