# Programmed by: Lee Anne Y. Angeles

numList = [1, 4, 3, 4, 4, 5, 6, 2, 56, 200]

def mainMenu():                                                           
    print("\n\n<<<<<<<<<<<<<<<<<<<<<<< MAIN MENU >>>>>>>>>>>>>>>>>>>>>>>>")
    print("\n\t[1] Add an element" + "\n\t[2] Insert an element" +                                           
    "\n\t[3] Modify an element" + "\n\t[4] Delete an element" + 
    "\n\t[5] Arrange in ascending order" + "\n\t[6] Arrange in descending order" +
    "\n\t[7] Exit Program")      

def addElement():                                                         
    while True:
        print("\n\n<<<<<<<<<<<<<<<<<<<<< ADD AN ELEMENT >>>>>>>>>>>>>>>>>>>>>")
        print("\nArray:", numList)
        num = int(input("\nEnter the number you want to add: "))                                   
        numList.append(num)
        print("The element has been successfully added!")
        print("\nThis is the new array: \n", numList)               

        addAgain = input("\nWould you like to add another element? [ yes / no ] : ")  
        if addAgain.casefold() == "yes":                                              
            continue
        elif addAgain.casefold() == "no":
            runProgram() 
                                                                       

def insertElement():
    while True:                                       
        print("\n\n<<<<<<<<<<<<<<<<<<< INSERT AN ELEMENT >>>>>>>>>>>>>>>>>>>>")
        print("\nArray:", numList)
        idx = int(input("\nEnter the index where you want to insert: "))
        num = int(input("Enter the number you want to insert: "))                              
        numList.insert(idx, num)        
        print("The element has been successfully inserted!")
        print("\nThis is the new array: \n", numList)

        insertAgain = input("\nWould you like to insert another element? [ yes / no ] : ")  
        if insertAgain.casefold() == "yes":                                              
            continue
        elif insertAgain.casefold() == "no":
            runProgram() 

def modifyElement():
    while True:
        print("\n\n<<<<<<<<<<<<<<<<<<< MODIFY AN ELEMENT >>>>>>>>>>>>>>>>>>>>")
        print("\nArray:", numList)
        idx = int(input("\nEnter the index you want to modify: "))         
        numList.pop(idx)                                                      
        num = int(input("Enter the modified number: "))                              
        numList.insert(idx, num)
        print("The element has been successfully modified!")
        print("\nThis is the new array: \n", numList)  

        modifyAgain = input("\nWould you like to modify another element? [ yes / no ] : ")  
        if modifyAgain.casefold() == "yes":                                              
            continue
        elif modifyAgain.casefold() == "no":
            runProgram() 


def deleteElement():
    while True:
        print("\n\n<<<<<<<<<<<<<<<<<<< DELETE AN ELEMENT >>>>>>>>>>>>>>>>>>>>")
        print("\nArray:", numList)
        idx = int(input("\nEnter the index you want to delete: "))         
        numList.pop(idx)
        print("The element has been successfully deleted!")
        print("\nThis is the new array: \n", numList)
                                            
        deleteAgain = input("\nWould you like to delete another contact? [ yes / no ] : ")  
        if deleteAgain.casefold() == "yes":                                              
            continue
        elif deleteAgain.casefold() == "no":
            runProgram() 

def ascendingOrder():
    while True:
        print("\n\n<<<<<<<<<<<<<<< ARRANGE IN ASCENDING ORDER >>>>>>>>>>>>>>>")
        numList.sort()
        print("\nThis is the new array:\n", numList)

        next = input("\nWould you like to return to main menu? [ yes / no ] : ")  
        if next.casefold() == "yes":                                              
            runProgram()
        elif next.casefold() == "no":
            print("\nThank you for using this program!\n")
            exit()

def descendingOrder():
    while True:
        print("\n\n<<<<<<<<<<<<<<< ARRANGE IN DESCENDING ORDER >>>>>>>>>>>>>>")       
        numList.sort()
        numList.reverse()
        print("\nThis is the new array:\n", numList)

        next = input("\nWould you like to return to main menu? [ yes / no ] : ")  
        if next.casefold() == "yes":                                              
            runProgram()
        elif next.casefold() == "no":
            print("\nThank you for using this program!\n")
            exit()

def runProgram():
    print("\n\nArray:", numList)
    while True:
        mainMenu()
        menuOption = int(input("\nWhat do you want to do?: "))

        if menuOption in (1, 2, 3, 4, 5, 6, 7):
            if menuOption == 1:
                addElement() 
            elif menuOption == 2:
                insertElement()
            elif menuOption == 3:
                modifyElement()
            elif menuOption == 4:
                deleteElement()
            elif menuOption == 5:
                ascendingOrder()
            elif menuOption == 6:
                descendingOrder()  
            elif menuOption == 7:
                print("\nThank you for using this program!\n")
                exit()                                                  
        else:
            print("Invalid Input! Choose a number on the menu and try again!")
            continue

while True:
    runProgram()