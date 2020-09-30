# Marvel Collection Django

## Uma aplicação simples para estudo.
Aplicação para estudo das funcionalidades do Django, usando a **API da Oficial Marvel**.


* O usuário é autenticado, através do *engine* de auth interno do Django.
* No Dashboard é exibido todos os itens da coleção de personagens da Marvel que o usuário possui.
* Ao pesquisar por nome do personagem, a aplicação consome a **API da Oficial Marvel**.
* Ao adicionar um personagem a aplicação faz o *parse* da API da Marvel, e guarda as informações do personagem relacionando com a conta do usuário.
* O usuário pode selecionar um *personagem favorito*, que terá sua imagem na cover do Dashboard.
* O usuário pode também remover personagens de sua coleção.

## Deploy de Teste:

A última versão da aplicação pode ser encontrada em:
https://marvel-django.herokuapp.com/marvel/

* Usuario de teste: guest
* Senha: django1234

## Marvel API

Mais informações sobre a Marvel API:
[https://developer.marvel.com/]
