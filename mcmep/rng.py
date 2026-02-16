from abc import ABC, abstractmethod


class Sequence(list):

    def __init__(self, seed: int):
        super().__init__()
        self.seed = seed
        self.end_point = None

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


if __name__ == "__main__":
    sequences = []
    for i in range(100):
        prng = MiddleSquare(i, num_digits=2)
        for value in prng:
            pass
        sequence = prng._sequence
        sequences.append(sequence)
    endpoints = set(seq.end_point for seq in sequences)
    for end in endpoints:
        seqs = [seq for seq in sequences if seq.end_point == end]
        seqs.sort(key=lambda s: -len(s))
        print(f"Endpoint: {end}")
        for seq in seqs:
                print(seq.seed, "->", seq, len(seq))
        print(f"Number of sequences ending in {end}: {len(seqs)}")