import sys
import time
#Project Created by Me for a challenge presented to me by my Computer Science Teacher :)
#This program performs calculations based on marks inside a txt file.
#The process of creating this challenged and grew my skills of creating functions and using file operations to perform tasks
studentNames = []
studentMarks = []


file = open("nameAndMarks.txt", "r")

for i in range(6):
    #This for loop reads the content of nameAndMarks and appends them to a list

    appearance1 = file.readline().strip("\n").split(":")
    var1, var2 = appearance1
    studentNames.append(var1)
    secondVar = var2
    secondVar2 = secondVar.split(",", maxsplit=3)
    var11, var22, var33 = secondVar2
    studentMarks.append([[int(var11)],[int(var22)],[int(var33)]])

file.close()

def main():
    #The main function, used to run all previous functions created
    complete = False
    while complete != True:
        print("|-------------------------------------------------|") #Menu
        print("| Welcome to the Mark input/calculation Program!  |")
        print("| 1.               Input new marks                |")
        print("| 2.            Calculate Total Score             |")
        print("| 3.        Calculate Average Total Score         |")
        print("| 4.    Find Student With Highest Total Score     |")
        print("| 5.    Calculate Average Score for Each Test     |")
        print("| 6.                Exit Program                  |")
        print("|-------------------------------------------------|")
        userInput = input()
        
        try: 
            if int(userInput) == 1:
                global nameInput #makes nameInput a global variable to be used outside of the main function
                nameInput = input("Input name of Student: ")
                global position
                position = getNamePos(nameInput)
                print(position)
                inputMark(position)
            elif int(userInput) == 2:
                totalScore()
            elif int(userInput) == 3:
                averageTotal()
            elif int(userInput) == 4:
                highestTotalAverage()
            elif int(userInput) == 5:
                averagePercentageOfTest()
            elif int(userInput) == 6:
                print("Bye!")
                time.sleep(1)
                sys.exit() #Exits program
            else:
                print("Not a valid number, try again")
        except ValueError: #If ValueError appears print this statement and rerun loop
            print("Input an Integer from 1-6")

def writeToLine(num, pos):
    #This function overwrites current mark for the Student and replaces it with the new mark then returns it for use in another function
    with open("nameAndMarks.txt", "r+") as file:
        for i in range(6):
            data = file.readline().strip("\n").split(":")
            variab1, variab2 = data
            if variab1 == nameInput:
                marks = variab2.split(",")
                myStrOld = ",".join(marks)
                marks[pos] = str(num)
                myStr = ",".join(marks)
                if position < 5 and position >= 0:
                    finalResult = nameInput + ":" + myStr + "\n"
                    break
                elif position == 5:
                    finalResult = nameInput + ":" + myStr
                    break
    file.close()
    return finalResult


def finallyWrite(fullData):
    #rewrites the txt file with the new test scores and is used in useWriteToLine
    file = open("nameAndMarks.txt", "w")
    file.writelines(fullData)


def useWriteToLine(result, pos):
    #This function rewrites the data in the array created by reading the txt file
    file = open("nameAndMarks.txt", "r")
    data = file.readlines()
    data[pos] = result
    file.close()
    finallyWrite(data)
    return data


def getNamePos(name):
    #This function gets the position of the name inputted by the user
    completed = False

    while completed == False:
        if name in studentNames:
            print("In Array!")
            position = studentNames.index(name)
            completed = True
            return position

        elif name not in studentNames:
            print("Not in array")
            name = input("Input name of Students: ")
            completed = False


def inputMark(position):
    #This function inputs the marks for the Student
    complete1 = False
    complete2 = False
    complete3 = False 


    file1 = open("nameAndMarks.txt", "r")

    num = input("Input marks for 1st test: ") 

    while complete1 != True:
        try:
            if int(num) >= 0 and int(num) <= 20:
                studentMarks[position][0] = int(num)
                result1 = writeToLine(num, 0)
                result11 = useWriteToLine(result1, position)
                complete1 = True

            elif int(num) < 0 or int(num) > 20:
                num = input("Input a valid score (out of 20): ")
                complete1 = False

        except ValueError:
            #If ValueError Occurs (String inputted instead of Integer) run this
            num = input("Input an integer not a string: ")
            complete1 = False

    numInput2 = input("Input marks for 2nd test: ")


    while complete2 != True:
        try:
            if int(numInput2) >= 0 and int(numInput2) <= 25:
                studentMarks[position][1] = int(numInput2)
                result2 = writeToLine(numInput2, 1)
                result22 = useWriteToLine(result2, position)
                complete2 = True

            elif int(numInput2) < 0 or int(numInput2) > 25:
                numInput2 = input("Input a valid score (out of 25): ")
                complete2 = False

        except ValueError:
            numInput2 = input("Input an integer not a string: ")
            complete2 = False
    numInput3 = input("Input marks for 3rd test: ")


    while complete3 != True:
        try:
            if int(numInput3) >= 0 and int(numInput3) <= 35:
                studentMarks[position][2] = int(numInput3)
                result3 = writeToLine(numInput3, 2)
                result33 = useWriteToLine(result3, position)
                complete3 = True

            elif int(numInput3) < 0 or int(numInput3) > 35:
                numInput3 = input("Input a valid score (out of 35): ")
                complete3 = False

        except ValueError:
            numInput3 = input("Input an integer not a string: ")
            complete3 = False


    file1.close()


def getArrayMarks():
    #This function gets the name and marks and puts them into 2 seperate lists, for use in other functions
    with open("nameAndMarks.txt", "r") as file:
        listNames = []
        listMarks = []
        for i in range(6):
            data = file.readline().strip("\n").split(":")
            variab1, variab2 = data 
            listNames.append(variab1)
            listMarks.append(variab2)
        return listNames, listMarks


def totalScoreForOtherCalculations():
    #This function performs the same as totalScore() but does not print out any statement and is for use in different functions
    listNames, listMarks = getArrayMarks()
    tempList = []
    calculatedList = []

    for i in range(6):
        tempList = listMarks[i].split(",")
        if len(tempList) != 1:
            tempVal = 0
            for i in tempList:
                tempVal += int(i)
            calculatedList.append(tempVal)
        else:
            break
    return calculatedList


def totalScore():
    #This function calculates the total score of each student and outputs it upon the user's request
    listNames, listMarks = getArrayMarks()
    tempList = []
    calculatedList = []
    for i in range(6):
        tempList = listMarks[i].split(",")
        if len(tempList) != 1:
            tempVal = 0
            for i in tempList:
                tempVal += int(i)
            calculatedList.append(tempVal)
        else:
            break
    check = input("Would you like to see your results? ")
    if check.lower() == "yes":
        for i in range(6):
            print("The total for " + str(listNames[i]) + " marks was " + str(calculatedList[i]) + "!")
    else:
        pass
    return calculatedList


def averageTotal():
    #This function calculates the average out of every students totals
    total = totalScoreForOtherCalculations()
    numberOfScores = len(total)
    totalTotal = sum(total)
    average = totalTotal / numberOfScores
    roundedAverage = round(average, 2)
    print("The average total score in the class was: " + str(roundedAverage))


def highestTotalAverage():
    #This function finds the student with the highest total score and outputs it
    total = totalScoreForOtherCalculations()
    listName, listMarks = getArrayMarks()
    highest = -999999

    for i in total:
        if i > highest:
            highest = i
    for i in total:
        if i == highest:
            print("The Student with the highest total was " + listName[total.index(i)] + " With " + str(i) + " Marks!")

def average(list):
    #This function finds the average of the inputted list and returns it
    numberOfScores = len(list)
    totalListSum = sum(list)
    average1 = totalListSum / numberOfScores
    roundedAverage1 = round(average1, 2)
    return roundedAverage1

def averagePercentageOfTest():
    #This procedure calculates and prints the average for each test
    listName, listMarks = getArrayMarks()
    test1List = []
    test2List = []
    test3List = []
    averagesList = []
    for i in range(6):
        tempList = listMarks[i].split(",")
        variab1, variab2, variab3 = tempList
        test1List.append(int(variab1))
        test2List.append(int(variab2))
        test3List.append(int(variab3))
    test1Average = average(test1List)
    test2Average = average(test2List)
    test3Average = average(test3List)
    averagesList.append(test1Average)
    averagesList.append(test2Average)
    averagesList.append(test3Average)
    maxAverage = max(averagesList)
    maxAveragePos = averagesList.index(maxAverage) + 1
    print("The average score for Test 1 was: " + str(test1Average))
    print("The average score for Test 2 was: " + str(test2Average))
    print("The average score for Test 3 was " + str(test3Average))
    print("The Test with the highest average was Test " + str(maxAveragePos) + " With an average of " + str(maxAverage) + "!") 

main()