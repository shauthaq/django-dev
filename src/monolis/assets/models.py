from django.db import models

class Asset(models.Model):
    # ステータスの選択肢
    ASSET_STATUS_CHOICES = [
        ('available', '利用可能'),
        ('in_use', '利用中'),
        ('maintenance', '修理中'),
        ('retired', '廃棄'),
    ]
    
    # 種別の選択肢
    ASSET_TYPE_CHOICES = [
        ('pc', 'パソコン'),
        ('laptop', 'ノートPC'),
        ('tablet', 'タブレット'),
        ('printer', 'プリンター'),
        ('monitor', 'モニター'),
        ('phone', '電話機'),
        ('medical', '医療機器'),
        ('furniture', '家具'),
        ('other', 'その他'),
    ]
    
    # データベースのフィールド定義
    asset_number = models.CharField(max_length=50, unique=True, verbose_name='資産番号')
    name = models.CharField(max_length=200, verbose_name='品名')
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPE_CHOICES, verbose_name='種別')
    manufacturer = models.CharField(max_length=100, verbose_name='メーカー', blank=True)
    model_number = models.CharField(max_length=100, verbose_name='型番', blank=True)
    purchase_date = models.DateField(verbose_name='購入日')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='購入価格')
    status = models.CharField(max_length=20, choices=ASSET_STATUS_CHOICES, default='available', verbose_name='状態')
    location = models.CharField(max_length=200, verbose_name='設置場所', blank=True)
    notes = models.TextField(verbose_name='備考', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'リース品'
        verbose_name_plural = 'リース品一覧'
        ordering = ['asset_number']
    
    def __str__(self):
        return f"{self.asset_number} - {self.name}"