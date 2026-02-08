import csv

class StallModel:
    def summary(self):
        with open("data/stalls.csv", newline='', encoding="utf-8") as f:
            stalls = list(csv.DictReader(f))
        with open("data/complaints.csv", newline='', encoding="utf-8") as f:
            complaints = list(csv.DictReader(f))

        result = []
        for s in stalls:
            count = sum(1 for c in complaints if c["stall_id"] == s["stall_id"])
            result.append((s["name"], count))
        return result
