# -*- coding: utf-8 -*-
"""
Sistema simples de cadastro de alunos, registro de notas e verificação de aprovação.
Feito para treinar dicionários, listas, funções e manipulação de arquivos JSON.
"""

import json
import os
import time
from typing import Dict, Any

alunos: Dict[str, Dict[str, Any]] = {}


def limpar_tela() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def salvar_alunos() -> None:
    with open('alunos.json', 'w', encoding='utf-8') as f:
        json.dump(alunos, f, ensure_ascii=False, indent=4)


def carregar_alunos() -> None:
    global alunos
    try:
        with open('alunos.json', 'r', encoding='utf-8') as f:
            alunos = json.load(f)
    except FileNotFoundError:
        alunos = {}


carregar_alunos()


def cadastrar_aluno() -> str | None:
    while True:
        limpar_tela()
        nome = input("Digite o nome do aluno (ou 'sair' para voltar): ").strip()
        if nome.lower() == 'sair':
            return None
        if nome.isalpha():
            if nome not in alunos:
                alunos[nome] = {}
                salvar_alunos()
            return nome
        print('\nNome inválido! Use apenas letras.')
        time.sleep(1)


def cadastrar_notas(nome: str) -> None:
    while True:
        limpar_tela()
        try:
            qtd = int(input('Quantas provas? '))
            if qtd <= 0:
                raise ValueError
            break
        except ValueError:
            print('\nDigite um número inteiro positivo.')
            time.sleep(1)

    for i in range(1, qtd + 1):
        while True:
            limpar_tela()
            try:
                nota = float(input(f'Digite a nota da {i}ª prova (0-10): '))
                if 0 <= nota <= 10:
                    alunos[nome][f'nota_{i}'] = nota
                    salvar_alunos()
                    break
                raise ValueError
            except ValueError:
                print('\nValor inválido. Digite entre 0 e 10.')
                time.sleep(1)
    print('\nNotas cadastradas com sucesso!')
    time.sleep(1)


def calcular_media(nome: str) -> float:
    notas = alunos[nome].values()
    return sum(notas) / len(notas) if notas else 0.0


def verificar_aprovacao(nome: str) -> None:
    media = calcular_media(nome)
    limpar_tela()
    if not alunos[nome]:
        print(f'O aluno {nome} ainda não possui notas.')
    elif media >= 6:
        print(f'O aluno {nome} foi \033[32mAPROVADO\033[0m com média {media:.2f}.')
    else:
        print(f'O aluno {nome} está em \033[33mRECUPERAÇÃO\033[0m com média {media:.2f}.')
    input('\nPressione ENTER para continuar.')


def selecionar_aluno() -> str | None:
    while True:
        limpar_tela()
        nome = input("Digite o nome do aluno (ou 'sair'): ").strip()
        if nome.lower() == 'sair':
            return None
        if nome in alunos:
            return nome
        print('\nAluno não encontrado.')
        time.sleep(1)


def menu():
    while True:
        limpar_tela()
        print('╔════════ MENU PRINCIPAL ════════╗')
        print('║ 1 - Verificar aprovação        ║')
        print('║ 2 - Cadastrar aluno            ║')
        print('║ 3 - Sair                       ║')
        print('╚════════════════════════════════╝')
        try:
            opcao = int(input('Escolha: '))
        except ValueError:
            continue

        if opcao == 1:
            aluno = selecionar_aluno()
            if aluno:
                verificar_aprovacao(aluno)
        elif opcao == 2:
            aluno = cadastrar_aluno()
            if aluno:
                cadastrar_notas(aluno)
        elif opcao == 3:
            limpar_tela()
            print('Obrigado por usar o sistema!')
            break


if __name__ == '__main__':
    menu()
