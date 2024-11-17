import random
#user's name
user_name=input("enter your name:")
#scores
user_score=0
machine_score=0
paper=10
scissor=20
rock=30
#start
match_count=0
while match_count<3:
    match_count+=1
    #user's choice
    print("\nchoose an option:")
    print("1.paper")
    print("2.scissor")
    print("3.rock")
    user_choice=input(f"{user_name}enter your choice(1,2,or 3):")
    if user_choice=='1':
        user_value=paper
        user_choice_name='paper'
    elif user_choice=='2':
        user_value=scissor
        user_choice_name='scissor'
    elif user_choice=='3':
        user_value='rock'
        user_choice_name='rock'
    else:
        print("invalid input! please enter 1,2,or 3.")
        continue
    # machine random
    machine_choice=random.randint(1,3)
    if machine_choice==1:
        machine_value=paper
        machine_choice_name='paper'
    elif machine_choice==2:
        machine_value=scissor
        machine_choice_name='scissor'
    else:
        machine_value=rock
        machine_choice_name='rock'
    # display choices
    print(f"{user_name}chose: {user_choice_name}")
    print(f"machine chose:{machine_choice_name}")

    # determine the winner of the macth
    if user_value==machine_value:
        print("it's a draw!")
        user_score+=1
        machine_score+=1
    elif (user_value ==paper and machine_value ==rock)or\
         (user_value == scissor and machine_value == paper)or\
         (user_value == rock and machine_value == scissor):
        print(f"{user_name}wins this match!")
        user_score+=2
    else:
        print("machine wins this match!")
        machine_score += 2
# after 3 matches,print the overall winner
print("\ngame over!")
if user_score>machine_score:
      print(f"{user_name} is the overall winnwer!")
elif user_score<machine_score:
      print("machine is the overall winner!")
else :
      print("the game is a draw!")
        
                      
