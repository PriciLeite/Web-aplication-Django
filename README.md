# Web Application Django. <br>
Uma breve demonstração de como utilizar o framework Django para criar uma página static para Web.<br>

### Home 

![aplicativoWeb_Django](https://user-images.githubusercontent.com/109990443/196002716-c1aaba62-2867-40b4-83a6-a2e149cc0e27.png)


#### Ferramentas: <br>
* Python (Versão utilizada 3.9) https://www.python.org/ <br>
* Framework Django e Pillow 

#### Configurações: <br>
* pip install django.
* pip install pillow. <br>    (pip para python, no terminal cmd);  

* django-admin startproject projectname - (Para criar PROJETO);
* Python manage.py startapp nameapp - (Para criar o APLICATIVO); <br>
* Substituir SEU DIRETÓRIO em template; <br>
* Substituir SEU DIRETÓRIO em static; <br>



#### CRIANDO USUÁRIO PARA O PROJETO:
###### OBS: DJANGO POR PADRÃO JÁ VEM CONFIGURADO COM O BANCO DE DADOS SqlLite, ENTÃO DEVERÁ APENAS CRIAR UM USUÁRIO NO SHELL.
* python manage.py createsuperuser - (Para criar usuário)<br>
![dados do usuario](https://user-images.githubusercontent.com/109990443/196005530-a0bd4529-8300-432c-8892-c96e9b1db2bc.png)

#### MIGRANDO O SCRIP DISPONIVEL ACIMA PARA O BANCO DE DADOS:
* python manage.py makemigrations nomeapp - (Para migrar o scrip de código)<br>

###### APÓS CRIAR USUÁRIO E MIGRAR O SCRIPT ESTABELEÇA CONEXÃO COM O BANCO DE DADOS:
* Python manage.py runserver - Para iniciar seu servidor use: localhost - para Django será localhost:8000)<br>
![localholst](https://user-images.githubusercontent.com/109990443/196004918-ada64c15-4abd-4f5f-8188-670348794d23.png)

#### ACESSE APÓS ESTABELECER CONEXÃO:
* http://localhost:8000/admin/ <br>
![login](https://user-images.githubusercontent.com/109990443/196007815-fa288cb9-eb39-4a44-94e3-52c3446dbbf1.png)

#### TEMOS ENTÃO ACESSO AO BANCO QUE FOI CRIADO COM O SCRIPT: <br>
![bancodedados](https://user-images.githubusercontent.com/109990443/196008528-f45fc5f8-9cf3-43ef-8636-ed4357be27fa.png)

#### EXIBIÇÃO DAS PÁGINAS: <br>
![pages](https://user-images.githubusercontent.com/109990443/196008710-3d20915e-afdd-44f0-ae0d-edc205a85a03.png)

#### EXIBIÇÃO DAS CATEGORIAS: <br>
![categorias](https://user-images.githubusercontent.com/109990443/196008854-468eb6c9-0aba-443c-9268-fc274164f972.png)



