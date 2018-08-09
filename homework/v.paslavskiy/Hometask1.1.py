name = None
answer1 = None
answer2 = None
answer3 = None
answer4 = None
answer5 = None
if name == None:
    name = input('What is your name?:  ' )
    age = int(input("Hello {}, how old are you?:  ".format(name)))
    if age > 0 and age <= 7:
        while answer1 == 'a' or 'b' or 'c':
            answer1 = input("""What are you doing here, little baby?
                                a) I'm looking for my mommy!
                                b) I'm looking for some cookies
                                c) I'm lost
                            """)
            if answer1 != 'a' or 'b' or 'c':
                print("You should answer 'a' or 'b' or 'c'!!!")
            if answer1 == 'a':
                print("Your mommy went home, go there and find her")
                break
            elif answer1 == 'b':
                print("Cookies at the kitchen, go there and find them")
                break
            elif answer1 == 'c':
                print("Let me call to police")
                break
    elif age > 7 and age <=14:
        while answer2 == 'a' or 'b' or 'c':
            answer2 = input("""How it's going in your school?
                                a) Everything is going well
                                b) School is bull shit
                                c) I hate school, why are you asking?
                            """)
            if answer2 != 'a' or 'b' or 'c':
                print("You should answer 'a' or 'b' or 'c'!!!")
            if answer2 == 'a':
                print("Good boy!")
                break
            elif answer2 == 'b':
                print("oh you little bastard, how dare you")
                break
            elif answer2 == 'c':
                print("because I'm your father {}".format(name))
                break
    elif age > 14 and age <=21:
        while answer3 == 'a' or 'b' or 'c':
            answer3 = input("""Seems that you are teenager, what are you doing at you free time?
                                a) Dating with my girlfriend
                                b) Selling drugs
                                c) MOVE BITCH GET OUT OF MY WAY!!!
                            """)
            if answer3 != 'a' or 'b' or 'c':
                print("You should answer 'a' or 'b' or 'c'!!!")
            if answer3 == 'a':
                print("Good boy!")
                break
            elif answer3 == 'b':
                print("Oh you little bastard, I'm calling to police!")
                break
            elif answer3 == 'c':
                print("F**k you {}".format(name))
                break
    elif age > 21 and age <=40:
        while answer4 == 'a' or 'b' or 'c':
            answer4 = input("""What is your job?
                                a) I'm a president
                                b) I'm a prostitute
                                c) I'm a fireman
                            """)
            if answer4 != 'a' or 'b' or 'c':
                print("You should answer 'a' or 'b' or 'c'!!!")
            if answer4 == 'a':
                print("Don't lie to me!")
                break
            elif answer4 == 'b':
                print("Seariously? you can't be a prostitute, you are a man!!")
                break
            elif answer4 == 'c':
                print("Good job!!! you are a hero!")
                break
    elif age > 40 and age <=120:
            while answer5 == 'a' or 'b' or 'c':
                answer5 = input("""Who is your wife?
                                    a) Brain killer
                                    b) I have no wife
                                    c) The best woman ever!!!
                                """)
                if answer5 != 'a' or 'b' or 'c':
                    print("You should answer 'a' or 'b' or 'c'!!!")
                if answer5 == 'a':
                    print("I'm so sorry")
                    break
                elif answer5 == 'b':
                    print("What's wrong with you, are you a gay?")
                    break
                elif answer5 == 'c':
                    print("I'm really glad for you!")
                    break
    else:
        print("You cannot be so old, dirty lier !!!")