from abc import ABC, abstractmethod


class Sequence(list):

    def __init__(self):
        super().__init__()


class AbstractPRNG(ABC):

    def __init__(self, seed: int, modulus: int):
        if seed < 0:
            raise ValueError("Seed must be non-negative.")
        if modulus <= 0:
            raise ValueError("Modulus must be positive.")
        super().__init__()
        self._current = seed
        self._modulus = modulus
        self._sequence = Sequence()

    def __iter__(self):
        return self

    def __next__(self):
        value = self._next()
        if value in self._sequence:
            raise StopIteration
        self._sequence.append(value)
        self._current = value
        return value

    @abstractmethod
    def _next(self):
        pass


class MiddleSquare(AbstractPRNG):

    def __init__(self, seed: int, num_digits: int = 2):
        super().__init__(seed, 10 ** num_digits)
        self._divider = 10 ** (num_digits // 2)

    def _next(self):
        return (self._current ** 2 // self._divider) % self._modulus


if __name__ == "__main__":
    for i in range(100):
        prng = MiddleSquare(i, num_digits=2)
        for value in prng:
            pass
        sequence = prng._sequence
        print(i, len(sequence), sequence, prng._next())
