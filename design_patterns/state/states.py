class State:
    def refill(self, num_balls):
        print("You cant refill the machine now")

    def insert_coin(self):
        print("You cant insert a coin now")

    def remove_coin(self):
        print("YOu cant remove the coin now")

    def turn_crank(self):
        print("You cant turn the crank now")

    def dispense(self):
        print("Gumball can't be dispensed now")


class EmptyState(State):
    def __init__(self, ball_machine):
        self.ball_machine = ball_machine

    def refill(self, num_balls):
        self.ball_machine.count = num_balls
        print(f'EMPTY_STATE: Refilling machine with {num_balls} balls')
        if self.ball_machine.count > 0:
            self.ball_machine.current_state = self.ball_machine.no_coin_state


class NoCoinState(State):
    def __init__(self, ball_machine):
        self.ball_machine = ball_machine

    def insert_coin(self):
        print('NO_COIN_STATE: Inserted coin')
        self.ball_machine.current_state = self.ball_machine.coin_loaded_state


class CoinLoadedState(State):
    def __init__(self, ball_machine):
        self.ball_machine = ball_machine
        self.winner_counter = 1

    def turn_crank(self):
        if self.ball_machine.count >= 2 and self.winner_counter == 2:
            print('COIN_LOADED_STATE: Crank turned: Lucky Winner')
            self.winner_counter = 0
            self.ball_machine.current_state = self.ball_machine.winner_state
            self.ball_machine.current_state.dispense()
        elif self.ball_machine.count >= 1:
            print('COIN_LOADED_STATE: Crank turned: Coin accepted')
            self.ball_machine.current_state = self.ball_machine.sold_state
            self.winner_counter += 1
            self.ball_machine.current_state.dispense()
        else:
            print('COIN_LOADED_STATE: Crank turned: empty machine, coin rejected')
            self.ball_machine.current_state = self.ball_machine.empty_state

    def remove_coin(self):
        print('COIN_LOADED_STATE: Coin removed')
        self.ball_machine.current_state = self.ball_machine.no_coin_state


class SoldState(State):
    def __init__(self, ball_machine):
        self.ball_machine = ball_machine

    def dispense(self):
        print('SOLD_STATE: Dispensing a ball')
        self.ball_machine.count -= 1
        if self.ball_machine.count == 0:
            self.ball_machine.current_state = self.ball_machine.empty_state
        else:
            self.ball_machine.current_state = self.ball_machine.no_coin_state


class WinnerState(State):
    def __init__(self, ball_machine):
        self.ball_machine = ball_machine

    def dispense(self):
        print('WINNER_STATE: Dispensing 2 balls')
        self.ball_machine.count -= 2
        if self.ball_machine.count == 0:
            self.ball_machine.current_state = self.ball_machine.empty_state
        else:
            self.ball_machine.current_state = self.ball_machine.no_coin_state

