from django.shortcuts import render

# Create your views here.
# pip install block-io==1.1.15
from block_io import BlockIo

def index(request):
    context = dict()

    context['data'] = 'Test API Çalışması'

    template = 'index.html'
    return render(request, template, context)


def bitcoinAPI(request):
    context = dict()
    version = 2
    yourapI = '00c6-f206-7e73-bf39'
    secret = 'goztepe35'
    adresss = '2NAXDbBeDB5RCYFNg6WUzJydcnuawyirTYg'

    block_io = BlockIo(yourapI, secret, version)
    a =block_io.get_balance()
    b = block_io.get_address_balance(labels='LABEL')

    #context['data2'] = json.load(a)

    context['data'] = a
    context['data2'] = b
    print(b.values())


    template = 'wallet.html'
    return render(request, template, context)
