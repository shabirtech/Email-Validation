from curses.ascii import isalpha, isspace
import email


email=input("Enter your email:-  ")
a,b,c=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".")^(email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        a=1
                    elif i.isalpha():
                        if i==i.upper():
                            b=1
                    elif i.isdigit():
                        continue
                    elif i=="_"or i=="." or i=="@":
                        continue
                    else:
                        c=1
                if a==1:
                    print("Wrong Email. \n Email don't need any space in email address")
                elif b==1:
                    print("Wrong Email. \nEmail address don't need any upper later.")
                elif c==1:
                    print("Wrong Email")
                else:
                    print("Right Email")
            else:
                print("Wrong Email. \n. is not present in present in email")
        else:
            print("Wrong Email. \n@ is not in Email")
    else:
        print("Wrong Email.\n First letter is not alphabet")
else:
    print("Wrong Email. \nShort Email dress")
