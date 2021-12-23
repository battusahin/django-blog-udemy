from django.shortcuts import render

def anasayfa(request):
    context = {
        'isim' : 'Batuhan Şahin',
    }
    return render(request, 'pages/anasayfa.html', context=context)