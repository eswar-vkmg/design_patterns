from adaptee import AddNumbersV2, AddNumbersV3
from adapter import AddNumbers

if __name__ == "__main__":
    sum_obj_1 = AddNumbers([1, 2], AddNumbersV2)
    res_1 = sum_obj_1.add_nums()
    print(res_1)

    sum_obj_2 = AddNumbers([5.2, 8.9], AddNumbersV3)
    res_2 = sum_obj_2.add_nums()
    print(res_2)
