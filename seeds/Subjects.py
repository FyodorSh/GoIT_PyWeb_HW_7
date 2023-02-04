from faker import Faker
import random

from database.db import session
from database.models import Subject, Teacher

fake = Faker('uk_UA')


def create_subjects():
    teachers = session.query(Teacher).all()
    for _ in range(1, 15):
        subject = Subject(
            name=fake.job(),
            teacher_id=random.choice(teachers).id
        )
        session.add(subject)
    session.commit()


if __name__ == "__main__":
    create_subjects()
