questionsAnswers={"What does CPU stand for?": ["a",{"a":"Central Processing Unit", "b":"Central processing Udar", "c":"Central Part Unit"}],
                  "What does CIA stand for?": ["b",{"a":"Central Information Appearence", "b":"Central Intelligence Agency", "c":"Coma Intelgent Apart"}],
                  "What does FBI stand for?": ["c",{"a":"Federal Big invest", "b":"Federal Baby Investigation", "c":"federal bureau of investigation"}]}
def game():
    p=0
    for k,v in questionsAnswers.items():
        print(k)
        for liter, ans in v[1].items():
            print(liter,":",ans)
        answer = input("Type your answer: ").lower()
        print(v[0])
        if answer== v[0]:
            p += 1 
            print("Correct")
        else:
            print("Incorrect")   

    print("Your punctation for all game is:"+ str(p))        
def playing():
    print("Welcom to my computer quiz")
    while True:
        playing = input("Do you wanna play? Type y or n: ")
        if playing.lower() =="n":
            quit()
        elif playing.lower() == "y":
            game()
            quit()
        else:
            print("type y or n")
if __name__=='__main__':
    playing()