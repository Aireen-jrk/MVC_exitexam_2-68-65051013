import tkinter as tk

class StallSummaryView(tk.Frame):
    def __init__(self, master, data, back_callback):
        super().__init__(master)

        tk.Label(self, text="ร้านอาหารและจำนวนร้องเรียน", font=("Tahoma", 14)).pack()

        for name, count in data:
            tk.Label(self, text=f"{name} : {count} รายการ").pack(anchor="w")

        # ✅ ปุ่มย้อนกลับ
        tk.Button(self, text="← กลับ", command=back_callback).pack(pady=10)
