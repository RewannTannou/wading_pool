import os
import datetime


class ScoreManager:
    def __init__(self, score_file="best_scores.txt"):
        self.score_file = score_file

    def get_best_score(self):
        if not os.path.exists(self.score_file):
            return None
        with open(self.score_file, "r", encoding="utf8") as f:
            scores = [int(line.strip().split(",")[1]) for line in f if line.strip()]
            return min(scores) if scores else None

    def save_score(self, word, attempts):
        with open(self.score_file, "a", encoding="utf8") as f:
            f.write(f"{datetime.date.today()},{attempts},{word}\n")
