from django.http.response import HttpResponse
from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. 장고 템플릿!")

# 지시사항
# 로또번호 표시
def lottos(request):
    lotto = []
    while len(lotto) < 6:
        lotto.append(random.randint(1,46))
        lotto = list(set(lotto))
    print(lotto)

    return HttpResponse(f"이번주 로또 번호 : {lotto}")


