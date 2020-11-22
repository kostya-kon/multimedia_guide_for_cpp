from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from lessons.forms import Test1


def home(request):
    return render(request, "index.html")


def lessons_home(request):
    return HttpResponsePermanentRedirect("/lessons/1/")


def lessons(request, id):
    html_page = "lessons/lesson" + id + ".html"
    return render(request, html_page)


def test(request, id):
    html_page = "tests/test" + id + ".html"

    answer_dict = {'question1': ['1'], 'question2': ['2'], 'question3': ['3']}
    context = {"form": Test1}

    grade = -1

    if request.method == "GET":
        return render(request, html_page, context=context)
    if request.method == "POST":
        grade = 0
        userform = Test1(request.POST)
        data = dict(request.POST)
        data.pop("csrfmiddlewaretoken")
        if userform.is_valid():
            for i in data:
                if data[i] == answer_dict[i]:
                    grade += 1
            context["grade"] = grade
            return render(request, html_page, context=context)
    # return render(request, "delete_me_test.html", context=context)


def about(request):
    pass