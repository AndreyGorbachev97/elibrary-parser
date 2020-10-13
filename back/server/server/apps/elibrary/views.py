import mimetypes
import os

from django.http import HttpResponse
from . import parserhtml
from . import writeToDoc
import json

def index(request):
    # print(parserhtml.parse())
    print(request.GET.get("startYear"))
    print(request.GET.get("endYear"))
    print(request.GET.get("id"))
    print(request.GET.get("directory"))
    print(request.GET.get("name"))
    name = request.GET.get("name")
    directory = request.GET.get("directory")
    start_year = request.GET.get("startYear")
    end_year = request.GET.get("endYear")
    data = parserhtml.parse(request.GET.get("id"))
    # data = [
    #     {"year": "2005"},
    #     {"year": "2008"},
    #     {"year": "2009"},
    #     {"year": "2009"},
    #     {"year": "2019"},
    #     {"year": "2020"},
    #     {"year": "2020"},
    #     {"year": "2020"}
    # ]
    print(data)
    filter_data = list(filter(lambda obj: int(obj["year"]) >= int(start_year), data))
    filter_data = list(filter(lambda obj: int(obj["year"]) <= int(end_year), filter_data))
    print('data', filter_data)
    writeToDoc.write('s.docx', filter_data, directory, name)

    return HttpResponse(json.dumps(filter_data), content_type="application/json")

# print(request.GET.get("rangYear"))
    # return HttpResponse(json.dumps(parserhtml.parse()), content_type="application/json")
    # return HttpResponse(open('v1.docx', 'rb'), as_attachment=True)
    # return HttpResponse('hhhh', content_type="application/json")
