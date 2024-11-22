from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from bookmark.models import Bookmark


def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    # SELECT * FROM bookmark
    context = { 'bookmarks': bookmarks }

    return render(request, 'bookmark_list.html', context)
    # return HttpResponse("<h1>북마크 리스트 페이지 입니다.</h1>")

def bookmark_detail(request, pk):
    try:
        bookmark = Bookmark.objects.get(pk=pk)
    except:
        raise Http404

    # from django.shortcuts import get_object_or_4o4
    # bookmark = get_object_or_404(Bookmark, pk=pk)

    context = {'bookmark': bookmark}
    return render(request, 'bookmark_detail.html', context)
