import tkinter as tk

class ComplaintDetailView(tk.Frame):
    def __init__(self, master, complaint, reply_callback, back_callback):
        super().__init__(master)

        tk.Label(self, text="รายละเอียดการร้องเรียน", font=("Tahoma", 14)).pack()

        for k, v in complaint.items():
            tk.Label(self, text=f"{k}: {v}").pack(anchor="w")

        tk.Button(self, text="ตอบกลับ", command=lambda: reply_callback(complaint["complaint_id"])).pack()
        tk.Button(self, text="← กลับ", command=back_callback).pack(pady=5)
