from django.contrib import admin
from .models import BoardModel
# Register your models here.

admin.site.register(BoardModel)
# こういうもん！覚えてこれ書かないと管理者画面からこのモデルが開けない