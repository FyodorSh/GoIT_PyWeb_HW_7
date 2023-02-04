from faker import Faker
import random

from database.db import session
from database.models import Student, Group

fake = Faker('uk_UA')


def create_students():
    groups = session.query(Group).all()

    for _ in range(1, 50):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            group_id=random.choice(groups).id
        )
        session.add(student)
    session.commit()


if __name__ == "__main__":
    create_students()
