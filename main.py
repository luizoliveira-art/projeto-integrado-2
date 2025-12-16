from plataforma import Plataforma
from doador import Doador
from livro import Livro
from coordenacao import Coordenacao
from doacao import Doacao

plataforma_principal = Plataforma(cod_plataforma='P_DOA01', nome='Plataforma Mãos que transformam')

def buscar_objeto(lista, pk_valor, pk_atributo):
    for obj in lista:
        if getattr(obj, pk_atributo) == pk_valor:
            return obj
    return None

def buscar_doador(cpf_doador):
    return buscar_objeto(plataforma_principal._lista_doadores, cpf_doador, 'cpf_doador')

def buscar_livro(isbn):
    return buscar_objeto(plataforma_principal._lista_livros, isbn, 'isbn')

def buscar_coordenador(matricula):
    return buscar_objeto(plataforma_principal._lista_coordenadores, matricula, 'matricula_coord')

def buscar_doacao(cod_doacao):
    return buscar_objeto(plataforma_principal._lista_doacoes, cod_doacao, 'cod_doacao')


def cadastrar_doador():
    print('\n--- CADASTRO DE NOVO DOADOR ---')
    try:
        cpf_doador = input('CPF do Doador (PK): ')
        nome = input('Nome Completo: ')
        telefone = input('Telefone: ')

        novo_doador = Doador(cpf_doador=cpf_doador, nome=nome, telefone=telefone)
        
        resultado = plataforma_principal.adicionar_doador(novo_doador)
        print(f'\n[STATUS]: {resultado}')
        
    except Exception as e:
        print(f'\n[ERRO] Ocorreu um erro no cadastro: {e}')

def cadastrar_livro():
    print('\n--- CADASTRO DE NOVO LIVRO ---')
    try:
        isbn = input('ISBN do Livro (PK): ')
        titulo = input('Título: ')
        autor = input('Autor: ')
        materia = input('Matéria: ')
        ano_escolar = input('Ano Escolar (Ex: 6o Ano): ')

        novo_livro = Livro(isbn=isbn, titulo=titulo, autor=autor, materia=materia, ano_escolar=ano_escolar)
        
        resultado = plataforma_principal.adicionar_livro(novo_livro)
        print(f'\n[STATUS]: {resultado}')
        
    except Exception as e:
        print(f'\n[ERRO] Ocorreu um erro no cadastro: {e}')

def cadastrar_coordenador():
    print('\n--- CADASTRO DE NOVO COORDENADOR ---')
    try:
        matricula_coord = input('Matrícula do Coordenador (PK): ')
        cpf = input('CPF: ')
        nome = input('Nome Completo: ')
        setor = input('Setor (Ex: Fundamental I): ')

        novo_coord = Coordenacao(matricula_coord=matricula_coord, cpf=cpf, nome=nome, setor=setor)
        
        resultado = plataforma_principal.adicionar_coordenador(novo_coord)
        print(f'\n[STATUS]: {resultado}')
        
    except Exception as e:
        print(f'\n[ERRO] Ocorreu um erro no cadastro: {e}')


def registrar_doacao_integrada():
    print('\n--- REGISTRAR NOVA DOAÇÃO E AVALIAÇÃO ---')
    
    cpf_doador = input('CPF do Doador: ')
    doador = buscar_doador(cpf_doador)
    
    if not doador:
        print('Erro: Doador não encontrado. Cadastro de doação cancelado.')
        return

    matricula_coord = input('Matrícula do Coordenador Avaliador: ')
    coordenador = buscar_coordenador(matricula_coord)

    if not coordenador:
        print('Erro: Coordenador Avaliador não encontrado. Cadastro de doação cancelado.')
        return

    cod_doacao = input('Código da Doação (PK): ')
    data = input('Data da Doação (Ex: 15/12/2025): ')
    
    nova_doacao = Doacao(cod_doacao=cod_doacao, data=data, doador_obj=doador)
    
    resultado_agregacao = plataforma_principal.adicionar_doacao(nova_doacao)
    if resultado_agregacao.startswith('Erro:'):
        print(resultado_agregacao)
        return

    print(nova_doacao.atribuir_avaliador(coordenador))

    print('\n--- ADICIONANDO LIVROS ---')
    while True:
        isbn_livro = input('ISBN do Livro a ser doado (ou "FIM" para encerrar): ').upper()
        if isbn_livro == 'FIM':
            break

        livro = buscar_livro(isbn_livro)
        
        if livro:
            resultado = nova_doacao.registrar_livro_doado(livro)
            print(f'[REGISTRO]: {resultado}')
        else:
            print(f'Erro: Livro com ISBN {isbn_livro} não encontrado no catálogo. Cadastre-o primeiro.')

    print(f'\n[STATUS FINAL]: Doação {cod_doacao} registrada com sucesso.')
    nova_doacao.exibir_dados()


def exibir_historico_doacao():
    print('\n--- HISTÓRICO DE DOAÇÃO ---')
    cod_doacao = input('Digite o Código da Doação que deseja visualizar: ')
    doacao = buscar_doacao(cod_doacao)
    
    if doacao:
        doacao.exibir_dados()
    else:
        print(f'Erro: Doação com código {cod_doacao} não encontrada.')


def exibir_menu():
    print('\n' + '='*50)
    print(f'SISTEMA DE DOAÇÕES DE LIVROS (EP1) - {plataforma_principal.nome}')
    print('='*50)
    print('1 - Exibir Dados da Plataforma (Visão Geral)')
    print('2 - Cadastrar Doador')
    print('3 - Cadastrar Livro no Catálogo')
    print('4 - Cadastrar Coordenador')
    print('5 - REGISTRAR NOVA DOAÇÃO (Integração)')
    print('6 - Exibir Histórico de Doação')
    print('0 - Sair do Sistema')
    print('='*50)

if __name__ == '__main__':
    
    while True:
        exibir_menu()
        
        op = input('Escolha uma opção: ')

        if op == '1':
            plataforma_principal.exibir_dados()
        
        elif op == '2':
            cadastrar_doador()
        
        elif op == '3':
            cadastrar_livro()
        
        elif op == '4':
            cadastrar_coordenador()
            
        elif op == '5':
            registrar_doacao_integrada()
            
        elif op == '6':
            exibir_historico_doacao()
        
        elif op == '0':
            print('Saindo do sistema. Até mais!')
            break
        
        else:
            print('Opção inválida. Tente novamente.')