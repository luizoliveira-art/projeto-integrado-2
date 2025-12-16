class Doacao:
    def __init__(self, cod_doacao, data, doador_obj):
        self._cod_doacao = cod_doacao
        self._data = data
        self._doador = doador_obj
        self._livros_doados = []
        self._coordenador_avaliador = None

    @property
    def cod_doacao(self):
        return self._cod_doacao

    def atribuir_avaliador(self, coordenador_obj):
        self._coordenador_avaliador = coordenador_obj
        return f'Coordenador(a) {coordenador_obj.nome} atribuído(a) como avaliador(a) desta doação.'
    
    def registrar_livro_doado(self, livro_obj):
        
        if not self._coordenador_avaliador:
            return 'Erro: É necessário atribuir um Coordenador Avaliador primeiro.'

        estado = self._coordenador_avaliador.avaliar_livro(livro_obj)
        
        if estado.startswith('Erro:'):
            return estado

        self._livros_doados.append({
            'livro': livro_obj,
            'estado': estado,
            'disponivel_repasse': True if estado in ['Ótimo', 'Bom'] else False
        })
        
        self._doador.registrar_doacao(self.cod_doacao) 
        
        return f'Livro {livro_obj.titulo} registrado. Estado: {estado}.'

    def exibir_dados(self):
        avaliador = self._coordenador_avaliador.nome if self._coordenador_avaliador else 'NÃO ATRIBUÍDO'
        
        print(f'\n--- FICHA DA DOAÇÃO {self.cod_doacao} ({self._data}) ---')
        print(f'Doador: {self._doador.nome} (CPF: {self._doador.cpf_doador})')
        print(f'Avaliador Responsável: {avaliador}')
        print(f'Total de Itens Doados: {len(self._livros_doados)}')
        
        if self._livros_doados:
            print('\nITENS DOAÇÃO:')
            for item in self._livros_doados:
                livro = item['livro']
                repasse = 'SIM' if item['disponivel_repasse'] else 'NÃO'
                print(f'  [ISBN {livro.isbn}] {livro.titulo} - Estado: {item["estado"]} | Repasse: {repasse}')