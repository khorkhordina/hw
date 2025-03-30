import csv
import json
from pydantic import BaseModel
from itertools import cycle


class Book(BaseModel):
    title: str
    author: str
    pages: int
    genre: str


class User(BaseModel):
    name: str
    gender: str
    address: str
    age: int
    books: list[Book] = []


def load_books(file_path):
    with open(file_path, "r", newline='') as books_file:
        books_reader = csv.DictReader(books_file)
        books_list = [
            Book(
                title=row["Title"].strip(),
                author=row["Author"].strip(),
                pages=int(row["Pages"].strip()),
                genre=row["Genre"].strip()
            )
            for row in books_reader
        ]
    return books_list

def load_users(file_path):
    with open(file_path, "r") as json_file:
        users = json.load(json_file)
        users_list = [User(**user) for user in users]
        return users_list

def distribute_books(books, users):
    users_cycle = cycle(users)
    for book in books:
        next(users_cycle).books.append(book)


def save_results(users, file_path):
    with open(file_path, "w", encoding="utf-8") as results_file:
        json.dump(
            [user.model_dump() for user in users],
            results_file,
            indent=4
        )


def main():
    books_list = load_books("books.csv")
    users_list = load_users("user.json")
    distribute_books(books_list, users_list)
    save_results(users_list, "result.json")


if __name__ == "__main__":
    main()