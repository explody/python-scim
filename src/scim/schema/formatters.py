# -*- coding: utf-8 -*-

class SimpleFormatter(object):

    def __init__(self, obj, attrs, join_with=" "):

        parts = []
        for part in attrs:
            if getattr(obj,part):
                print("found:",part)
                parts.append(getattr(obj,part))
            else:
                print("not found:",part)

        self.formatted = join_with.join(parts)

    def __repr__(self):
        return self.formatted

