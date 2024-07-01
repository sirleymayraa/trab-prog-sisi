from config import *

class Livro(db.Entity):
    nome = Required(str)
    editora = Required(str)
    autor = Required(str)
    genero = Required(str)
    classificacaoIndicativa = Required(str)
    anoDeEdicao = Required(str)
    def __str__(self):
        return f'{self.nome}, {self.editora}, {self.autor}, {self.genero}, {self.classificacaoIndicativa}, {self.anoDeEdicao}'

db.bind(provider='sqlite', filename='person.db', create_db=True)
db.generate_mapping(create_tables=True)