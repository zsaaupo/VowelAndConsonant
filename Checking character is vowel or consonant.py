"""
Check character is vowel or consonant
"""
print(__doc__)
UserInupt = input("Endter the character = ")

if(UserInupt == "a" or UserInupt == "e" or UserInupt == "i" or UserInupt == "o" or UserInupt == "u" or UserInupt == "A" or UserInupt == "E" or UserInupt == "I" or UserInupt == "O" or UserInupt == "U"):
    print(UserInupt, "is Vowel")
elif(UserInupt == "b" or UserInupt == "c" or UserInupt == "d" or UserInupt == "f" or UserInupt == "g" or UserInupt == "h" or UserInupt == "j" or UserInupt == "k" or UserInupt == "l" or UserInupt == "m" or UserInupt == "n" or UserInupt == "p" or UserInupt == "q" or UserInupt == "r" or UserInupt == "s" or UserInupt == "t" or UserInupt == "w" or UserInupt == "x" or UserInupt == "y" or UserInupt == "z" or UserInupt == "B" or UserInupt == "C" or UserInupt == "D" or UserInupt == "F" or UserInupt == "G" or UserInupt == "H" or UserInupt == "J" or UserInupt == "K" or UserInupt == "L" or UserInupt == "M" or UserInupt == "N" or UserInupt == "P" or UserInupt == "Q" or UserInupt == "R" or UserInupt == "S" or UserInupt == "T" or UserInupt == "W" or UserInupt == "X" or UserInupt == "Y" or UserInupt == "Z"):
    print(UserInupt, "is Consonant")
else:
    print("Nothing")