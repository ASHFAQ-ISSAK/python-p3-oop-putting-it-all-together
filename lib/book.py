#!/usr/bin/env python3


class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def is_page_count_integer(self):
        if not isinstance(self.page_count, int):
            print("page_count must be an integer")
        else:
            print(self.page_count)
