import csv
from datetime import date

class ResponseModel:
    FILE = "data/responses.csv"

    def add(self, complaint_id, message):
        with open(self.FILE, "a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([complaint_id, date.today(), message])
