from django.shortcuts import render

"""def count_w(request):
    if request.method == "POST":
        count_word = request.POST.get('count')
        count = 0
        for i in count_word:
            if i == " ":
                count += 1
        context = {
            "count":count+1
        }
        return render(request, "count_word.html", context)
    return render(request, "count_word.html")"""

def count_w(request):
    if request.method == "POST":
        count_word = request.POST.get('count')
        words = count_word.split()
        #print(words)
        word_count = len(words)
        context = {
            "count": word_count
        }
        return render(request, "count_word.html", context)
    return render(request, "count_word.html")

def count_c(request):
    if request.method == "POST":
        count_character = request.POST.get('count')
        character_count = len(tuple(count_character))
        #print(character_count)
        context = {
            "count": character_count
        }
        return render(request, "count_character.html", context)
    return render(request, "count_character.html")
    