from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Product
from django.core.serializers import serialize
from django.db import connection
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import  SqlLexer
from sqlparse import format

# Create your views here.
def home(request):
    qs = Product.objects.all()
    serializer_data = serialize("json", qs) 
    q =list(connection.queries)
    for qs in q:
        sqlformatted = format(str(qs['sql']), reindent=True)
        print(highlight(sqlformatted, SqlLexer(),TerminalFormatter()))
    serializer_data = json.loads(serializer_data)
    return JsonResponse(serializer_data, safe=False, status=200)
 