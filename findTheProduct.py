# Accept two int values from the user and return their product.
# If the product is greater than 1000, then return their sum

def get1st():
    # ask for 1st value.
    print('''Hey, did you know I'm good with math operations?\n'''
          '''Come on, give me a number, any number, but don't crazy!''')
    firstValue = int(input())
    while firstValue > 1000 or firstValue < 0:
        print("I said don't go crazy. Give a number between 0 - 1000, please")
        firstValue = input()
    return firstValue

def get2nd():
    print()
    print("Now choose another number")
    secondValue = int(input())
    while secondValue > 1000 or secondValue < 0:
        print("Remember not to go Crazy! Something between 0 - 1000")
        secondValue = input()
    return secondValue

def getProduct():
    product = firstValue * secondValue
    Sum = firstValue + secondValue
    if product > 1000:
        return "I'm too lazy to multiply that. Gonna add them for you. Their result is: " + str(Sum) 
    else:
        return str(firstValue) + " times " + str(secondValue) + " is " + str(product)
        
firstValue = get1st()
secondValue = get2nd()
print()
print(getProduct())
