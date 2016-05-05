#!/usr/bin/env python3

from collections import OrderedDict
import json


class RecharifyConfig(OrderedDict):
    def __init__(self, data=None):

        if isinstance(data, basestring):
            super().__init__(json.loads(data))
        elif isinstance(data, dict):
            super().__init__(data)
        else:
            super().__init__()

    def __str__(self):
        return json.dumps(self)