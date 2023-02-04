import sys

from database.db import session
from database.models import Teacher, Student, Grade, Subject, Group
from sqlalchemy import and_, func, desc

help_message = """
Виберіть який запит ви хочете виконати?
0 -- Вихід
1 -- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
2 -- Знайти студента із найвищим середнім балом з певного предмета.
3 -- Знайти середній бал у групах з певного предмета.
4 -- Знайти середній бал на потоці (по всій таблиці оцінок).
5 -- Знайти які курси читає певний викладач.
6 -- Знайти список студентів у певній групі.
7 -- Знайти оцінки студентів у окремій групі з певного предмета.
8 -- Знайти середній бал, який ставить певний викладач зі своїх предметів.
9 -- Знайти список курсів, які відвідує певний студент.
10 -- Список курсів, які певному студенту читає певний викладач.
"""


def max_5_avg_grade():
    students = session.query(Student.first_name, Student.last_name,
                             func.round(func.avg(Grade.grade), 2).label('avg_rate')).select_from(
        Grade).join(Student).filter(Grade.student_id == Student.id).group_by(Student.id).order_by(
        desc('avg_rate')).limit(5)

    for student in students:
        print(f'{student[1]} {student[0]} - {student[2]}')


def best_in_subject():
    students = session.query(Student.first_name, Student.last_name,
                             func.round(func.avg(Grade.grade), 2).label('avg_rate'), Subject.name).select_from(
        Grade).join(Student).join(Subject).filter(and_(Grade.student_id == Student.id, Grade.subject_id == 3)).\
        group_by(Student.id, Subject.id).order_by(desc('avg_rate')).limit(1)

    for student in students:
        print(f'{student[3]} * {student[1]} {student[0]} - {student[2]}')


def avg_grade_in_group_by_subject():
    grades = session.query(Group.name, Subject.name, func.round(func.avg(Grade.grade), 2).label('avg_rate')).\
        select_from(Grade).join(Subject).join(Student).join(Group).group_by(Subject.id, Group.id).\
        order_by(desc('avg_rate')).all()
    for grade in grades:
        print(f'{grade[0]} | {grade[1]} - {grade[2]}')


def avg_grade_from_all():
    grades = session.query(func.round(func.avg(Grade.grade), 2).label('avg_rate')).select_from(Grade).all()
    for grade in grades:
        print(f'Avg. grade (from all students) - {grade[0]}')


def teacher_subjects():
    subjects = session.query(Subject.name, Teacher.first_name, Teacher.last_name).select_from(Subject).join(Teacher).\
        filter(Teacher.id == 2).all()
    for subject in subjects:
        print(f'{subject[2]} {subject[1]} - {subject[0]}')


def students_in_group():
    students = session.query((Student.last_name + ' ' + Student.first_name), Group.name).select_from(Student).\
        join(Group).filter(Group.id == 1).all()
    for student in students:
        print(f'{student[0]} - {student[1]}')


def grades_in_group_by_subject():
    grades = session.query((Student.last_name + ' ' + Student.first_name), Group.name, Grade.grade, Subject.name).\
        select_from(Grade).join(Student).join(Group).join(Subject).filter(and_(Group.id == 3, Subject.id == 4)).all()
    for grade in grades:
        print(f'{grade[0]} - {grade[1]} - {grade[3]} - {grade[2]}')


def teacher_avg_grade_by_subject():
    grades = session.query(Teacher.last_name + ' ' + Teacher.first_name, func.round(func.avg(Grade.grade), 2).
                           label('avg_rate'), Subject.name).select_from(Grade).join(Subject).join(Teacher).\
        filter(Teacher.id == 5).group_by(Teacher.id, Subject.id).order_by(desc('avg_rate')).all()
    for grade in grades:
        print(f'{grade[0]} - {grade[2]} - {grade[1]}')


def student_subjects():
    subjects = session.query((Student.last_name + ' ' + Student.first_name), Subject.name).select_from(Grade).\
        join(Student).join(Subject).filter(Student.id == 11).group_by(Student.id, Subject.id).all()

    for subject in subjects:
        print(f'{subject[0]} - {subject[1]}')


def student_teacher_subjects():
    subjects = session.query((Student.last_name + ' ' + Student.first_name),
                             Teacher.last_name + ' ' + Teacher.first_name, Subject.name).select_from(Grade).\
        join(Student).join(Subject).join(Teacher).filter(and_(Student.id == 11, Teacher.id == 5)).\
        group_by(Student.id, Teacher.id, Subject.id).all()

    for subject in subjects:
        print(f'{subject[0]} - {subject[1]} - {subject[2]}')


def get_data():
    queries = {
        1: max_5_avg_grade,
        2: best_in_subject,
        3: avg_grade_in_group_by_subject,
        4: avg_grade_from_all,
        5: teacher_subjects,
        6: students_in_group,
        7: grades_in_group_by_subject,
        8: teacher_avg_grade_by_subject,
        9: student_subjects,
        10: student_teacher_subjects,
    }

    print(help_message)
    while True:
        task = int(input("Виберіть номер запиту: "))
        if task == 0:
            sys.exit()

        try:
            queries[task]()
        except KeyError as e:
            print('Запит не знайдений: ', e)


if __name__ == "__main__":
    get_data()
