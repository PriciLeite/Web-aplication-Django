from multiprocessing import context
# Criando a rendenização do about.html template/rango/
from urllib import response
from django.shortcuts import render
from rango.models import category, page


def index(request):
    #Consulta o banco de dados para uma lista de TODAS as categorias atualmente armazenadas.
    #Ordene as categorias pelo número de curtidas em ordem decrescente.
    # Recupere apenas os 5 primeiros -- ou todos se forem menores que 5.
    # Coloque a lista em nosso dicionário context_dict (com nossa mensagem em negrito!) 
    #que será passada para o mecanismo de template    
    category_list = category.objects.order_by('-like')[:5]

    context_dict = {}    
    context_dict ['boldmessage'] = 'Estudos, Primeiro aplicativo web , Tutorial Django!'
    context_dict['categories'] = category_list 
    return render(request, 'rango/index.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        Category = category.objects.get(slug=category_name_slug)
        # Recupere todas as páginas associadas.
        # O filter() retornará uma lista de objetos de página ou uma lista vazia.
        Pages = page.objects.filter(category=Category)
        # Adiciona nossa lista de resultados ao contexto do modelo nas páginas de nome.
        context_dict['pages'] = Pages
        # Também adicionamos o objeto de categoria de
        # o banco de dados para o dicionário de contexto.
        # Usaremos isso no modelo para verificar se a categoria existe.
        context_dict['category'] = Category
    except category.DoesNotExist:
       # Chegamos aqui se não encontramos a categoria especificada.
        # Não faça nada -
        # o modelo exibirá a mensagem "sem categoria" para nós.
        context_dict['category'] = None
        context_dict['pages'] = None
        # Vai renderizar a resposta e devolvê-la ao cliente.
    return render(request, 'rango/category.html', context=context_dict)
