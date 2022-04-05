#!/usr/bin/python3
import random
import os


def nameFunc():
   
    nameList = input("Enter name for generating password? \n>> ").split()
   
    if len(nameList) > 1:
        nameOrderChoice = input("Do you want to randomize name order ([Y]es/[N]o) (Default = No)? \n>> ")
        if nameOrderChoice.lower() == 'y':
            random.shuffle(nameList)
    
    nameOrdered = "".join(nameList)

    passName = ''.join(map(random.choice, zip(nameOrdered.lower(), nameOrdered.upper())))

    return passName

def randomNumGen():
    numberList = ['0','1', '2', '3', '4', '5', '6' , '7' , '8', '9']
    numPassList = []
    numLen = input("\nHow many digits to be included (Default = 4)? \n>> ")
    
    if numLen == '':
        numLen = 4
    
    for i in range(int(numLen)):
        numPassList.append(random.choice(numberList))
    
    return "".join(numPassList)


def num():
    
    numChoice = input("\nDo you want to include number/year/DOB in your password ([y]es/[r]andom/[n]o) (Deafult = y)? \n>> ")
    if (numChoice.lower() == 'y' or numChoice  == ''):
        number = input("Enter number/year/DOB for generating password? \n>> ")
    elif numChoice.lower() ==  'r':
        number = randomNumGen()
    else:
        number = ''

    return number


def specialChar():

    specialChar = ["!", "@", "#", "$", "%", "^", "&", "*", "~", "?", ";", ":", "-", "|"]
    passSpecialchar = []

    specialCharChoice = input("\nHow many Special Character to be included [Default = 1]? \n>> ")

    if specialCharChoice == "":
        specialCharLen = 1
    else:
        specialCharLen = int(specialCharChoice)
    
    for _ in range(specialCharLen):
        passSpecialchar.append(random.choice(specialChar))
    
    return "".join(passSpecialchar)


def logo():

    os.system("cls")        
    pyNPGLogo = """
#############################################################
#        PYTHON - Name Based Password Generator (Py-NPG)    #   
#############################################################
#                         CONTACT                           #
#############################################################
#               DEVELOPER : 0xViKi                          #
#          Github : https://github.com/0xViKi               #
#############################################################
	"""

    print(pyNPGLogo)

def main():

    logo()
    passName = nameFunc()
    print("-"*80)
    passNumber = num()
    print("-"*80)
    passSpecialString = specialChar() 
    finalPassList = [passName, passSpecialString, passNumber]
    print()
    print("Generated password")
    print('-'*80)
    print(">> ","".join(finalPassList))
    print('-'*80)

if __name__ == "__main__":
    main()