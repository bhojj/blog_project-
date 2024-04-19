from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author' : 'Bhoj Raj Joshi',
        'title' : 'Blog Post 1',
        'content' : 'First Post Content',
        'date_posted' : '17 April 2024'
    },
    {
        'author' : 'Roshan Joshi',
        'title' : 'Blog Post 2',
        'content' : 'Second Post Content',
        'date_posted' : '18 April 2024'

    }
]

# Create your views here.
def home (request):
    # return HttpResponse('<h1> Blog Home </h1>')
    # return render(request, 'blog/home.html')
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about (request):
    # return HttpResponse('<h1> Blog About</h1>')
    return render (request, 'blog/about.html', {'title':'About'})
