from ducks import ADuck, BDuck, CDuck
from fly_behaviour import FastFlyBehaviour, SlowFlyBehaviour
from quack_behaviour import LowQuackBehavior, HighQuackBehaviour

if __name__ == "__main__":
    a_duck_1 = ADuck(LowQuackBehavior(), FastFlyBehaviour())
    a_duck_2 = ADuck(LowQuackBehavior(), SlowFlyBehaviour())

    b_duck_1 = BDuck(HighQuackBehaviour(), FastFlyBehaviour())
    b_duck_2 = BDuck(HighQuackBehaviour(), SlowFlyBehaviour())

    c_duck_1 = CDuck(LowQuackBehavior(), FastFlyBehaviour())
    c_duck_2 = CDuck(HighQuackBehaviour(), SlowFlyBehaviour())

    for duck_obj in [a_duck_1, a_duck_2, b_duck_1, b_duck_2, c_duck_1, c_duck_2]:
        duck_obj.perform_quack()
        duck_obj.perform_fly()
        print()
