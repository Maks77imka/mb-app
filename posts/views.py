from django.views.generic import ListView
from posts.models import Post
# Create your views here.


class HomePageView(ListView):
    model = Post
    template_name = "posts/home.html"
    context_object_name = "all_posts_list" # ListView возвращает список object_list по умолчанию