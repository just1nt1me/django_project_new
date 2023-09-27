from django.shortcuts import render
from .models import Post

# dummy data
# list of dictionaries, each dict has post content
# posts = [
#     {
#         'author': 'Mujo',
#         'title': 'First blog',
#         'content': 'Read my post here',
#         'date_posted': 'September 28, 2023'
#     },
#     {
#         'author': 'John Doe',
#         'title': 'John\'s story',
#         'content': 'Here\'s my post',
#         'date_posted': 'September 28, 2023'
#     }
# ]

# return what we want user to see from "home" page
def home(request):
    # dictionary to pass into render function
    context = {
        # set each post to be pulled from SQL database
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# return what we want user to see from "about" page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
