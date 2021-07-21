from django.shortcuts import render
# from django.http import HttpResponse


posts = [
    {
        "Content": "Learn Spanish",
        "Status": False
    },
    {
        "Content": "Make ToDo App",
        "Status": False
    },
    {
        "Content": "Sleep",
        "Status": False
    },
]


def home(request):
    context = {
        "posts": posts
    }

    return render(request, "main/home.html", context)
