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
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка домашние задания: {self.count_avarage():.2f}' \
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

cool_lecturer = Lecturer('Harry', 'Smith')
cool_lecturer.courses_attached += ['JS']
best_student.rate(cool_lecturer, 'JS', 10)
best_student.rate(cool_lecturer, 'JS', 5)
best_student.rate(cool_lecturer, 'JS', 10)

print(cool_reviewer)
print()
print(cool_lecturer)
print()
print(best_student)
print()
print(other_student)
print()
print(best_student.__lt__(other_student))
