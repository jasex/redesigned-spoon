#!/usr/bin/env python3

import random

data = {'城镇户口': 5, '农村户口': 1}
def pick_hu():
    value_list = []
    for key, value in data.items():
        value_list += value*[key]
    pick_value = random.choice(value_list)
    return pick_value
