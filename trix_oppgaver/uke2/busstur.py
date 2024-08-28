station = "Station "
message = "! How many people want to board the buss?"
boarding = " people board the buss"

def walk():
    print(f"The buss is full! {extra} people must walk.")

def neg_num():
    print(f"{waiters} is negative, and we cannot have negative people.")
    print("Please try again.")
    exit()

def ppl_onboard():
    print(f'There are {passengers} people on the buss\n')

#station 1
waiters = int(input(f"{station}1{message}\n"))
if waiters <= 30 and waiters >=0:
    passengers = waiters
    print(f"{waiters}{boarding}")
elif waiters > 30:
    passengers = 30
    extra = waiters - 30
    walk()
else:
    neg_num()

ppl_onboard()

#station 2
waiters = int(input(f"{station}2{message}\n"))
if waiters <= (30 - passengers) and waiters >=0:
    passengers = passengers + waiters
    print(f"{waiters}{boarding}")
elif waiters > (30 - passengers):
    extra = waiters - (30 - passengers)
    passengers = 30
    walk()
else:
    neg_num()

ppl_onboard()

#station 3
waiters = int(input(f"{station}3{message}\n"))
if waiters <= (30 - passengers) and waiters >=0:
    passengers = passengers + waiters
    print(f"{waiters}{boarding}")
elif waiters > (30 - passengers):
    extra = waiters - (30 - passengers)
    passengers = 30
    walk()
else:
    neg_num()

print(f'\nThe buss arrives at the station with {passengers} passangers.')