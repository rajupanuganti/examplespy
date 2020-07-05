import os
 
choice = input("Shut Down your Computer ? ( y or n ) ")
 
if choice == 'y' or choice == 'Y':
    os.system("shutdown /s")
else:
    print("Exiting the program doing nothing")