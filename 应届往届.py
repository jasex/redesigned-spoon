#!/usr/bin/env python3

import random

data = {'应届生': 10, '往届生': 1}
def pick_yin():
    value_list = []
    for key, value in data.items():
        value_list += value*[key]
    pick_value = random.choice(value_list)
    return pick_value
