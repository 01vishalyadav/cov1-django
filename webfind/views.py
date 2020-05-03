from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.

def findOnline():
  # url = pyperclip.paste()
  url = "https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Uttar_Pradesh"
  page = requests.get(url)

  soup = BeautifulSoup(page.content, 'html.parser')
  soup.prettify()
  info=[]
  input_output_list = soup.find_all('tr')
  for l in input_output_list:
    if "Azamgarh" in l.get_text():
      for el in l.get_text().split('\n'):
        if(len(el)>0):
          info.append(el)
  return info
from django.http import HttpResponse
def hello(request):

  webinfo = findOnline()
  distName = webinfo[1]
  activeCases = webinfo[2]

  context = {"distName":distName,
             "activeCases":activeCases,
            }
  # return HttpResponse("Welcome to the world of python!")
  # return HttpResponse(soup)
  return render(request,"hello.html", context)
