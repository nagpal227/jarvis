import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from email_draft import *

load_dotenv()
setup_database()
with open("personaldata.json" , "r") as f :
    user = json.load(f)

def getmultiline():
    print("enter your email body.press Enter twice on an empty line to finish:")
    lines =[]
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    emailbody ="\n".join(lines)
    return emailbody


def createemail():
    
    receiver_email = input("enter recievers email:")
    subject = input("enter the subject")
    body  = getmultiline()

    choice = input("Send or save as draft? ")

    if choice.lower() == "send":
        sendemail(receiver_email, subject, body)

    elif choice.lower() == "draft":
        create_draft(receiver_email, subject, body)
    


def sendemail(reciever_email,subject,body): 
    sender_email = os.getenv("email")
    password = os.getenv("email_password")
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = reciever_email
    message["Subject"] = subject
    message.attach(MIMEText(body,"plain"))

    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        print("Email:", sender_email)
        print("Password:", password)
        server.login(sender_email,password)
        server.send_message(message)

    print("email sent successfully")
    
def add(x):
    lists = x.split(" ")
    sum = 0 
    listn = [int(i) for i in lists]
    for i in listn:
        sum = sum + i 
    return sum 

def subtract(y , x):
    lists = x.split(" ")
    sum = 0 
    listn = [int(i) for i in lists]
    for i in listn:
        sum = sum + i 
    return y - sum 

def multiply(x):
    lists = x.split(" ")
    product = 1 
    listn = [int(i) for i in lists]
    for i in listn:
        product = product * i 
    return product

def divide(x):
    lists = x.split(" ")
    product = 1 
    listn = [int(i) for i in lists]
    for i in listn:
        product = product * i 
    return product
    
def dvwe():
    print("Hello")

def createnote(name):
    text1 = []
    print("enter stop to stop entering the lines")
    while(1>0):
        l = input("enter line")
        if(l =="stop"):
            break
        text1.append(l+"\n")
    with open(f"{name}.txt" , "w") as file1:
         file1.writelines(text1)

def view(name):
    with open(f"{name}.txt" , "r") as file1:
        text2 = file1.read()
    print(text2)
    return

def removenote(name,no):
    with open(f"{name}.txt","r") as file1:
        text2 = file1.readlines()
    text2.pop(no-1)
    with open(f"{name}.txt","w")as file1:
        file1.writelines(text2)
    return

def addlinenote(name,no):
    with open(f"{name}.txt","r") as file1:
        text2 = file1.readlines()
    a = input("enter the line you want to enter ")
    text2.insert(a+"\n",no-1)
    with open(f"{name}.txt","w")as file1:
        file1.writelines(text2)
    return

def changelinenote(name,no):
    with open(f"{name}.txt","r") as file1:
        text2 = file1.readlines()
    a = input("enter the changed line  ")
    text2[no-1] =a+"\n"
    with open(f"{name}.txt","w")as file1:
        file1.writelines(text2)
    return

def findword(name,word):
    with open(f"{name}.txt","r") as file1:
        text2 = file1.read()
    if(text2.find(word) == -1):
        print("word not found")
    else:
        print(f"word found at index{text2.find(word)}")

def addtodo(no):
    with open(f"todo{no}.txt","r") as file1:
        text = file1.readlines()
    text.append(input("enter the task"+"\n"))
    with open(f"todo{no}.txt","w") as file1:
        file1.writelines(text)

def deletetask(name,no):
    with open(f"{name}.txt","r") as file1:
        text2 = file1.readlines()
    removed = text2.pop(no-1)
    with open(f"{name}.txt","w")as file1:
        file1.writelines(text2)
    with open("deleted.txt","a") as file1:
        file1.write(removed)
    return


def greeting(type,occasion ,name ="none", time = "general"):
    if(type == "formal"):
        if(occasion == "Job Interview"):
            print(f"Good {time} , Mr.{name} i am {user["n1"]}. i am here for the interview")
        elif(occasion == "Formal Invitations"):
            print(f"hello dear , {user["n1"]} here i wanted u to join us on the occasion of {occasion}")
        elif(occasion == "Business Meeting"):
            print(f"Good {time} everyone , i am here for presenting ")
        elif(occasion == "Networking Event"):
            print(f"Good evening. It's a pleasure to be here and connect with such a diverse group of professionals."/
                   f"I'm {user["n1"]}, and I'm looking forward to some insightful conversations today.")
        elif(occasion == "Academic Ceremony"):
            print(f"Respected dignitaries, honored faculty members, and dear fellow students, good {time}."/
                  f" It is a great privilege to be present here today for this {occasion} that celebrates learning, dedication, and achievement.")
        elif(occasion == "Diplomatic Function"):
            print(f"Respected ambassadors, honored guests, and distinguished colleagues, good {time}."/
                  f" I am delighted to join you at this important occasion that celebrates dialogue, partnership, and mutual understanding.")
        elif(occasion == "Legal Proceedings"):
            print(f"Respected ambassadors, honored guests, and distinguished colleagues, good {time}."/
                  f" I am {user["n1"]} delighted to join you at this important occasion that celebrates dialogue, partnership, and mutual understanding.")
        
    elif(type == "informal but respectful"):
        if occasion == "adressing one":
            print(f"hello Mr.{name} , how are you")
        elif occasion == "adressing many":
            print(f"hey everyone , hows everyone doing ")
        elif occasion == "leaving": 
            print("byy! it was a nice time with you")
    elif(type == "casual"):
        if occasion == "adressing friends":
            print(f"hello Mr.{name} , how are you")
        elif occasion == "adressing peps in the hood":
            print(f"heyy mann!! hows it going ? ")
    return




print("hey i am jarvis. i can do many things , but still my functionality is limited right now  \n and i am text based too , sorry for inconvinence my developer is beginner and also a nerd")
activate = input(("do you want to activate me  ?"))

city = "nabha"
friends ={}
if activate.lower() == "yes":
    print('''these are the functions that i can perform:
        1.I can provide u with a custom greeting message
        2.Update your personal details
        3.I can perform calculations for you 
        4.Write, edit, view, search or delete a note for you
        5.Make a to do list
        6.Write an email for you
        7.Open a website
        8.Tell u the time
        9.Call your friend 
        10.Launch an app for you
        11.for stopping
''')
    while(1>0):
        a = int(input("enter the number of the task that you want me to perform :"))
        if(a == 1):
            typee = {1:"formal",2:"informal but respectful",3:"casual"}
            occasions1 ={1:"Job Interview",2:"Formal Invitations",3:"Business Meeting",4:"Networking Event",5:"Academic Ceremony",6:"Diplomatic Function",7:"Legal Proceedings"}
            occasions2 ={1:"adressing one",2:"adressing many",3:"leaving"}
            occasions3 ={1:"adressing friends",2:"adressing peps in the hood"}
            time = {1:"morning",2:"afternoon",3:"evening"}
            print("types of greeting \n" , typee)
            typen = int(input("tell me the type of greeting u want"))
            if(typen == 1):
                print("these are the different occasions i can give u greeting for \n" , occasions1)
                b = int(input("tell me the occasion"))
                c = (input("enter the name of the person u re witing to if not specific then leave blank:"))
                print(time)
                d = int(input("enter time slot(1or2or3):"))
                greeting(typee[typen] , occasions1[b] , c , time[d])
            elif(typen == 2):
                print("these are the different occasions i can give u greeting for \n" , occasions2)
                b = int(input("tell me the occasion"))
                c = (input("enter the name of the person u re witing to if not specific then leave blank:"))
                print(time)
                d = int(input("enter time slot(1or2or3):"))
                greeting(typee[typen] , occasions2[b] , c , time[d])
                
            elif(typen == 3):
                print("these are the different occasions i can give u greeting for \n" , occasions3)
                b = int(input("tell me the occasion"))
                c = (input("enter the name of the person u re witing to if not specific then leave blank:"))
                print(time)
                d = int(input("enter time slot(1or2or3):"))
                greeting(typee[typen] , occasions3[b] , c , time[d])
        if(a == 2):
            while(1>0):
                print("these are your current details \n" , user)
                b = input("what detail do you want to update:")
                c =input("what do you want to change it to ?")
                user[b] = c
                d = input("do you want to update anything else ? ")                
                if(d.lower() == "no"):
                    with open("personaldata.json", "w") as f:
                        json.dump(user, f, indent=4)
                    break
        if(a==4):
            print('''what do you waant to do?
                    1.create a note
                    2.view a note 
                    3.edit a note
                    4.search in a note 
                    5.delte a note ''')
            notes = int(input("enter the no of the task"))
            if(notes == 1):
                #create a note 
                name = input("enter the name of the note")
                createnote(name)
                print("note created")
                
                


            elif(notes == 2):
                #view a note 
                name = input("enter the name of the file ")
                print("here is your note:")
                view(name)
                
                     
            elif(notes == 3):
                #edit a note 
                name = input("enter the name of the file you want to edit ")
                view(name)
                while(True):
                    print('''\nwhat do you want to perform : 
                        1.remove a line
                        2.add a line
                        3.edit a line
                        4.stop ''')
                    what  = int(input("which one of these u want to perform "))
                    if(what == 1):
                        numberxyz = int(input("enter the no of line you want to remove "))
                        removenote(name,numberxyz)
                        print("the new note is:")
                        print("done")
                        view(name)
                    elif(what == 2):
                        numberxyz = int(input("enter the position at which you want to add a line"))
                        addlinenote(name,numberxyz)
                        print("done")
                        print("the new note is:")
                        view(name)
                    elif(what ==3):
                        numberxyz = int(input("enter the position of the line you want to change "))
                        changelinenote(name,numberxyz)
                        print("done")
                        print("the new note is:")
                        view(name)
                    elif(what == 4):
                        break
                        

            elif(notes == 4):
                #search for words in a note 
                name = input("enter the name of the note")
                word = input("enter the word you want to find ")
                findword(name,word)
                
            elif(notes == 5):
                #delete a note
                name = input("enter the name of the note you wan to delete ")
                os.remove(f"{name}.txt")
                print("note deleted")

                
            else:
                print("no such option available")
        if(a==5):
            no = int(input("enter the no of the to do list :"))
            while(True):
                print('''what do you want to do ?
                        1. add a task
                        2. make a task completed
                        3. delete a to do list
                        4. you are done''')
                task = (input(":"))
                if(task == 1):
                    addtodo(no)
                elif(task == 2):
                    print("these is your current to do  list")
                    view(f"todo{no}")
                    #delete()
                    # incomplete
        if(a==6):
            print("""what do you want to do :
                1.create a new email
                2.see the current drafts
                3.send an email from the drafts
                """)
            option = int(input("enter the number of the task"))
            if(option == 1):
                createemail()
            elif(option == 2):
                show_drafts()
            elif(option == 3):
                show_drafts()
                id = int(input("which draft do you want to send"))
                email = get_draft(id)
                if email:
                    reciever,subject,body = email
                    sendemail(reciever,subject,body)
                    mark_sent(id)



          

                
                

        if(a == 11):
            print("byee")
            print("hello")
            print("adfed")
            break
