from Processor.Processor import Processor
from student.Student import Student

# manu
classlist = []

processor = Processor(classlist)

student1 = Student("Judith", 1111, 89)
student2 = Student("Tresor", 2222, 90)
student3 = Student("Tecla", 3333,78)

processor.add_student(student1)
processor.add_student(student2)
processor.add_student(student3)

def my_menu():
    menu= input("1 : Add student" + "\n" + "2 : Search student" + "\n" + "3 : Set student marks" + "\n" + "4 : Remove student" + "\n" + "5 : Get classlist" + "\n" + "6 close system: " + "\n")
    return int(menu)


menu= my_menu()

while menu != 6:
    if menu == 1:
        name = input("enter name: ")
        studNum = int(input("enter student number: "))
        marks = int(input("enter marks: "))

        my_student = Student(name, studNum, marks)
        msg = processor.add_student(my_student)
        print(msg)

    elif menu == 2:
        studNum = int(input("enter student number: "))
        index = processor.search(studNum)
        if index > -1:
            data = "NAME: {} " + "\n" + " STUDENT NUM: {}" + "\n" + " MARKS:  {}"
            print(data.format(classlist[index].name, classlist[index].studentNum, classlist[index].marks))

        else:
            data = "STUDENT NOT FOUND"
            print(data)



    elif menu == 3:
        studNum = int(input("enter student number: "))
        marks = int(input("enter marks: "))
        print(processor.change_marks(studNum, marks))

    elif menu == 4:
        studNum = input("enter student number: ")

        print(processor.remove(studNum))

    elif menu == 5:
        for s in classlist:
            print("{} : {}".format(s.name, s.studentNum))
    menu = my_menu()

print("GOOD BEY")
    # choice =input("1 use program"+"\n"+"2 close system: "+"\n")


