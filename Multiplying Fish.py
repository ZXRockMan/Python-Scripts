file = open("fish.txt", "r")

fileread = file.read()

fileread = list(fileread)

##days = 0

for i in range(0, len(fileread)):
    fileread[i] = int(fileread[i])
    
numberofnumbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def doublingnines(list_n):
    placeholder = list_n[9] * 2
    list_n[9] = list_n[8]
    list_n[8] = list_n[7]
    list_n[7] = list_n[6]
    list_n[6] = list_n[5]
    list_n[5] = list_n[4]
    list_n[4] = list_n[3]
    list_n[3] = list_n[2]
    list_n[2] = list_n[1]
    list_n[1] = list_n[0]
    list_n[0] = placeholder
    return list_n

for i in range(0, len(fileread)):
    numberofnumbers[fileread[i]] = numberofnumbers[fileread[i]] + 1
    
def calculatingnumberoffish(numberofnumbers):
    totaloffish = 0
    for i in range(0, len(numberofnumbers)):
        totaloffish += numberofnumbers[i]
    return totaloffish

numberoffish = calculatingnumberoffish(numberofnumbers)

days = 0

while numberoffish < 10 ** 100:
    doublingnines(numberofnumbers)
    numberoffish = calculatingnumberoffish(numberofnumbers)
    days += 1

print(("The days it takes to get to a 10 to the 100th ") + str(days) + (" days."))
print("Total of fish " + str(calculatingnumberoffish(numberofnumbers)) + ("."))
      
##print(calculatingnumberoffish(numberofnumbers))
##print(numberofnumbers)
            


##while len(fileread) < 1000000000000:
##
##    for i in range(0, len(fileread)):
##        fileread[i] = fileread[i] + 1
##
##    for i in range(0, len(fileread)):
##        if fileread[i] == 10:
##            fileread[i] = 0
##            fileread.append(0)
##            
##    print(("Amount of days: ") + str(days) + (" Length of list: ") + str(len(fileread)))
##    days += 1
##
##print(len(fileread))
##print("Here's how many days it took " + str(days) +".")
