import random as rd

# Nunber of trails user needs to Guess the Nunber generated by random function
no_of_trails = int(input("Give The number of Trials to guess the Number form 1-100:- "))
rand_range = rd.randint(0,100)
input_ = int(input("Enter First Guess:- "))

for i in range(no_of_trails+1):
    if input_==rand_range:
        print(f"Congratulations {rand_range} is the Random Number and it took you {i} trails")
        break
    elif input_!=rand_range:
        input_ = int(input("Guess the Next Number:- "))
    if input_>rand_range:
        print("Enter a Smaller Number")
    if input_<rand_range:
        print("Enter a Greater Number")
    if i >= no_of_trails :
        print("Sorry you Lose Try Again!!")
    
