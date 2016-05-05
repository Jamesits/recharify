#!/usr/bin/env python3

import logging

# FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
# logging.basicConfig(format=FORMAT)

class MyLogger(logging.Logger):
    """
    A logging.Logger with different default options.
    """
    def __init__(self, name, level=logging.INFO):
        super().__init__(name, level)
        super().addHandler(logging.StreamHandler())
