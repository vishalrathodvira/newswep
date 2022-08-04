from django.shortcuts import render
API_KEY="c71bff0eb1f84ccbbf6458304ca592cc"
import requests
# GET https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}
# Create your views here.
def home(request):
    search = request.GET.get('search')
    country = request.GET.get('country')
    category = request.GET.get('category')

    

    if search:
        url=f'https://newsapi.org/v2/everything?q={search}&apiKey={API_KEY}'

        data=requests.get(url)
        responce=data.json()
        articles=responce['articles']

    elif country:
        url=f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        data=requests.get(url)
        responce=data.json()
        articles=responce['articles']

    elif category:
        url=f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        data=requests.get(url)
        responce=data.json()
        articles=responce['articles']

        
    else:
        url=f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
        data=requests.get(url)
        responce=data.json()
        articles=responce['articles']
    newses={'articles':articles}

    #print(responce)
    return render(request,'index.html',newses)
    


