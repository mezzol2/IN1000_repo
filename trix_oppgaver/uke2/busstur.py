station = "Station "
message = "! How many people want to board the buss?"
boarding = " people board the buss"

def walk():
    print(f"The buss is full! {extra} people must walk.")

#station 1
waiters = int(input(f"{station}1{message}\n"))
if waiters <= 30 and waiters >=0:
    passengers = waiters
    print(f"{waiters}{boarding}")