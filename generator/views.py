from django.shortcuts import render
import random
import string

def home(request):
    password = ""
    if request.method == "POST":
        length = int(request.POST.get("length", 8))
        use_upper = 'uppercase' in request.POST
        use_lower = 'lowercase' in request.POST
        use_digits = 'digits' in request.POST
        use_symbols = 'symbols' in request.POST

        characters = ""
        if use_upper:
            characters += string.ascii_uppercase
        if use_lower:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if characters:
            password = ''.join(random.choice(characters) for _ in range(length))

    return render(request, "home.html", {"password": password})