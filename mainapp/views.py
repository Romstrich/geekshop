from django.shortcuts import render


# Create your views here.
def index(request):
    context={
        'title':'Geekshop',

    }
    return render(request, 'mainapp/index.html',context)


def products(request):
    context = {
        'title': 'Geetshop Каталог',

    }
    return render(request, 'mainapp/products.html', context)


# def test(request):
#     context = {
#         'title': 'geekshop_test',
#         'main_header':'Проверка контекста',
#         'welcome':'Приветствую, ',
#         'user':'Ромыч',
#         'items':[
#             {'name':'Худи черного цвета с монограммами adidas Originals','price':6900},
#             {'name': 'Синяя куртка The North Face', 'price': 23725},
#             {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390},
#             {'name': 'Черный рюкзак Nike Heritage', 'price': 2340},
#             {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590},
#             {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890}
#     ],
#     }
    return render(request, 'test.html', context)
