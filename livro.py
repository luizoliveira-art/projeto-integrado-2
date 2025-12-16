class Livro:
    def __init__(self, isbn, titulo, autor, materia, ano_escolar):
        self._isbn = isbn
        self._titulo = titulo
        self._autor = autor
        self._materia = materia
        self._ano_escolar = ano_escolar
        self._historico_repasse = []

    @property
    def isbn(self):
        return self._isbn

    @property
    def titulo(self):
        return self._titulo.title()

    @property
    def materia(self):
        return self._materia.title()

    @titulo.setter
    def titulo(self, novo_titulo):
        if isinstance(novo_titulo, str) and len(novo_titulo) > 0:
            self._titulo = novo_titulo
            print(f'Título do livro alterado para: {self.titulo}')
        else:
            print('Erro: Título inválido.')

    def exibir_dados(self):
        print(f'\n--- FICHA DO LIVRO: {self.titulo} ---')
        print(f'ISBN (PK): {self.isbn}')
        print(f'Autor: {self._autor.title()}')
        print(f'Matéria: {self.materia}')
        print(f'Ano Escolar: {self._ano_escolar}')
        
    def registrar_repasse(self, cod_repasse, turma_destino):
        self._historico_repasse.append((cod_repasse, turma_destino))
        print(f'Livro {self.titulo} registrado para repasse à turma {turma_destino}.')