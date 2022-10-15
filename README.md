# Web application with Django.
*** Página Inicial do Aplicativo ***

![aplicativoWeb_Django](https://user-images.githubusercontent.com/109990443/196002716-c1aaba62-2867-40b4-83a6-a2e149cc0e27.png)

#### DESCRIÇÃO: <br>
Para a criação do projeto e para execução será necessário: Primeiramente instalar Python (Versão utilizada 3.9). <br>
Instalar : Framework Django e Pillow. <br>
Para isso em Shell: <br>
* pip install django.
* pip install pillow. <br>

#### CRIANDO O PROJETO NO DIRETÓRIO: 
###### OBS: VOCÊ DEVERÁ APONTAR PARA O SHELL O CAMINHO DO DIRETÓRIO AO QUAL DESEJA SALVAR O SEU PROJETO. <br> CASO ESTEJA UTILIZANDO VERSIONAMENTO GIT DEVERÁ CRIAR PRIMEIRO A PASTA E INSERIR O ENDEREÇO NO SHELL.
![diretorio](https://user-images.githubusercontent.com/109990443/196004415-898a0db5-aecd-4ea7-b0e7-f30038ccf3bf.png)
Em Shell:
* django-admin startproject projectname - (Para criar o projeto)
* Python manage.py startapp nameapp - (Para criar o aplicativo) <br>

#### CRIANDO USUÁRIO PARA O PROJETO:
###### OBS: DJANGO POR PADRÃO JÁ VEM CONFIGURADO COM O BANCO DE DADOS SqlLite, ENTÃO DEVERÁ APENAS CRIAR UM USUÁRIO NO SHELL.
* python manage.py createsuperuser - (Para criar usuário)<br>
![dados do usuario](https://user-images.githubusercontent.com/109990443/196005530-a0bd4529-8300-432c-8892-c96e9b1db2bc.png)

#### MIGRANDO O SCRIP DIPONIVÉL ACIMA PARA O BANCO DE DADOS:
* python manage.py makemigrations nomeapp - (Para migrar o scrip de código)<br>

###### APÓS CRIAR USUÁRIO E MIGRAR O SCRIPT ESTABELEÇA CONEXÃO COM O BANCO DE DADOS:
* Python manage.py runserver - Para iniciar seu servidor use: localhost - para Django será localhost:8000)<br>
![localholst](https://user-images.githubusercontent.com/109990443/196004918-ada64c15-4abd-4f5f-8188-670348794d23.png)


