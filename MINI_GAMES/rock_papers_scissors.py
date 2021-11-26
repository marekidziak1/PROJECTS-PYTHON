import random
def game():
    lst = ['rock', 'paper', 'scizzors']
    punc=0
    comPunc=0
    while True:
        choice = input("Type 1 for rock, 2 for paper, 3 for scizzors, or q to quit ")
        if choice not in ["1","2","3"]:
            if choice == 'q':
                print("goodbye, you won "+str(punc)+" times and you lose "+str(comPunc)+" times")
                quit()
            continue   
        computerChoice=random.choice(lst)
        print("Computer choice is: "+str(computerChoice))
        if computerChoice != lst[int(choice)-1]:
            if (computerChoice=='rock'):
                if choice == '2':
                    print("You win")
                    punc+=1 
                    continue
            elif (computerChoice=='paper'):
                if choice == '3':
                    print("You win") 
                    punc+=1  
                    continue
            elif (computerChoice=='scizzors'):
                if choice == '1':
                    print("You win") 
                    punc+=1 
                    continue
            print("You lose")
            comPunc+=1
        else: 
            print("the same choices, try again")
if __name__=='__main__':
    game()