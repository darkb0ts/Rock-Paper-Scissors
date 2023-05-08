import random
def RPSgame(option):
    user_score = 1
    YesorNo=input("Enter the Yes/No to Game: ").lower()
    if YesorNo != "N" and YesorNo != "n" :
        flag=True
        while(flag):
            User_Choose = input("enter the rock/r paper/p scissors/s: ").lower()
            # rock 0 paper
            guess=random.randint(0,2)
            Computer_Choose=option[guess]
            if User_Choose==Computer_Choose:
                print("Draw again")
                continue
            elif Computer_Choose=="r":
                if User_Choose=="s":
                    user_score-=1
                    print("Computer is",Computer_Choose,"and You Choosed",User_Choose,"and Point is",user_score)
                else:
                    print("User is Winner and"," Point is ",user_score)
                    user_score+=1
            elif Computer_Choose=="p":
                if User_Choose=="r":
                    user_score -= 1
                    print( "Computer is" , Computer_Choose , "and You Choosed" , User_Choose , "and Point is" ,
                           user_score )
                else:
                    print("User is Winner and"," Point is ",user_score)
                    user_score+=1
            elif Computer_Choose=="s":
                if User_Choose=="p":
                    user_score -= 1
                    print( "Computer is" , Computer_Choose , "and You Choosed" , User_Choose , "and Point is" ,
                           user_score )
                else:
                    print("User is Winner and"," Point is ",user_score)
                    user_score+=1
            else:
                print("invaild input")
    else:
        print("Thank For Playing")
option = ["r" , "p" , "s"]
RPSgame(option)

