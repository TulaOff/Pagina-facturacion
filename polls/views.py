from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import os


@login_required
def home(request):
    cuit = request.user.username
    enero_exist = os.path.exists(fr"C:\Users\offen\PycharmProjects\Pagina-facturacion\facturas_enero\{cuit}.pdf")
    request.session['enero_exist'] = enero_exist
    febrero_exist = os.path.exists(fr"C:\Users\offen\PycharmProjects\Pagina-facturacion\facturas_febrero\{cuit}.pdf")
    request.session['febrero_exist'] = febrero_exist
    marzo_exist = os.path.exists(fr"C:\Users\offen\PycharmProjects\Pagina-facturacion\facturas_marzo\{cuit}.pdf")
    request.session['marzo_exist'] = marzo_exist
    nc_enero_exist = os.path.exists(fr"C:\Users\offen\PycharmProjects\Pagina-facturacion\nc_enero\{cuit}.pdf")
    request.session['nc_enero_exist'] = nc_enero_exist
    nc_febrero_exist = os.path.exists(fr"C:\Users\offen\PycharmProjects\Pagina-facturacion\nc_febrero\{cuit}.pdf")
    request.session['nc_febrero_exist'] = nc_febrero_exist
    nc_marzo_exist = os.path.exists(fr"C:\Users\offen\PycharmProjects\Pagina-facturacion\nc_marzo\{cuit}.pdf")
    request.session['nc_marzo_exist'] = nc_marzo_exist
    abril_exist = os.path.exists(fr"C:\Users\offen\PycharmProjects\Pagina-facturacion\facturas_abril\{cuit}.pdf")
    request.session['abril_exist'] = abril_exist
    return render(request, 'polls/facturas.html', {'cuit': cuit})


def facturas(request):
    return render(request, 'polls/facturas.html')


def pagar(request):
    return render(request, 'polls/pagar.html')