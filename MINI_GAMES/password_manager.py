def checkExistance():
    import os
    if os.path.isfile('./passwords1.txt'):
        return True 
    else:
        return False
def checkIfUserExist(user):
    if checkExistance():
        with open ("passwords1.txt", 'r') as f:
            for line in f:
                u, p = line.split("|")
                if u==user:
                    print("User exist")
                    return False 
            return True        
    return False     
def add():
    user=input('Account Name: ')
    if not checkIfUserExist(user):
        import getpass
        pwd = getpass.getpass('Password: ')
        with open('passwords1.txt', 'a') as f:
            f.write(user +"|"+ pwd+"\n")
    
def view():
    if checkExistance():
        with open('passwords1.txt','r') as f:
            for line in f.readlines():
                user, pwd =line.strip().split("|")
                print("User: ",user,"Password:",pwd)
    else:
        print("there is no file with users")
def main():
    while True:
        mode = input("Would you like to add a new password, view existing ones or quit? ('a' for adding new password OR 'v' fo view OR 'q' to quit): ")
        if mode =='v':
            view()
        elif mode =='a':
            add()
        elif mode=='q':
            quit()
        else:
            print("invalid mode, try again")
            continue
if __name__=='__main__':
    '''in main() you choose 3 options, to quit, to view passwords and to add username & password.
    if you decide to view first program will check if the password1.txt is exist by checkExistance(). if True it will open password1.txt and show you all, if False give you info that not exist
    if you decide to add, first program will check if username exist by checkIfUserExist. If exist show info that exist and return False, else return True and in add() function you will add user and password'''
    main()