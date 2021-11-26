import random 
numbers=[]
def typeNumber():
    while True:
        inputNumber= input("Type your number: ")
        if inputNumber.isdigit():
            inputNumber = int(inputNumber)
            if inputNumber in numbers:
                print("you typed this number earlier, try again")
                continue
            else:
                numbers.append(inputNumber)
                return inputNumber
        else:
            print("your number must be digit,try again")
def game(number):
    inputNumber= typeNumber()
    while inputNumber != number:
        if inputNumber >number:
            print("the number is smaller")
        elif inputNumber<number:
            print("the number is bigger")
        inputNumber= typeNumber()
    print("you win by "+str(len(numbers))+" try")   
def startStop():
    while True:
        start,stop =  input("Type a START number: "), input("Type a STOP number: ")
        if start.isdigit() and stop.isdigit():
            if stop<start:
                print("stopNumber must be bigger than startNumber")
                continue
            number = random.randrange(int(start), int(stop))
            game(number)   
            quit()
        else:
            print("type two integers!")
if __name__ == "__main__":
    startStop()