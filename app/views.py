"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http.response import JsonResponse
from app import data_accesser

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

# ビュー表示関数
def for_view(req):    
    return render(req,'app/surprise.html')

# AJAX呼び出し関数
def for_ajax(req):    
    import json
    from django.http import HttpResponse,Http404

    if req.method == 'POST':
        #txt = req.POST['your_txt']  # POSTデータを取得

        # DBから辞書形式でデータを取得
        results = data_accesser.get_data()

        # 辞書をJSON形式に変換
        response = json.dumps(results)  

        # JSONデータを返却
        return HttpResponse(response,content_type='application/json')

    else:
        raise Http404