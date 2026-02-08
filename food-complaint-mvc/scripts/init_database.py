import csv
import os

os.makedirs("data", exist_ok=True)

def write_csv(filename, header, rows):
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

# -----------------------------
# CANTEENS
# -----------------------------
write_csv(
    "data/canteens.csv",
    ["canteen_id", "name", "location"],
    [
        ["C01", "โรงอาหารกลาง", "อาคาร A"],
        ["C02", "โรงอาหารวิศวะ", "อาคาร B"],
        ["C03", "โรงอาหารวิทย์", "อาคาร C"],
    ]
)

# -----------------------------
# STALLS
# -----------------------------
write_csv(
    "data/stalls.csv",
    ["stall_id", "name", "canteen_id"],
    [
        ["S01", "ข้าวแกงป้าแดง", "C01"],
        ["S02", "ก๋วยเตี๋ยวเรือ", "C01"],
        ["S03", "อาหารตามสั่ง", "C02"],
        ["S04", "ข้าวมันไก่", "C02"],
        ["S05", "ส้มตำ", "C03"],
        ["S06", "ชานมไข่มุก", "C03"],
        ["S07", "กาแฟสด", "C01"],
        ["S08", "ขนมหวาน", "C02"],
    ]
)

# -----------------------------
# COMPLAINTS
# -----------------------------
write_csv(
    "data/complaints.csv",
    ["complaint_id", "stall_id", "date", "type", "detail", "status"],
    [
        ["CP01", "S01", "2026-02-01", "อาหารไม่สะอาด", "พบเส้นผมในอาหาร", "รอตรวจสอบ"],
        ["CP02", "S02", "2026-02-02", "รสชาติ", "เค็มเกินไป", "ดำเนินการแล้ว"],
        ["CP03", "S03", "2026-02-03", "บริการช้า", "รอนาน", "รอตรวจสอบ"],
    ]
)

# -----------------------------
# RESPONSES
# -----------------------------
write_csv(
    "data/responses.csv",
    ["complaint_id", "date", "message"],
    [
        ["CP02", "2026-02-03", "ปรับปรุงสูตรแล้ว"]
    ]
)

print("✅ สร้างฐานข้อมูล CSV เรียบร้อย")
