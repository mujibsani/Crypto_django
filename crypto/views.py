from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    #Grab cripto price data ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content.decode("utf-8"))

    #Grab Crypto news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content.decode("utf-8"))
    return render(request, 'home.html', {'api': api,"price":price})


def prices(request):
    if request.method == 'POST':
        import json
        import requests
        quote = request.POST['quote']
        quote=quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=USD")
        crypto = json.loads(crypto_request.content.decode("utf-8"))
        return render(request,'prices.html',{'quote':quote,'crypto':crypto})
    else:
        notfound = "Enter a crypto Currency symbolinto the search box"
        return render(request, 'prices.html', {'notfound':notfound})