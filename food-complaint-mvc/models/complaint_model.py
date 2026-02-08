from datetime import datetime
import csv

class ComplaintModel:
    FILE = "data/complaints.csv"

    def get_all(self):
        with open(self.FILE, newline='', encoding="utf-8") as f:
            data = list(csv.DictReader(f))

        # เรียงเก่า → ใหม่
        data.sort(
            key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d")
        )
        return data
    
    def get_by_id(self, cid):
        for c in self.get_all():
            if c["complaint_id"] == cid:
                return c
        return None

    def update_status(self, cid, status):
        data = self.get_all()
        for c in data:
            if c["complaint_id"] == cid:
                c["status"] = status

        with open(self.FILE, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
