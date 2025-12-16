class Coordenacao:
    def __init__(self, matricula_coord, cpf, nome, setor):
        self._matricula_coord = matricula_coord
        self._cpf = cpf
        self._nome = nome
        self._setor = setor

    @property
    def matricula_coord(self):
        return self._matricula_coord

    @property
    def nome(self):
        return self._nome.title()
    
    def exibir_dados(self):
        print(f'\n--- FICHA DO COORDENADOR(A): {self.nome} ---')
        print(f'Matrícula (PK): {self.matricula_coord}')
        print(f'Setor: {self._setor.title()}')

    def avaliar_livro(self, livro_obj):
        estado = input(f'Avalie o estado de conservação do livro "{livro_obj.titulo}" (Ótimo, Bom, Regular, Ruim): ').strip().title()
        
        if estado not in ['Ótimo', 'Bom', 'Regular', 'Ruim']:
            return f'Erro: Estado "{estado}" inválido. Avaliação cancelada.'
        
        print(f'-> Avaliação concluída por {self.nome}. Resultado: {estado}.')
        return estado