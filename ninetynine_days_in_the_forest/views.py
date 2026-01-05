from django.shortcuts import render
from django.http import Http404


MAX_DAYS = 99  # game length
GAME_NAME = "99 Days in the Forest"

def home(request):
    context = {
        'title': GAME_NAME,
        'total_days': MAX_DAYS,
    }
    return render(request, 'home.html', context)


def days(request):
    context = {
        'days': range(1, MAX_DAYS + 1),
        'game_name': GAME_NAME,
    }
    return render(request, 'days.html', context)


def day_detail(request, day):
    if day < 1 or day > MAX_DAYS:
        raise Http404("Day does not exist")

    context = {
        'game_name': GAME_NAME,
        'day': day,
        'next_day': day + 1 if day < MAX_DAYS else None,
        'previous_day': day - 1 if day > 1 else None,
    }
    return render(request, 'day_details.html', context)


def about(request):
    return render(request, 'about.html', {'game_name': GAME_NAME})
