#!/usr/bin/env python3

class CartesianProduct:
    def __init__(self, objects, n):
        try:
            if n < 1:
                raise ValueError('"n" must be positive') from None

            self._cursor = 0
            self._products = [[]]
            for _ in range(n):
                self._products = [product + [obj] for product in self._products for obj in objects]
        except TypeError:
            raise ValueError('"objects" must be of "Iterable" type; "n" must be of "int" type') from None

    def current(self):
        return tuple(self._products[self._cursor]) if self._cursor < len(self._products) else None

    def next(self, looped=False):
        current = self.current()

        self._cursor += 1
        if looped and self._cursor >= len(self._products):
            self._cursor = 0

        return current
