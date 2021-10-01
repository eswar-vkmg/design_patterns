from machine import Machine

if __name__ == '__main__':
    machine = Machine(4)
    print(machine)
    actions = [
        (machine.insert_coin, machine.turn_crank),
        (machine.insert_coin, machine.turn_crank),
        (machine.insert_coin, machine.remove_coin),
        (machine.remove_coin, machine.turn_crank),
        (machine.insert_coin, machine.turn_crank)
    ]

    for action_1, action_2 in actions:
        action_1()
        print(machine)
        action_2()
        print(machine)
