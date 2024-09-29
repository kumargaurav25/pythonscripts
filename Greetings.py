import datetime

def greetings(name,greet):{
    print("Hello "+name+" "+greet+"\n")

}
    
name=input("What is your name? ")
t=datetime.datetime.now().hour

if t < 12:
    greet="Good Morning "
else:
    greet="Good Evening "

greetings(name,greet)

