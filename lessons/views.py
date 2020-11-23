from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from lessons.forms import *
from lessons.answers import *


def home(request):
    return render(request, "home.html")


def lessons_home(request):
    return HttpResponsePermanentRedirect("/lessons/1/")


def lessons(request, id):
    html_page = "lessons/lesson" + id + ".html"
    context = {"classname" : "'lesson" + id + "'"}
    print(context)
    return render(request, html_page, context=context)


def test(request, id):
    html_page = "tests/test" + id + ".html"

    choose_form = {"1": (Test1, answer_dict_1), "2": (Test2, answer_dict_2),
                   "3": (Test3, answer_dict_3), "4": (Test4, answer_dict_4)}
    form, answer_dict = choose_form[id]

    context = {"form": form}
    grade = -1
    if request.method == "GET":
        return render(request, html_page, context=context)
    if request.method == "POST":
        grade = 0
        userform = form(request.POST)
        data = dict(request.POST)
        data.pop("csrfmiddlewaretoken")
        if userform.is_valid():
            for i in data:
                if data[i] == answer_dict[i]:
                    grade += 1
            context["grade"] = grade
            return render(request, html_page, context=context)
        else:
            return HttpResponse(userform.errors)
    # return render(request, "delete_me_test.html", context=context)


def about(request):
    return render(request, "team.html")