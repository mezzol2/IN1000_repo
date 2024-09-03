amt = int(1000)
print(f"Your account balance is {amt}.")
action = input("Would you like to deposit or withdraw money?\nWrite d or w: ")

if action == 'w':
    change = int(input("How much would you like to withdraw: "))
    if change <= amt:
        amt = amt - change
        print(f'You have withdrawn {change}, and your remaing balance is {amt}.')
    elif change > amt:
        print(f'You are too broke to withdraw {change} as you only have {amt}.')
    else:
        print('You have entered an invalid input, and your account has been deleted.')    
elif action == 'd':
    change = int(input("How much would you like to depost: "))
    amt = amt + change
    print(f'You have deposited {change}.  Your new balance is {amt}.')
    print(f'Goodbye.')
else:
    print('You have entered an invalid input, and your account has been deleted.')