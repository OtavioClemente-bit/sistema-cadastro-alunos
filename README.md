# Sistema de Cadastro de Alunos

Projeto simples em Python, com interface no terminal, voltado para o cadastro de alunos e gerenciamento de notas. Os dados são armazenados localmente em um arquivo JSON.

## Funcionalidades

- Cadastro de novos alunos
- Registro de múltiplas notas por aluno
- Cálculo automático da média
- Verificação de aprovação (>=6) ou recuperação
- Armazenamento dos dados em arquivo `.json`

## Tecnologias usadas

- Python 3.x
- Módulo `json` (persistência dos dados)
- Módulo `os` e `time` (controle de tela e pausa)

## Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/OtavioClemente-bit/cadastro_alunos.git
   cd cadastro_alunos

    Execute o código:

    python main.py

    ⚠️ Requer Python 3 instalado no sistema.

Estrutura dos arquivos

cadastro_alunos/
│
├── main.py         # Código principal do sistema
├── alunos.json     # Dados salvos dos alunos e notas
└── README.md       # Documentação

Autor

Desenvolvido por Otavio Clemente,
em processo de transição de carreira para desenvolvedor backend com Python.
