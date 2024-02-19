from peewee import *
db = SqliteDatabase('filmes.db')

class Filme(Model):
    nome=CharField(unique=True)
    nota=DecimalField(max_digits=2,decimal_places=1)
    class Meta:
        database =db
