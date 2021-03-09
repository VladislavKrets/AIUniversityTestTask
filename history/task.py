import pickle


class History:

    def __init__(self):
        self.history_arr = set()
        self.score = None
        self.duplicates_count = 0

    def set_history(self, sequence: list, score: float):
        sequence = tuple(sequence)
        is_duplicate_exists = self.is_it_dupe_sequence(sequence)
        if is_duplicate_exists:
            self.duplicates_count += 1
        if is_duplicate_exists and (self.score is None or score < self.score):
            self.score = score
        else:
            self.history_arr.add(sequence)

    def is_it_dupe_sequence(self, sequence):
        return sequence in self.history_arr

    def save_history(self, filepath: str):
        with open(filepath, 'wb') as fp:
            pickle.dump(self.history_arr, fp)

    def load_history(self, filepath: str):
        self.history_arr = None
        with open(filepath, 'rb') as fp:
            self.history_arr = pickle.load(fp)

