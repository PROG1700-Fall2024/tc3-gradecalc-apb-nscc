# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.

"""
Student Name:    W0487099
Program Title:   Grade Point Calculator
Description:    This program will get input from a user and convert a letter grade into a number grade
"""

#Initialize Variables

letterToGradeConversionList = ["F", "D", "C", "B", "A"] #Each grade is put into the index value of the list that the number is equal to A=4, B=3,C=2,D=1,F=0

letterGrade = ""
modifier = ""
letterValue = 0.0
modifierValue = 0.0

gradeValue = 0.0

def GetLetterGrade():
    _letterGrade = input("Please enter a letter grade: ")
    if (_letterGrade.upper() == "A") or (_letterGrade.upper() == "B") or (_letterGrade.upper() == "C") or (_letterGrade.upper() == "D") or (_letterGrade.upper() == "F"):
        return _letterGrade
    else:
        print("You entered an invalid grade, please try again.")
        return GetLetterGrade()
    
def GetModifier():
    _modifier = input("Please enter a modifier (+, - or nothing): ")
    if _modifier == "+" or _modifier == "-" or _modifier == "" or _modifier == "nothing":
        return _modifier
    else:
        print("You entered an invalid grade, please try again.")
        return GetModifier()

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Describe the program to the user

    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +,- or nothing")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0\n")

    #Get the user to input a letter grade (and determine if it is valid)

    letterGrade = GetLetterGrade()

    #Get the user to input a modifier (and determine if it is valid)

    modifier = GetModifier()

    #Calculate grade (and enforce special rules)

    letterValue = letterToGradeConversionList.index(letterGrade.upper()) #Get value from the index of the list that the letter is in
    

    match modifier: # Adjust modifier value based on the value the user inputed
        case "": modifierValue = 0.0
        case "nothing": modifierValue = 0.0
        case "+": modifierValue =  0.3
        case "-": modifierValue = -0.3

    if (modifier == "+" or modifier == "-") and letterGrade.upper() == "F": #Make sure if user tries to add a modifier to "F" it will tell the user that isn't possible and will set the modifierValue to 0
        print("'F's cannot have modifiers!")
        modifierValue = 0.0


    gradeValue = letterValue + modifierValue


    if gradeValue > 4.0:     #Make sure that grades don't go above 4 or less than 0
        gradeValue = 4.0
    elif gradeValue < 0.0:
        gradeValue = 0.0


    #Display Grade to the user

    print("")
    print(f"The numeric value is: {gradeValue}")

    #Your code ends on the line above
main()
