from abc import ABC, abstractmethod


class Sequence(list):

    def __init__(self, seed: int):
        super().__init__([seed])
        self.end_point = None

    @property
    def seed(self):
        return self[0]

    def finalize(self, value):
        if value == self[-1]:
            self.end_point = value


class AbstractPRNG(ABC):

    def __init__(self, seed: int, modulus: int):
        if seed < 0:
            raise ValueError("Seed must be non-negative.")
        if modulus <= 0:
            raise ValueError("Modulus must be positive.")
        super().__init__()
        self._current = seed
        self._modulus = modulus
        self._sequence = Sequence(seed)

    def __iter__(self):
        return self

    def __next__(self):
        value = self._next()
        if value in self._sequence:
            self._sequence.finalize(value)
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


class LinearCongruentialGenerator(AbstractPRNG):

    def __init__(self, seed: int, modulus: int, multiplier: int, increment: int):
        super().__init__(seed, modulus)
        self._multiplier = multiplier
        self._increment = increment

    def _next(self):
        return (self._multiplier * self._current + self._increment) % self._modulus


if __name__ == "__main__":
    pass
    # sequence_dict = {}
    # for i in range(100):
    #     prng = MiddleSquare(i, num_digits=2)
    #     for value in prng:
    #         pass
    #     sequence = prng._sequence
    #     try:
    #         sequence_dict[sequence.end_point].append(sequence)
    #     except KeyError:
    #         sequence_dict[sequence.end_point] = [sequence]
    # for l in sequence_dict.values():
    #     l.sort(key=lambda s: -len(s))
    # for key, value in sequence_dict.items():
    #     print(f"Sequences ending with {key}")
    #     visited = set()
    #     for seq in value:
    #         if seq.seed in visited:
    #             continue
    #         split = 0
    #         for val in seq:
    #             if val in visited:
    #                 break
    #             split += 1
    #         print(seq[:split], "->", seq[split:], f" (len={len(seq)})")
    #         visited |= set(seq)