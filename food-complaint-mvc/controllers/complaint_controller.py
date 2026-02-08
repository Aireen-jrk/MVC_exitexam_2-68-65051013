from models.complaint_model import ComplaintModel
from models.response_model import ResponseModel
from models.stall_model import StallModel

class ComplaintController:
    def __init__(self):
        self.complaint_model = ComplaintModel()
        self.response_model = ResponseModel()
        self.stall_model = StallModel()

    def get_complaints(self):
        return self.complaint_model.get_all()

    def get_complaint(self, cid):
        return self.complaint_model.get_by_id(cid)

    def reply(self, cid, message):
        self.response_model.add(cid, message)
        self.complaint_model.update_status(cid, "ดำเนินการแล้ว")

    def stall_summary(self):
        return self.stall_model.summary()
