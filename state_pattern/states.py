import config
from winner_logic import WinnerLogic


class State:
    def __init__(self, machine):
        self.machine = machine

    def fill_balls(self, ball_count):
        print(f"Don't have permissions to fill machine in {self.machine.current_state.name}")

    def insert_coin(self):
        print(f"Can't insert coin in {self.machine.current_state.name}")

    def remove_coin(self):
        print(f"Can't remove coin in {self.machine.current_state.name}")

    def turn_crank(self):
        print(f"Can't turn crank in {self.machine.current_state.name}")
        return False

    def dispatch(self):
        print(f"Can't dispatch in {self.machine.current_state.name}")

    def change_state(self, new_state):
        self.machine.current_state = self.machine.states_mapper[new_state]


class EmptyState(State):
    def __init__(self, machine):
        super(EmptyState, self).__init__(machine)
        self.name = config.EMPTY

    def fill_balls(self, ball_count):
        self.machine.ball_count = ball_count
        print(f'Filled {self.machine.ball_count} balls')
        self.change_state(config.INPUT_STATE)


class NoCoinInsertedState(State):
    def __init__(self, machine):
        super(NoCoinInsertedState, self).__init__(machine)
        self.name = config.INPUT_STATE

    def insert_coin(self):
        print('Coin inserted')
        self.change_state(config.COIN_INSERTED)


class CoinInsertedState(State):
    def __init__(self, machine):
        super(CoinInsertedState, self).__init__(machine)
        self.name = config.COIN_INSERTED

    def remove_coin(self):
        print('Removed coin')
        self.change_state(config.INPUT_STATE)

    def turn_crank(self):
        print('Turning crank')
        next_state = config.WINNER_DISPATCHED if self.machine.ball_count > 1 and WinnerLogic().is_a_winner() \
            else config.NORMAL_DISPATCHED
        self.change_state(next_state)
        return True


class BallDispatchingState(State):
    def __init__(self, machine):
        super(BallDispatchingState, self).__init__(machine)
        self.name = config.NORMAL_DISPATCHED

    def dispatch(self):
        self.machine.ball_count -= 1
        print('Releasing 1 Ball !')
        next_state = config.INPUT_STATE if self.machine.ball_count else config.EMPTY
        self.change_state(next_state)


class WinnerState(State):
    def __init__(self, machine):
        super(WinnerState, self).__init__(machine)
        self.name = config.WINNER_DISPATCHED

    def dispatch(self):
        self.machine.ball_count -= 2
        print('Congrats on getting 2 balls !')
        next_state = config.INPUT_STATE if self.machine.ball_count else config.EMPTY
        self.change_state(next_state)
