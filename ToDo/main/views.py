from django.shortcuts import render
# from django.http import HttpResponse


posts = [
    {
        "content": "Learn Spanish",
        "status": False
    },
    {
        "content": "Make ToDo App",
        "status": False
    },
    {
        "content": "Sleep",
        "status": False
    },
    {
        "content": "College Work",
        "status": False
    },
    {
        "content": "WWWWWWWWWWWWWWWWWWWWWWWWW",
        "status": False
    },
]


def home(request):
    context = {
        "posts": posts
    }

    return render(request, "main/home.html", context)
