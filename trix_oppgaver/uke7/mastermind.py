from random import randint

class MasterMind:
    def __init__(self) -> None:
        self._code = []
        for i in range(4):
            self._code.append(randint(1,6))
    
    def hent_bruker_gjett(self):
        guess = input("Guess a 4 digit with digits 1 through 6: ")
        guess_list = []
        for num in guess:
            guess_list.append(int(num))
        return guess_list
    
    def sjekk_gjett(self, guess):
        reveal = ["X", "X", "X", "X"]
        for i in range(4):
            if self._code[i] == guess[i]:
                reveal[i] = self._code[i]
        return reveal
    
    def spill(self):
        win = False
        times_played = 0

        while not win:
            times_played += 1
            guess = self.hent_bruker_gjett()
            print(self.sjekk_gjett(guess))
            if guess == self._code:
                win = True
        
        print(f"Congrats! You won after {times_played} guesses.")

game = MasterMind()
game.spill()
        