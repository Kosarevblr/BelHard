# 1. Написать класс Student
# Конструктор класса принимает аргументы: first_name: str, group: int, marks: list[int]
# Написать метод __str__ возвращающая форматированную строку с данными об студенте
# Написать функцию (не метод) student_sort принимающая список студентов: students:
# list[Student] и возвращающая список студентов отсортированный по имени

first_name = 'John'
group = 999
marks = [2, 3, 4]
students = ['sdasd', 'asdffff', 'trog', 'bdfgd']


class Student:

    def __init__(self, first_name: str, group: int, marks: list[int]) -> None:
        self.first_name = first_name
        self.group = group
        self.marks = marks

    def __str__(self) -> str:
        return f'Студент {self.first_name} из группы {self.group}, оценки - {self.marks}'

    @staticmethod
    def student_sort(students: list[str]) -> list:
        return sorted(students, key=lambda student: student.first_name)


a = Student(first_name, group, marks)

print(a)
print(Student.student_sort(students))
