class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def count_avarage(self):
        count = []
        for grade in self.grades.values():
            for item in grade:
                count += [item]
        return sum(count) / len(count)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.count_avarage():.2f}' \
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.count_avarage() < other.count_avarage()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def count_avarage(self):
        count = []
        for grade in self.grades.values():
            for item in grade:
                count += [item]
        return sum(count) / len(count)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.count_avarage():.2f}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.count_avarage() < other.count_avarage()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def get_avarage_student(students, course):
    count = []
    for student in students:
        for grade in student.grades[course]:
            count += [grade]
    return sum(count) / len(count)


def get_avarage_lecturer(lecturers, course):
    count = []
    for lecturer in lecturers:
        for grade in lecturer.grades[course]:
            count += [grade]
    return sum(count) / len(count)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'JS']
best_student.finished_courses += ['Git']

other_student = Student('John', 'Other', 'male')
other_student.courses_in_progress += ['Python', 'JS']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'JS']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'JS', 10)

cool_reviewer.rate_hw(other_student, 'Python', 10)

another_reviewer = Reviewer('Mark', 'Black')
another_reviewer.courses_attached += ['Git', 'JS']

cool_lecturer = Lecturer('Harry', 'Smith')
cool_lecturer.courses_attached += ['JS']

another_lecturer = Lecturer('Bobby', 'Brown')
another_lecturer.courses_attached += ['Git', 'JS']

best_student.rate(cool_lecturer, 'JS', 10)
other_student.rate(cool_lecturer, 'JS', 5)
best_student.rate(another_lecturer, 'JS', 9)
other_student.rate(another_lecturer, 'JS', 8)

student_list = [best_student, other_student]
lecturer_list = [cool_lecturer, another_lecturer]

print(get_avarage_student(student_list, 'Python'))
print(get_avarage_student(lecturer_list, 'JS'))
