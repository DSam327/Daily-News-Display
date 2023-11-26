from django.contrib import admin
from disp_news.models import daily_news
# Register your models here.

class newsadmin(admin.ModelAdmin):
    list_display=('news_title', 'news_desc', 'news_img')

admin.site.register(daily_news, newsadmin)
