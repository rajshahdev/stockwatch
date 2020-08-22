from django.shortcuts import render,redirect
from .models import Stock
from .form import StockForm
from django.contrib import messages

# Create your views here.
#pk_d3b6bf4f23e7349b19d74e0bd70184a6 

# from nsetools import Nse
# from pprint import pprint
# nse = Nse()

# q = nse.get_quote(input())
# pprint(q['lastPrice'])


def home(request):
    import requests
    import json

    if request.method =='POST':
        ticker=request.POST['ticker']
        api_request=requests.get("https://cloud.iexapis.com/stable/stock/" + ticker +"/quote?token=pk_48b1b4f09d8b46e7a8eaec4136ff4ebe")
        try:
            api=json.loads(api_request.content)
        except Exception as e:
            api="error"
        return render(request,'home.html',{'api':api})

    else:
        ticker=Stock.objects.all()
        output=[]
        for ticker_item in ticker:
            api_request=requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item)+"/quote?token=pk_48b1b4f09d8b46e7a8eaec4136ff4ebe")
            try:
                api=json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api="error"
        return render(request,'home.html',{'ticker':"Ticker Does not exist",'output':output})

def add_stock(request):
    import requests
    import json

    if request.method =='POST':
        form=StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,("Stock has been Added"))
            return redirect("stock")
    else:
        ticker=Stock.objects.all()
        output=[]
        for ticker_item in ticker:
            api_request=requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item)+"/quote?token=pk_48b1b4f09d8b46e7a8eaec4136ff4ebe")
        
            try:
                api=json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api="Error..."

        return render(request,'add_stock.html',{'ticker':ticker,'output':output})

def delete(request,stock_id):
    item=Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request,("Stock has been Deleted"))
    return redirect("stock")
