class Plataforma:
    def __init__(self, cod_plataforma, nome):
        self._cod_plataforma = cod_plataforma
        self._nome = nome
        self._lista_doadores = []  
        self._lista_livros = []    
        self._lista_doacoes = []   
        self._lista_coordenadores = []

    @property
    def nome(self):
        return self._nome.upper()

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and len(novo_nome) > 0:
            self._nome = novo_nome
            print(f'Nome da Plataforma alterado para: {self.nome}')
        else:
            print('Erro: Nome da Plataforma inválido.')

    def adicionar_doador(self, doador_obj):
        cpfs_atuais = [d.cpf_doador for d in self._lista_doadores]
        
        if doador_obj.cpf_doador not in cpfs_atuais:
            self._lista_doadores.append(doador_obj)
            return f'Doador(a) {doador_obj.nome} cadastrado(a) na {self.nome}.'
        else:
            return f'Erro: Doador(a) com CPF {doador_obj.cpf_doador} já está cadastrado(a).'

    def adicionar_livro(self, livro_obj):
        isbns_atuais = [li.isbn for li in self._lista_livros]

        if livro_obj.isbn not in isbns_atuais:
            self._lista_livros.append(livro_obj)
            return f'Livro {livro_obj.titulo} adicionado ao catálogo da {self.nome}.'
        else:
            return f'Erro: Livro com ISBN {livro_obj.isbn} já existe no catálogo.'

    def adicionar_coordenador(self, coordenador_obj):
        matriculas_atuais = [c.matricula_coord for c in self._lista_coordenadores]
        
        if coordenador_obj.matricula_coord not in matriculas_atuais:
            self._lista_coordenadores.append(coordenador_obj)
            return f'Coordenador(a) {coordenador_obj.nome} cadastrado(a) na {self.nome}.'
        else:
            return f'Erro: Coordenador(a) com matrícula {coordenador_obj.matricula_coord} já está cadastrado(a).'

    def adicionar_doacao(self, doacao_obj):
        cods_doacao_atuais = [d.cod_doacao for d in self._lista_doacoes]
        
        if doacao_obj.cod_doacao not in cods_doacao_atuais:
            self._lista_doacoes.append(doacao_obj)
            return f'Doação {doacao_obj.cod_doacao} registrada na {self.nome}.'
        else:
            return f'Erro: Doação com código {doacao_obj.cod_doacao} já existe.'

    def exibir_dados(self):
        print(f'\n----- DADOS DA PLATAFORMA {self.nome} ------')
        print(f'Código: {self._cod_plataforma}')
        print(f'Total de Doadores: {len(self._lista_doadores)}')
        print(f'Total de Livros no Catálogo: {len(self._lista_livros)}')
        print(f'Total de Doações Registradas: {len(self._lista_doacoes)}')
        print(f'Total de Coordenadores Cadastrados: {len(self._lista_coordenadores)}')