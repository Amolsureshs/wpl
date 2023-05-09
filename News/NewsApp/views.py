


from django.shortcuts import render
from newsapi import NewsApiClient
  
# Create your views here. 
def getNews(request):
      
    newsapi = NewsApiClient(api_key ='d90a7bb67ebc48a1a06ca854fc72574e')
    top = newsapi.get_top_headlines(sources ='techcrunch')
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
  
    return render(request, 'news.html', context ={"mylist":mylist})



    
