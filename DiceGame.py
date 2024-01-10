import random


class Die:

    def __init__(self):
        self._value = None
        # we make it non-public because we don't want the value of the die
        # to change outside the class.
    
    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value


class Player:

    def __init__(self, die, is_computer=False): # die --> composition
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        self._counter += 1
    
    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self): # aggregation
        return self._die.roll()
    

class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("==============================")
        print("🎲Welcome to Roll the Dice!🎲")
        print("==============================")
        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break

    def play_round(self):
        # Welcome the user
        self.print_round_welcome()

        # Roll the dice
        self.roll_dice()

        # Show the values
        self.show_dice()

        # Determine winner and loser
        if self.player_value > self.computer_value:
            print("You won the round!🎉")
            self.update_counters(winner=self._player, loser=self._computer)
        elif self.computer_value > self.player_value:
            print("The computer won this round.😟 Try again.")
            self.update_counters(winner=self._computer, loser=self._player)
        else:
            print("It's a tie!😎")

        # Show counters
        self.show_counters()
        
    def print_round_welcome(self):
        print("\n---------- New Round ----------")
        input("🎲Press any key to roll the dice.🎲")

    def roll_dice(self):
        self.player_value = self._player.roll_die()
        self.computer_value = self._computer.roll_die()

    def show_dice(self):
        print(f"Your die: {self.player_value}")
        print(f"Computer die: {self.computer_value}\n")

    def update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()
    
    def show_counters(self):
        print(f"\nYour counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter}")
    
    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player) # Game over. The player won.
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer) # Game over. The computer won.
            return True
        else:
            return False
        
    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n====================")
            print("G A M E  O V E R")
            print("==============================")
            print("The computer won the game. Sorry...")
            print("==============================")
        else:
            print("\n====================")
            print("G A M E  O V E R")
            print("==============================")
            print("You won the game, congratulations!")
            print("==============================")

    
# Create instances
player_die = Die()
computer_die = Die()

my_player = Player(player_die)
computer_player = Player(computer_die, True)

game = DiceGame(my_player, computer_player)

# Start the game
game.play()