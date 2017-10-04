from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse,Http404
from udhaar.models import Transactions,Groups
from django.core import serializers
import json

# Create your views here.
def index(request):
    data  = Groups.objects.order_by('gid').distinct().values('gid')
    print (data)
    return render(request,'udhaar/home.html',{'groupids':data})

def info(request,groupid):
    data = Transactions.objects.filter(gid=groupid).values('to','from_user','amount')
    if not data:
        raise Http404("No!")

    datajson = []

    for i in data:
        datajson.append(i)

    datajson = json.dumps(datajson)

    #data = get_list_or_404(Transactions, gid=groupid)
    #qs_json = serializers.serialize('json', data)
    #print (qs_json)
    #print (data[0].to)

    #from django.http import JsonResponse
    #return JsonResponse(data)


    return render(request, 'udhaar/info.html', {'info': datajson})
    #return HttpResponse("You are looking at %s" % groupid)

def creategroup(request):
    return render(request, 'udhaar/newgroup.html')

def addtransaction(request):
    return "hello world"
