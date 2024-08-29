#1. The program may or may not running depending upon what the user inputs.
#
#2. If the user inputs greater than or equal to 10, the program will run, but
#   nothing will be printed to the terminal.  If the user inputs a number less
#   than 10, the program will return an error when it tries to execute the final
#   line because Python cannot "add" an integer and a string. If the user inputs
#   a non-numerical value, the program will halt on the second line when it
#   tries to convert the value to an integer.



a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")