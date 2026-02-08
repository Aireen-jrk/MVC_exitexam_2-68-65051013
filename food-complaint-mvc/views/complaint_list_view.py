import tkinter as tk

class ComplaintListView(tk.Frame):
    def __init__(self, master, controller, show_detail):
        super().__init__(master)
        self.controller = controller
        self.show_detail = show_detail

        tk.Label(self, text="รายการร้องเรียนทั้งหมด", font=("Tahoma", 14)).pack()

        self.listbox = tk.Listbox(self, width=80)
        self.listbox.pack()

        for c in controller.get_complaints():
            self.listbox.insert(tk.END, f"{c['complaint_id']} | {c['type']} | {c['status']}")

        tk.Button(self, text="ดูรายละเอียด", command=self.open_detail).pack(pady=5)

    def open_detail(self):
        idx = self.listbox.curselection()
        if idx:
            cid = self.listbox.get(idx).split(" | ")[0]
            self.show_detail(cid)
