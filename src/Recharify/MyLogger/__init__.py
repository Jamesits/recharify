#!/usr/bin/env python3

import logging


class MyLogger(logging.Logger):
    def __init__(self, name, level=logging.INFO):
        super().__init__(name, level)
        super().addHandler(logging.StreamHandler())
        # logger.setLevel(logging.INFO)
