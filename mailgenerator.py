#var email = "mailgen.only@protonmail.com";

#var min = 10000;
#var max = 99990;
#var rand = Math.floor(Math.random() * (max - min + 1)) + min;
#var email_split = email.split('@');

#return email_split[0]+'+only'+rand+'@'+email_split[1];


import random
import datetime

mail = input('Enter mail: ')
count = input('How many generates: ')
now = datetime.datetime.now()
d = now.strftime("%d%m%Y%H%M%S")
f = open(".\\"+d+".txt","w+")

def randafter():
    return random.randint(10000,99990)

def generatemail(maill):
    mail_split = maill.split("@")
    return mail_split[0]+"+only"+str(randafter())+"@"+mail_split[1]

gencount = 0
for x in range(0, int(count)):
    gencount = x
    umail = generatemail(mail)
    print(umail)
    f.write(umail+"\n")

f.close()
print("Generated "+str(x)+ " mail adresses and saved "+d+".txt")