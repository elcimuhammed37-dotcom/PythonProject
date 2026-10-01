import random
random_number= random.randint(1,100)
remainign_atempt=5
attempt_count=0
score=100
print(f" your starting score {score} and starting prediction attempt {remainign_atempt}")
while remainign_atempt > 0:
    attempt_count+=1
    guess= int(input("the number you mentioned must be between 1 and 100. what is your guess? "))
    if guess < 0 or guess >100:
        print("your guess is illegal. Please make a prediction that complies with the rules. ")
        continue
    if guess==random_number:
        print(f"congratulations! you guessed number correctly on your {attempt_count}.attempt")
        print(f"your total score is {score}")
        break
    elif guess < random_number:
        print(f"try a larger number")
    else :
        print("try a smaller number")
    remainign_atempt-=1
    score-=15
    if remainign_atempt>0:
        print(f"remaining attempt {remainign_atempt}")
        print(f"your current score {score}")
    else:
        print(f"unfortunately! you run out of attempts")
        print(f"your total score {score}")
        print(f"the number to be guessed was : {random_number}")




