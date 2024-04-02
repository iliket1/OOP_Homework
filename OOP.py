class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}

  def rate_lecturer(self, lecturer, course, grade):
      if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
          if course in lecturer.grades:
              lecturer.grades[course] += [grade]
          else:
              lecturer.grades[course] = [grade]
      else:
          return 'Ошибка'

  def av_grade(self):
      sum_grade = 0
      count = 0
      for i in self.grades.values():
          for j in i:
              sum_grade += j
              count += 1
      return round(sum_grade / count, 2)

  def __str__(self):
      return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

  def __lt__(self, other):
      if not isinstance(other, Student):
          print('Нет студента')
          return
      return self.av_grade() < other.av_grade()

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

  def average_grade(self):
    if not self.grades:
      return 0
    grades_list = []
    for k in self.grades.values():
      grades_list.extend(k)
    return round(sum(grades_list) / len(grades_list), 2)

  def __str__(self):
    return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'

  def __lt__(self, other):
    if not isinstance(other, Lecturer):
      print('Нет лектора')
      return
    return self.average_grade() < other.average_grade()

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
      return f'Имя: {self.name}\nФамилия: {self.surname}'

best_student = Student('Иван', 'Иванов', 'м')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']
best_student.grades['Git'] = [10, 9, 10, 10, 9]
best_student.grades['Python'] = [10, 9, 9]
new_student = Student('Петр', 'Петров', 'м')
new_student.courses_in_progress += ['Python', 'Git']
new_student.grades['Git'] = [10, 9, 8]
new_student.grades['Python'] = [7, 9]

cool_reviewer = Reviewer('Олег', 'Булыгин')
cool_reviewer.courses_attached += ['Python']
some_reviewer = Reviewer('Сергей', 'Сергеев')
some_reviewer.courses_attached += ['Git']

cool_lecturer = Lecturer('Федор', 'Федоров')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.grades['Python'] = [10, 10, 10, 10, 10]
some_lecturer = Lecturer('Александр', 'Александров')
some_lecturer.courses_attached += ['Git']
some_lecturer.grades['Git'] = [9, 10, 8, 10, 9]

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(new_student, 'Git', 10)

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(some_lecturer, 'Python', 10)

print(best_student.grades,'\n', new_student.grades)
print(best_student,'\n', new_student)
print()
print(cool_lecturer.grades,'\n', some_lecturer.grades)
print(cool_lecturer,'\n', some_lecturer)
print()
print(cool_lecturer > some_lecturer)
print(best_student > new_student)

def student_av_grade(students, course):
  if not isinstance(students, list):
    return "Not list"
  grades_list = []
  for student in students:
    grades_list.extend(student.grades.get(course, []))
  if not grades_list:
    return "По такому курсу ни у кого нет оценок"
  return round(sum(grades_list) / len(grades_list), 2)

def lecturer_av_grade(lecturers, course):
  if not isinstance(lecturers, list):
    return "Not list"
  grades_list = []
  for lecturer in lecturers:
    grades_list.extend(lecturer.grades.get(course, []))
  if not grades_list:
    return "По такому курсу ни у кого нет оценок"
  return round(sum(grades_list) / len(grades_list), 2)

students = [best_student, new_student]
lecturers = [cool_lecturer, some_lecturer]
print(student_av_grade(students, 'Python'))
print(student_av_grade(students, 'Git'))
print(lecturer_av_grade(lecturers, 'Python'))
print(lecturer_av_grade(lecturers, 'Git'))