import config
import states


class Machine:
    def __init__(self, count=0):
        self.ball_count = count
        self.current_state = None
        self.states_mapper = {
            config.EMPTY: states.EmptyState(self),
            config.INPUT_STATE: states.NoCoinInsertedState(self),
            config.COIN_INSERTED: states.CoinInsertedState(self),
            config.NORMAL_DISPATCHED: states.BallDispatchingState(self),
            config.WINNER_DISPATCHED: states.WinnerState(self)
        }
        self.current_state = self.states_mapper[config.EMPTY] if self.ball_count == 0 \
            else self.states_mapper[config.INPUT_STATE]

    def fill_balls(self, count):
        self.current_state.fill_balls(count)

    def insert_coin(self):
        self.current_state.insert_coin()

    def remove_coin(self):
        self.current_state.remove_coin()

    def turn_crank(self):
        if self.current_state.turn_crank():
            self.current_state.dispatch()

    def __str__(self):
        return f"----- {self.current_state.name} with {self.ball_count} ball(s) remaining -----"
