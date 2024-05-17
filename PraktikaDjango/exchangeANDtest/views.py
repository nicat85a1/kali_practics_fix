from django.shortcuts import render

"""def exchange(request):
    exchange_usd = 1.7
    exchange_euro = 1.83
    exchange_u_e = 0.93
    exchange = 0
    money2 = ''
    if request.method == "POST":
        money1 = request.POST.get('money1')
        money2 = request.POST.get('money2')
        exchange_input = request.POST.get('ei')

        if not exchange_input:
            return render(request, "exchange.html", {'error': 'Please fill in all fields.'})

        try:
            exchange_input = float(exchange_input)
        except ValueError:
            return render(request, "exchange.html", {'error': 'Please enter valid numbers.'})
        
        if money1 == 'dollar' and money2 == 'manat':
            exchange = exchange_input * exchange_usd
        elif money1 == 'manat' and money2 == 'dollar':
            exchange = exchange_input / exchange_usd
        elif money1 == 'euro' and money2 == 'manat':
            exchange = exchange_input * exchange_euro
        elif money1 == 'manat' and money2 == 'euro':
            exchange = exchange_input / exchange_euro
        elif money1 == 'dollar' and money2 == 'euro':
            exchange = exchange_input * exchange_u_e
        elif money1 == 'euro' and money2 == 'dollar':
            exchange = exchange_input / exchange_u_e

        context = {
            'exchange': exchange,
            'money2': money2
                }
        return render(request, "exchange.html", context)
        
    return render(request, "exchange.html")"""


import requests

def get_exchange_rate(from_currency, to_currency):

    url = f"https://v6.exchangerate-api.com/v6/80c34514425aa133d57e39f7/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    rate = data['conversion_rates'][to_currency]
    
    return rate

def exchange(request):
    if request.method == "POST":
        money1 = request.POST.get('money1')
        money2 = request.POST.get('money2')
        exchange_input = request.POST.get('ei')

        if not exchange_input:
            return render(request, "exchange.html", {'error': 'Please fill in all fields.'})

        try:
            exchange_input = float(exchange_input)
        except ValueError:
            return render(request, "exchange.html", {'error': 'Please enter valid numbers.'})

        exchange_rate = get_exchange_rate(money1, money2)

        exchange = exchange_input * exchange_rate

        context = {
            'exchange': exchange,
            'money2': money2
                }
        return render(request, "exchange.html", context)
        
    return render(request, "exchange.html")

answers = ['1', '1', '1', '3', '2', '2', '3', '2', '1', '3']
score_input = 'Dogru Cavab'

def test(request):
    score = 0
    if request.method == 'POST':
        user_answers = []
        for i in range(len(answers)):
            #answer = request.POST[f'quiz{i+1}']
            answer = request.POST.get(f'quiz{i+1}')
            user_answers.append(answer)

        for i, answer in enumerate(user_answers):
            if answer == answers[i]:
                score += 1
        context = {
            'score': score,
            'score_input': score_input
                }
        
        return render(request, 'test.html', context)

    return render(request, 'test.html')



def calculator(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        operation = request.POST['operation']

        if not num1 or not num2:
            result = 'Please fill in all fields.'
            return render(request, 'calculator.html', {'result': result})

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            result = 'Please enter valid numbers'
            return render(request, 'calculator.html', {'result': result})

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Divide by zero error.'
                return render(request, 'calculator.html', {'result': result})

        return render(request, 'calculator.html', {'result': result})
    else:
        return render(request, 'calculator.html')