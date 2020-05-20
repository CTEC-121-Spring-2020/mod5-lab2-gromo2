"""
CTEC 121
<Garrett>
<Mod 5 Lab 2>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
'''
def fingerFamily(name):
    print()
    print(name, "finger,", name, "finger, where are you?")
    print("Here I am, here I am. How do you do?")
    print()

def main():
    print()
    fingerFamily("Daddy")
    print()
    fingerFamily("Mommy")
    print()
    fingerFamily("Brother")
    print()
    fingerFamily("Sister")
    print()
    fingerFamily("Baby")
    print()
'''



def ageRange(age):
    if age <= 1:
        return "I"
    elif 0 > age:
        return "U"
    elif 1 < age < 13:
        return "C"
    elif 13 < age < 18:
        return "T"
    elif 18 < age <= 120:
        return "A"
    elif age > 120:
        return "U"

def unitTest():
    print(ageRange(-1))
    print(ageRange(0))
    print(ageRange(3))
    print(ageRange(12))
    print(ageRange(15))
    print(ageRange(19))
    print(ageRange(121))

unitTest()
#main()    