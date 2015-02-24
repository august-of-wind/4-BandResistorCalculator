#!/usr/bin/env python
def concInts(x, y):
    return x*10+y

def ResistorCheck():
           userInput = raw_input("Option 1.) Print all potential resistor band colors.\n Option 2.) Proceed to ResitorCheck program.\n Type 1 or 2 to proceed: ")
           if(userInput.lower() == "2"):
               print("All potential colors for FIRST THREE BANDS are:\nBlack\nBrown\nRed\nOrange\nYellow\nGreen\nBlue\nViolet\nGrey\nWhite")
               print("All potential colors for FOURTH BAND are:\nBlack\nBrown\nRed\nOrange\nYellow\nGreen\nBlue\nViolet")
               ResistorCheck()
           else:
               band1 = raw_input("Band 1 color: ")
               band2 = raw_input("Band 2 color: ")
               band3 = raw_input("Band 3 color: ")
               outputArray = []
               for band in [band1, band2]:
                          tempNum = "0"
                          if band.lower() == "black":
                                     tempNum = 0
                                     outputArray.append(tempNum)
                          elif band.lower() == "brown":
                                     tempNum = 1
                                     outputArray.append(tempNum)
                          elif band.lower() == "red":
                                     tempNum = 2
                                     outputArray.append(tempNum)
                          elif band.lower() == "orange":
                                     tempNum = 3
                                     outputArray.append(tempNum)
                          elif band.lower() == "yellow":
                                     tempNum = 4
                                     outputArray.append(tempNum)
                          elif band.lower() == "green":
                                     tempNum = 5
                                     outputArray.append(tempNum)
                          elif band.lower() == "blue":
                                     tempNum = 6
                                     outputArray.append(tempNum)
                          elif band.lower() == "violet":
                                     tempNum = 7
                                     outputArray.append(tempNum)
                          elif band.lower() == "grey":
                                     tempNum = 8
                                     outputArray.append(tempNum)
                          elif band.lower() == "white":
                                     tempNum = 9
                                     outputArray.append(tempNum)
                          else:
                                     print("Sorry, your input did not match any know resistor-band colors.")
                                     print("\n")
                                     ResistorCheck()
               toMultiply = concInts(outputArray[0], outputArray[1])
               multiplier = 0
               if band3.lower() == "black":
                          multiplier = 1
               elif band3.lower() == "brown":
                          multiplier = 10
               elif band3.lower() == "red":
                          multiplier = 100
               elif band3.lower() == "orange":
                          multiplier = 1000
               elif band3.lower() == "yellow":
                          multiplier = 10000
               elif band3.lower() == "green":
                          multiplier = 100000
               elif band3.lower() == "blue":
                          multiplier = 1000000
               elif band3.lower() == "violet" :
                          multiplier = 10000000
               else:
                          print("Sorry, your input did not match any know resistor-band colors.")
                          print("\n")
                          ResistorCheck()
               result = multiplier*toMultiply
               print("Your resistor has a resistance of {} ohms.").format(result)
               print("Program completed. Would you like to check another resistor?")
               donePrompt = raw_input("Yes or No: ")
               if donePrompt.lower() == "yes":
                          ResistorCheck()
               else:
                          print("Program completed")
              
ResistorCheck()
