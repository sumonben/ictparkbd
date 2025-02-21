from .models import Post
from accounts.models import CustomUser
from blog.models import Category,Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count

def posts(request):
        allpost=Post.objects.all().select_related('author').order_by('-id')

        d = timezone.now() - timedelta(days=100)
        post=Post.objects.all().select_related('author')
        latest_posts=Post.objects.all().select_related('author').order_by('-id')[:7]
        popular_posts = Post.objects.annotate(total_views=Count('likes')).filter(date_created__gte=d, total_views__gt=0).order_by('-total_views')[:5]
        users=CustomUser.objects.all()
        post=Post.objects.all().select_related('author').order_by('-id')[:8]
        categories=Category.objects.all()
        tags=Tag.objects.all()

        post=Post.objects.order_by('date_created')
        page = request.GET.get('page', 1)
        paginator = Paginator(post, 5)
        try:
         post = paginator.page(page)
        except PageNotAnInteger:
         post = paginator.page(1)
        except EmptyPage:
         post = paginator.page(paginator.num_pages)
        return {
        'all_posts': post,
        'allpost': allpost,
          'post': post,
          'users':users,
          'popular_posts':popular_posts,
          'latest_posts':latest_posts,
          'categories':categories,
          'tags':tags
    }