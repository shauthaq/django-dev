from django.shortcuts import render
from .models import Asset

def asset_list(request):
    """リース品一覧画面"""
    # データベースからすべてのリース品を取得
    assets = Asset.objects.all().order_by('asset_number')
    
    # テンプレートにデータを渡して表示
    context = {
        'assets': assets,
    }
    return render(request, 'assets/list.html', context)