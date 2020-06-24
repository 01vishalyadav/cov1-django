from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.


from .forms import DistForm
def get_dist(request):
  if request.method == 'POST':
    form = DistForm(request.POST)
    if form.is_valid():
      count = findOnline(request.POST['dist_name'])
      return render(request,'index.html',{'form':form,'distname':request.POST['dist_name'],'count':count})
  else:
    form=DistForm()
  return render(request,'index.html',{'form':form})



def findOnline(dist):
  # dist = "Azamgarh"
  # url = pyperclip.paste()
  try:
    url = "https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Uttar_Pradesh"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    soup.prettify()
    info=[]
    input_output_list = soup.find_all('tr')
    for l in input_output_list:
      if dist in l.get_text():
        for el in l.get_text().split('\n'):
          if(len(el)>0):
            info.append(el)
    return info[2]
  except:
    return -1
  


def hello(request):

  # webinfo = findOnline()
  # distName = webinfo[1]
  # activeCases = webinfo[2]
  distName = "test"
  activeCases = -1
  context = {"distName":distName,
             "activeCases":activeCases,
            }
  # return HttpResponse("Welcome to the world of python!")
  # return HttpResponse(soup)
  return render(request,"index.html", context)
