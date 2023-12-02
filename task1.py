import csv
import hashlib
h=hashlib.sha256()


def Register( username,passowrd):
    with open("data.csv",'a',newline='\n') as data:
        
       cwriter= csv.writer(data)
       cwriter.writerow([username,passowrd])
       return cwriter

def Login(username,password):
        
            with open('data.csv','r')as file:
                creader = csv.reader(file)
                for row in creader:
                    if (row[0]==username and row[1]==password):
                        return "Login Successful"
                    
        
     
def Hashing(password):
    h.update(password.encode())
    return h.hexdigest()


condition=True
while condition:
    choice = int(input("enter the choice 1: to login 2: to register 3: exit the page"))

    
    if choice==1:
        x=(input("enter the username"))
        y=input("enter the password")
        z=Login(x,Hashing(y))
        if z=="Login Successful":
            print("login successful")
        else :
            print("invalid user name or password")
    elif choice == 2:
        x=(input("enter the username"))
        y=input("enter the password")
        w=Register(x,Hashing(y))
        if w!=None: 
            print("registration successfull")
        else:
            print("Registration failed")
    elif choice == 3:
        print("thank you for using")
        condition=False
    else:
        print("invalid choice ")
