import tkinter as tk
from controllers.complaint_controller import ComplaintController
from views.complaint_list_view import ComplaintListView
from views.complaint_detail_view import ComplaintDetailView
from views.complaint_reply_view import ComplaintReplyView
from views.stall_summary_view import StallSummaryView

controller = ComplaintController()
root = tk.Tk()
root.title("ระบบร้องเรียนคุณภาพอาหาร")

current = None

def clear():
    global current
    if current:
        current.destroy()

def show_list():
    clear()
    global current
    current = ComplaintListView(root, controller, show_detail)
    current.pack()

def show_detail(cid):
    clear()
    global current
    c = controller.get_complaint(cid)
    current = ComplaintDetailView(root, c, show_reply, show_list)
    current.pack()

def show_reply(cid):
    clear()
    global current
    current = ComplaintReplyView(root, cid, submit_reply)
    current.pack()

def submit_reply(cid, msg):
    controller.reply(cid, msg.strip())
    show_detail(cid)

# แสดงหน้ารวม
show_list()

# ปุ่มสรุปร้านอาหาร
def show_stall_summary():
    clear()
    global current
    current = StallSummaryView(root, controller.stall_summary(), show_list)
    current.pack()

tk.Button(
    root,
    text="ดูสรุปร้านอาหาร",
    command=show_stall_summary
).pack()


root.mainloop()
