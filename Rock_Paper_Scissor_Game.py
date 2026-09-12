import random 
l=['Rock🪨','Paper📄','Scissor ✂️']
'''
rock vs paper=paper wins
rock vs  scissor=rock wins
paper vs scissor=scissor wins 
'''
while True:
    UserChoice=int(input("Wanna play Rock Paper Scissor ?\n press \n 1 Yes\n 2 No | Exit "))
    if UserChoice==1:
        ucount=0
        ccount=0
        for i in range(1,6):
            uchoice=int(input("Enter your choice\n 1 Rock🪨 \n 2 Paper 📄 \n 3 Scissor ✂️ \n "))
            if uchoice==1:
                uchoice='Rock🪨'
            elif uchoice==2:
                uchoice='Paper📄'
            elif uchoice==3:
                uchoice='Scissor ✂️'
            else:
                print("Invalid input , Please try again 😊...")
                continue
            cchoice=random.choice(l)
            if uchoice==cchoice:
                print(f"Computer choice is {cchoice} \nUser choice is {uchoice} \nMatch Draw✨ ...")
                ucount+=1
                ccount+=1
            elif (uchoice=='Rock🪨' and cchoice=='Scissor ✂️')or (uchoice=='Paper📄' and cchoice=='Rock🪨')or(uchoice=='Scissor ✂️' and cchoice=='Paper📄'):
                print(f"Computer choice is {cchoice} \n User choice is {uchoice} \n User Wins👩🏻")
                ucount+=1
            else:
                print(f"Computer choice is {cchoice} \n User choice is {uchoice} \n Computer Wins💻")
                ccount+=1
            print(f"User Score: {ucount}")
            print(f"Computer Score: {ccount}")
        if ucount==ccount:
            print("Match Draw ...")   
        elif ucount > ccount:
            print("User Wins the match 👩🏻🎉🎉...")
        else:
                print("Computer wins the match 🎉🎉💻...")  
    elif UserChoice==2:
        print("Thanks for playing 😊...")
        break
    else:
        print("Invalid input , Please try again ...")

    
