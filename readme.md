# Blog API Django

## Sobre:

Projeto está sendo desenvolvido com o intuito de aprender python no ecossistema django

## Para desenvolver:

    Começaremos iniciando um ambiente virtual para rodar nossa aplicação:
    
    $ pip install virtualenv
    $ python -m venv venv


Caso você esteja no Windows talvez seja interessante rodar esse comando
antes de tentar seguir os próximos passos:
    
    $ Set-ExecutionPolicy Unrestricted -Scope Process

Vale notar que esse comando deve ser rodado toda vez após um novo
processo de terminal ser executado
    Caso deseje deixar habilitado a execução de scripts direto utilize:

    $ Set-ExecutionPolicy Unrestricted -Force

Para mais informações sobre os comandos: [leia aqui.](https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows/18713789)

Também é recomendado que tenha o django instalado

E no Windows então execute 

    $ ./venv/Script/activate

Caso esteja no linux execute

    $ source ./venv/Script/activate

E depois

    $ pip install django
    $ pip install django-rest_framework
    $ python -m pip install django-cors-headers


Se ao executar esse comando aparecer "venv" nas linhas do seu terminal, tudo ocorreu corretamente!

Para rodar o projeto:

    $ cd siteBlog
    $ python ./manage.py runserver

Login admin:
    
    user : matheus
    password: 123