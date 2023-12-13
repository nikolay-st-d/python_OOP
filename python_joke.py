def use_condom(condom):
    if condom:
        return True
    return False


male = 1
female = 1
family = male + female
some_condom = 'Any brand'

if not use_condom(some_condom):
    family = 3
    print(f"You will gonna be {family}! Game Over!")
else:
    print("Live your life and be happy!")
