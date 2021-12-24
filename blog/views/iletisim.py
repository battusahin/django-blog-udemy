from django.shortcuts import render, redirect
from blog.forms import IletisimForm
from blog.models import IletisimModel

def iletisim(request):
    form = IletisimForm(initial={     #initial default olara kutunun içerisini doldurur.
        'isim_soyisim' : 'Batuhan Şahin',
        'email' : 'battusahin97@gmail.com',
        'mesaj' : 'deneme'
    })

    if request.method == 'POST':
        form = IletisimForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anasayfa')
            

    context={
        'form' : form
    }
    return render(request, 'pages/iletisim.html', context=context)  