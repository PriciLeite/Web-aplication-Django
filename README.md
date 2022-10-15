# Web application with Django. <br>
#### DESCRIÇÃO: <br>
Django é um framework de web server-side extremamente popular e repleto de características, escrito em Python. O módulo mostra por que o Django é um dos frameworks web mais populares, como configurar um ambiente de desenvolvimento e como começar a usa-lo para criar seus próprios aplicativos da Web. A explicação para construção do 
aplicativo não inclui detalhes sobre a escrita do script de preenchimento ao qual foi inserido no banco de dados, visto que o script está diponivel para FORK. Mas, fazendo o passo-a-passo das configurações do sistema operacional e migrando os dados do script para seu banco criado com seu usuário da forma como explicado, permitirá a visualização do aplicativo localmente em sua maquina. <br>

*** Página Inicial do Aplicativo ***

![aplicativoWeb_Django](https://user-images.githubusercontent.com/109990443/196002716-c1aaba62-2867-40b4-83a6-a2e149cc0e27.png)


#### COMEÇANDO: <br>
Para a criação do projeto e para execução será necessário:
* Primeiramente instalar Python (Versão utilizada 3.9) https://www.python.org/ <br>
* Instalar : Framework Django e Pillow <br>

#### PARA ISSO NO SHELL DIGITE: <br>
* pip install django.
* pip install pillow. <br>    (obs: pip é um comando python, portanto é necessário instalar primeiramente python);  

#### SE FOR CRIAR O PROJETO DO ZERO. CASO CONTRÁRIO FAZENDO FORK DO SCRIPT ACIMA NÃO SERÁ NECESSÁRIO CRIAR PASTAS PARA O PROJETO: 
###### OBS: VOCÊ DEVERÁ APONTAR PARA O SHELL O CAMINHO DO DIRETÓRIO O QUAL SALVOU O SEU PROJETO. <br> CASO ESTEJA UTILIZANDO VERSIONAMENTO GIT DEVERÁ CRIAR PRIMEIRO A PASTA E INSERIR O ENDEREÇO NO SHELL.
![diretorio](https://user-images.githubusercontent.com/109990443/196004415-898a0db5-aecd-4ea7-b0e7-f30038ccf3bf.png) <br>
Em Shell:
* django-admin startproject projectname - (Para criar o projeto do zero);
* Python manage.py startapp nameapp - (Para criar o aplicativo do zero); <br>

#### SUBSTITUA POR SEU DIRETÓRIO DA PASTA template; <br>
![template](https://user-images.githubusercontent.com/109990443/196011456-2ccd9093-8b0e-4a69-8a12-984cd672e9db.png)

#### SUBSTITUA POR SEU DIRETÓRIO DA PASTA static; <br>
![static](https://user-images.githubusercontent.com/109990443/196011627-1e37aaf1-2a67-4ebe-a518-e7b630e09909.png)


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

#### CLICANDO NO LINK NA INTERFACE DO BANCO DE DADOS PARA VISUALIZAR O  WEB SITE: 
#### VERÁ: 
![aplicativoWeb_Django](https://user-images.githubusercontent.com/109990443/196009146-394b03aa-25a7-455d-823d-00aa7c0dc272.png) <br>

![aplicativoWebCategoria_Django](https://user-images.githubusercontent.com/109990443/196009158-476aafb1-1acb-4427-8894-ab713601f965.png) <br>

![aplicativoWebPaginaDaWeb_Django](https://user-images.githubusercontent.com/109990443/196009169-fb673a6e-94a1-46bb-9ec8-4ced93885be5.png) <br>

![aplicativoWebCategoria2_Django](https://user-images.githubusercontent.com/109990443/196009164-ea8695b0-00aa-4d94-9514-7cac83d8a6ec.png) <br>

![aplicativoWebCategoria3_Django](https://user-images.githubusercontent.com/109990443/196009267-ff2e5098-64a1-4dfa-8a36-7ab7370189b0.png) <br>


