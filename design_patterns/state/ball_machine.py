from states import State, EmptyState, NoCoinState, CoinLoadedState, SoldState, WinnerState


class BallMachine:
    def __init__(self):
        self.empty_state = EmptyState(self)
        self.no_coin_state = NoCoinState(self)
        self.coin_loaded_state = CoinLoadedState(self)
        self.sold_state = SoldState(self)
        self.winner_state = WinnerState(self)
        self.current_state = self.empty_state
        self.count = 0

    def refill(self, num_balls):
        self.current_state.refill(num_balls)

    def insert_coin(self):
        self.current_state.insert_coin()

    def remove_coin(self):
        self.current_state.remove_coin()

    def turn_crank(self):
        self.current_state.turn_crank()
