from faker import Faker

fake = Faker()

class Creds:
    ADMIN_LOGIN = "user"
    ADMIN_PASSWORD = "bitnami"


def generate_product_data():

    return {
        "name": fake.unique.word() + " " + fake.unique.word(),
        "meta_title": fake.sentence(nb_words=3),
        "model": fake.unique.bothify(text='??-###'),
        "price": str(fake.random_int(min=10, max=1000)),
        "quantity": str(fake.random_int(min=1, max=100))
    }


def generate_user_data():

    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "email": fake.unique.email(),
        "password": fake.password(length=10)
    }