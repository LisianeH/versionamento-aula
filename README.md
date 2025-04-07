# Engenharia de Software 2 - Controle de Versão com Git e GitHub

Este repositório faz parte das atividades da disciplina **Engenharia de Software 2** e tem como foco o estudo e a aplicação de **sistemas de controle de versão**, com ênfase na utilização do **Git** e da plataforma **GitHub**.

## 📚 Conteúdo Abordado

Durante esta etapa da disciplina, estudamos:

- Conceito de **Controle de Versão**
- Vantagens do uso de sistemas de versionamento
- Introdução ao **Git**:
  - Inicialização de repositórios (`git init`)
  - Adição de arquivos (`git add`)
  - Registro de alterações (`git commit`)
  - Visualização do histórico (`git log`)
- Conceitos de **branches**, **merge** e resolução de conflitos
- Introdução ao **GitHub**:
  - Criação e clonagem de repositórios remotos
  - Push e Pull (`git push`, `git pull`)
  - Colaboração em projetos e pull requests
- Integração com o GitHub no Visual Studio Code

## 🎯 Objetivo

Capacitar os estudantes a:

- Compreender o funcionamento de sistemas de controle de versão distribuídos
- Trabalhar com repositórios locais e remotos
- Colaborar em equipe utilizando boas práticas de versionamento
- Preparar o ambiente de desenvolvimento para projetos reais

## 🔧 Comandos Básicos

Quando criamos uma pasta diretamente no local, utilizamos os seguintes comandos:

```bash
cd nome-da-pasta
git init
git add .
git commit -m "mensagem"
git remote add origin https://github.com/seu-usuario/seu-repositorio.git
git push origin main
