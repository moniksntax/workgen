import random
from django.shortcuts import render

from django.shortcuts import redirect


def home(request):
     return render(request, 'tools/home.html') 




jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the computer go to therapy? It had too many bytes.",
    "Parallel lines have so much in common… It’s a shame they’ll never meet."
]

def joke_generator(request):
    joke = random.choice(jokes)
    return render(request, 'tools/joke.html', {'joke': joke})

import requests
from django.shortcuts import render

def joke_generator(request):
    response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
    if response.status_code == 200:
        data = response.json()
        joke = data.get('joke', "Couldn't fetch a joke right now.")
    else:
        joke = "Error fetching joke."
    return render(request, 'tools/joke.html', {'joke': joke})

first_names = ["Alice", "Bob", "Charlie", "Daisy"]
last_names = ["Smith", "Johnson", "Lee", "Brown"]



def number_generator(request):
    import random
    min_val = int(request.GET.get('min', 1))
    max_val = int(request.GET.get('max', 4000))
    number = random.randint(min_val, max_val)
    return render(request, 'tools/number.html', {'number': number})



from django.shortcuts import render
import random
from datetime import datetime, timedelta

def date_generator(request):
    start_str = request.GET.get('start', '2020-01-01')  # default start date
    end_str = request.GET.get('end', '2025-01-01')      # default end date

    try:
        start_date = datetime.strptime(start_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_str, '%Y-%m-%d')

        if start_date > end_date:
            start_date, end_date = end_date, start_date  # Swap if in wrong order

        delta_days = (end_date - start_date).days
        random_days = random.randint(0, delta_days)
        random_date = start_date + timedelta(days=random_days)

        return render(request, 'tools/date.html', {'random_date': random_date.date()})

    except ValueError:
        return render(request, 'tools/date.html', {'error': 'Invalid date format. Use YYYY-MM-DD.'})
 
