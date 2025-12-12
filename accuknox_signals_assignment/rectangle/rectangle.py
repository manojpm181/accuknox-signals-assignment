

class Rectangle:
    def __init__(self, length: int, width: int):
        if not isinstance(length, int):
            raise TypeError("length must be int")
        if not isinstance(width, int):
            raise TypeError("width must be int")
        self.length = length
        self.width = width
        # optional: keep iteration state if someone uses the instance as iterator
        # but better: make __iter__ return a fresh iterator (stateless)

    def __iter__(self):
        # return an iterator that yields two dicts in order
        # implement as generator so every new iteration is fresh
        yield {'length': self.length}
        yield {'width': self.width}

    def __repr__(self):
        return f"Rectangle(length={self.length}, width={self.width})"
