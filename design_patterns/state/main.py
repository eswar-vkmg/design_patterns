from ball_machine import BallMachine

if __name__ == '__main__':
    ball_machine = BallMachine()
    ball_machine.refill(5)

    ball_machine.insert_coin()
    ball_machine.turn_crank()

    ball_machine.insert_coin()
    ball_machine.turn_crank()

    ball_machine.insert_coin()
    ball_machine.remove_coin()

    ball_machine.insert_coin()
    ball_machine.turn_crank()

    ball_machine.insert_coin()
    ball_machine.turn_crank()
