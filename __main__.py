from csv import DictReader
from json import load, dump


class BookFieldNames:
    TITLE = "Title"
    AUTHOR = "Author"
    PAGES = "Pages"
    GENRE = "Genre"


class UserFieldNames:
    NAME = "name"
    GENDER = "gender"
    ADDRESS = "address"
    AGE = "age"
    BOOKS = "books"


if __name__ == '__main__':
    with open("books.csv", newline='') as csv_file:
        books = [{
            BookFieldNames.TITLE: el.get(BookFieldNames.TITLE),
            BookFieldNames.AUTHOR: el.get(BookFieldNames.AUTHOR),
            BookFieldNames.PAGES: el.get(BookFieldNames.PAGES),
            BookFieldNames.GENRE: el.get(BookFieldNames.GENRE)
        } for el in DictReader(csv_file)]
    with open("users.json") as json_file:
        users = [{
            UserFieldNames.NAME: el.get(UserFieldNames.NAME),
            UserFieldNames.GENDER: el.get(UserFieldNames.GENDER),
            UserFieldNames.ADDRESS: el.get(UserFieldNames.ADDRESS),
            UserFieldNames.AGE: el.get(UserFieldNames.AGE),
            UserFieldNames.BOOKS: []
        } for el in load(json_file)]
    users_amount = len(users)
    for i in range(0, users_amount):
        users[i][UserFieldNames.BOOKS] = books[i::users_amount]
    with open("result.json", 'w') as result_file:
        dump(users, result_file, indent=3)
