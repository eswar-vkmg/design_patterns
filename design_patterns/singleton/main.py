from singleton import singleton


@singleton
class Sample:
    def __init__(self, val):
        self.val = val


if __name__ == "__main__":
    s1 = Sample(3)
    print(s1.val)

    s2 = Sample(5)
    print(s2.val)

    print(id(s1))
    print(id(s2))
    assert id(s1) == id(s2)
