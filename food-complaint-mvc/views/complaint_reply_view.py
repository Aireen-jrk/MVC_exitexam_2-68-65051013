import tkinter as tk

class ComplaintReplyView(tk.Frame):
    def __init__(self, master, cid, submit):
        super().__init__(master)
        tk.Label(self, text=f"ตอบกลับการร้องเรียน {cid}", font=("Tahoma", 14)).pack()

        self.text = tk.Text(self, height=4, width=50)
        self.text.pack()

        tk.Button(self, text="บันทึก", command=lambda: submit(cid, self.text.get("1.0", tk.END))).pack(pady=5)
