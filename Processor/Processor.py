from student.Student import Student


class Processor:

    def __init__(self, students=[]):
        self.students = students

    def add_student(self, student):
        self.students.append(student)
        return "student successfully added"


    def remove(self,num):
        index= self.search(num);
        if index >-1:
            self.students.pop(index)
            msg = "STUDENT REMOVED"
        else:
            msg = "STUDENT NOT FOUND"
        return msg

    def search(self ,num):
        for s in self.students:
            if s.studentNum == num:
                index= self.students.index(s);
                break
            else:
                index =-1

        return index

    def change_marks(self,num, newMarks):
        index = self.search(num);
        if index > -1:
            self.students[index].marks= newMarks
            msg = "NEW MARKS UPDATED"
        else:
            msg = "STUDENT NOT FOUND"
        return msg



