from django.shortcuts import render
from search.models import Champion
from django.db.models import Q


# index.html 페이지를 부르는 index 함수
from search.models import Post, Video

# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'search/index.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    return render(request, 'search/blog.html', {'postlist':postlist})

def garen(request):
    return render(request, 'search/garen.html')

def ashe(request):
    return render(request, 'search/ashe.html')

# def search1(request):
#     kw = request.GET.get('kw', '')  # 검색어
#
#     if 'kw':
#         Champions1 = Champion.objects.all().filter(
#             Q(name__icontains=kw)
#         )
#     return render(request, 'search/result.html', {'kw': kw, 'Champions1': Champions1})

def indexx(request):
        kw = request.GET.get('kw', '')
        _champion = Champion.objects.all()

        if 'kw':
            Champions1 = Champion.objects.all().filter(
                        Q(name__icontains=kw)
                    )

            context = {'champions': _champion, 'kw': kw, 'Champions1': Champions1}
            return render(request, 'search/indexx.html', context)

        else:
            context = {'champions': _champion}
            return render(request, 'search/indexx.html', context)


from django.shortcuts import HttpResponseRedirect

from django.urls import reverse

# url = /create_todo
def create_champion(request):
    content = request.POST['championname']
    new_champion = Champion(title=content)
    new_champion.save()
    return HttpResponseRedirect(reverse('indexx'))

def delete_champion(request):
    _id = request.GET['chmapionnum']
    champion = Champion.objects.get(id=_id)
    champion.delete()
    return HttpResponseRedirect(reverse('indexx'))



def video_list(request):
    video_list = Video.objects.all()
    return render(request, 'video/video_list.html', {'video_list': video_list})









