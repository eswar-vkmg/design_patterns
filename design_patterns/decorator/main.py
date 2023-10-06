from component import Coffee, Tea
from decorator import Soy, WhippedCream

if __name__ == "__main__":
    bev1 = Soy(WhippedCream(Coffee()))
    bev2 = WhippedCream(Coffee())
    bev3 = WhippedCream(Soy(Tea()))

    for obj in [bev1, bev2, bev3]:
        print(obj.describe())
        print(obj.cost())
        print()
