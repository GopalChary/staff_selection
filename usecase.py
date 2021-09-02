
class Applicant:
    def __init__(self,app_result):
        self.name=app_result[0]
        self.subject1=app_result[1]
        self.subject2=app_result[2]
        self.subject3=app_result[3]
        self.total=app_result[4]
        self.percentage=app_result[5]

    def __repr__(self):
        pass

    def set_name(self):
        self.name=name
    def get_subject1(self):
        return self.name
    def set_subject1(self):
        self.subject1=subject1
    def get_subject1(self):
        return self.subject1
    def set_subject2(self):
        self.subject2=subject2
    def get_subject2(self):
        return self.subject2
    def set_subject3(self):
        self.subject3=subject3
    def get_subject3(self):
        return self.subject3
    def set_total(self):
        self.total=total
    def get_total(self):
        return self.total
    def set_percentage(self):
        self.percentage=percentage
    def get_percentage(self):
        return self.percentage
