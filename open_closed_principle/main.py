from config import ANDROID, IOS, SMALL, LARGE, SD, MTK, BIONIC, SPECIFICATION_OBJ_MAP, AND, OR, SINGLE
from filter import ItemFilter
from functools import reduce

class Product:
    def __init__(self, name, os, size, processor):
        self.name = name
        self.os = os
        self.size = size
        self.processor = processor

    def __repr__(self):
        return f'{self.name}'


def process_request(phones, request):
    spec_obj_list = []
    result_list = []
    for condition in request['conditions']:
        spec_obj = SPECIFICATION_OBJ_MAP[condition](condition)
        spec_obj_list.append(spec_obj)
    consolidated_specs = None
    if request['mode'] == SINGLE:
        consolidated_specs = spec_obj_list[0]
    elif request['mode'] == AND:
        consolidated_specs = reduce(lambda spec_1, spec_2: spec_1 & spec_2, spec_obj_list)
    elif request['mode'] == OR:
        consolidated_specs = reduce(lambda spec_1, spec_2: spec_1 | spec_2, spec_obj_list)
    for phone in ItemFilter().filter(phones, consolidated_specs):
        result_list.append(phone)

    return result_list


def get_all_phones():
    iphone_se = Product('iPhone SE', IOS, SMALL, BIONIC)
    iphone_12_max = Product('iPhone 12 Max', IOS, LARGE, BIONIC)
    galaxy_s21_max = Product('Galaxy s21 max', ANDROID, LARGE, SD)
    asus_zenfone_8 = Product('Zenfone 8', ANDROID, SMALL, SD)
    nord_2 = Product('Nord 2', ANDROID, LARGE, MTK)
    pixel_4a = Product('Pixel 4a', ANDROID, SMALL, SD)
    dummy_iphone = Product('dummy iphone', IOS, LARGE, MTK)
    return [iphone_se, iphone_12_max, galaxy_s21_max, asus_zenfone_8, nord_2, pixel_4a, dummy_iphone]


if __name__ == "__main__":
    phones = get_all_phones()
    requests = [
        {"mode": SINGLE, "conditions": [IOS]},
        {"mode": AND, "conditions": [SMALL, ANDROID]},
        {"mode": OR, "conditions": [SMALL, SD]}
    ]
    for request in requests:
        result = process_request(phones, request)
        conditions = (" " + request['mode'] + " ").join(request['conditions'])
        print(f"{conditions}: {result}")
