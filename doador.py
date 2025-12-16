class Doador:
    def __init__(self, cpf_doador, nome, telefone):
        self._cpf_doador = cpf_doador
        self._telefone = telefone
        self._historico_doacoes = []

    @property
    def cpf_doador(self):
        return self._cpf_doador

    @property
    def nome(self):
        return self._nome.title()

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and len(novo_nome) > 3:
            self._nome = novo_nome
            print(f'Nome do doador alterado para: {self.nome}')
        else:
            print('Erro: o nome deve ser uma string válida com mais de 3 caracteres.')

    def exibir_historico(self):
        print(f'\n--- HISTÓRICO DE DOAÇÕES DE {self.nome} ---')
        if not self._historico_doacoes:
            print('Nenhuma doação registrada.')
            return
        
        for cod_doacao in self._historico_doacoes:
            print(f'- Código da Doação: {cod_doacao}')

    def registrar_doacao(self, cod_doacao):
        self._historico_doacoes.append(cod_doacao)
        print(f'Doação {cod_doacao} registrada no histórico de {self.nome}.')