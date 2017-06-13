from peewee import *

db = SqliteDatabase('people.db')


class News(Model):
    date = DateField()
    title = CharField()
    news = TextField()
    number = IntegerField()

    class Meta:
        database = db  # This model uses the "people.db" database.
