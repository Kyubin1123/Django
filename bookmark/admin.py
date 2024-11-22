from django.contrib import admin

from bookmark.models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url']
    # 리스트 표시
    list_display_links = ['name', 'url']
    # 리스트 표시된 부분 링크를 누를 수 있게 변경
    list_filtter = ['name', 'url']
    # 리스트를 필터처리

# admin.site.register(Bookmark, BookmarkAdmin)
# = @admin.register(Bookmark)
