import datetime

def main ():
    while True:
        youare= input("Press 'n' or 'new'if you want to be part of us.\nPress 'old' or 'o' if you are already with us.\n")
        if youare == "new" or youare == "n":
            newuser()
        elif youare == "old" or youare == "o":
            olduser()
        else:
            print("Tell me the truth")




def newuser():
    while True:
        newname= input ("what do you want to be called\n")
        newpass= input ("what pass you would like\n")
        for line in open("userlist.txt","a+").readlines():
            login_info = line.split()
        if newname == login_info[0] :
            print("sorry, anme is taken.\nLets try again with deferent name")
        else:
            YaRB=open("userlist.txt", "a+")
            YaRB.write(newname + " " + newpass+ "\n")
            YaRB.close()
            print("now you are register your name is:\n" + newname )
            print("and your password is:\n" + newpass )
            MashaALLAH= newname + newpass + ".txt"
            while True:
                print ("your notes: \n")
                contents= open(MashaALLAH,"r").read()
                print (contents)
                dec= input("Press yes to add a new note.\n")
                if dec == 'yes':
                    TabrakaALLAH = input("Tell me please\n")
                    SubhanALLAH= open(MashaALLAH, "a+")
                    RBIsubhanak = TabrakaALLAH + "\n" + str(datetime.datetime.now() + "\n")
                    SubhanALLAH.write(RBIsubhanak + "\n")
                    SubhanALLAH.close()
                elif dec == 'exit':
                    return False
                else :
                    print ("didnot get it")


def olduser():
    while True:
        oldname= input ("remind me with you name\n")
        oldpass= input ("verify it is you\n")
        for line in open("userlist.txt","r").readlines():
            login_info = line.split()
            print(login_info)
            if oldname == login_info[0] and oldpass == login_info[1]:
                print("Welcome Back dear!\n")
                MashaALLAH= oldname + oldpass + ".txt"
                while True:
                    print ("your notes: \n")
                    contents= open(MashaALLAH,"r").read()
                    print (contents)
                    dec= input("Press yes to add a new note.\n")
                    if dec == 'yes':
                        TabrakaALLAH = input("Tell me please\n")
                        SubhanALLAH= open(MashaALLAH, "a+")
                        RBIsubhanak = TabrakaALLAH + "\n" + str(datetime.datetime.now() + "\n")
                        SubhanALLAH.write(RBIsubhanak + "\n")
                        SubhanALLAH.close()
                    elif dec == 'exit':
                        return False
                    else :
                        print ("didnot get it")
        else :
            print("you wrote something incorrect,lets try again")
    return False


if __name__== "__main__":
  main ()
