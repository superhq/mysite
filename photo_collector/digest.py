# -*- coding:utf-8 -*-

import hashlib


class CalDigest:
    def __init__(self):
        pass

    @staticmethod
    def get_md5(path):
        m = hashlib.md5()
        with open(path, 'rb') as f:
            m.update(f.read())
            ret = m.hexdigest()
        return ret
