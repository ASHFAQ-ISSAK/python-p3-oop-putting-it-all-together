#!/usr/bin/env python3


class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Used"

    def is_size_an_integer(self):
        if not isinstance(self.size, int):
            print("size must be an integer")
        else:
            print(self.size)

    def cobble(self):
        self.condition = "New"
        if self.condition != "New":
            print("Your shoe is as good as new!")
