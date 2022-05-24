import csv

with open('books.csv') as books_csv:
    books_reader = csv.DictReader(books_csv, delimiter='@')
    isbn_list = []
    for row in books_reader:
        isbn_list.append(row['ISBN'])