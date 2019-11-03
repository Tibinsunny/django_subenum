from django.shortcuts import render
from django.shortcuts import HttpResponse
from urllib.request import urlopen
import json
'''html = urlopen("https://crt.sh/?q=%25.clickup.com&output=json").read()
jsonResponse = json.loads(html.decode('utf-8'))
res = [ sub['name_value'] for sub in jsonResponse ]
res=list(dict.fromkeys(res))'''
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'asd'})
def asd(request):
    val1=request.GET["num1"]
    try:
        html = urlopen("https://crt.sh/?q=%25."+val1+"&output=json").read()
        jsonResponse = json.loads(html.decode('utf-8'))
        res = [ sub['name_value'] for sub in jsonResponse ]
        res=list(dict.fromkeys(res))
    except:
        res="The site returned a huge data"
    return render(request,'base.html',{'value':val1,'result':res})
