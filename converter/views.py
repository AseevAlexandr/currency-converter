from django.shortcuts import render
import requests

from converter.services import API_URL


def get_exchange_rates():
    url = API_URL
    response = requests.get(url)
    return response.json()

def currency_converter_view(request):
    rates = get_exchange_rates()
    available_currencies = rates['rates'].keys() if rates and 'rates' in rates else []

    converted_amount = None
    error_message = None
    if request.method == "POST":
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        amount = request.POST.get('amount')

        if from_currency in rates['rates'] and to_currency in rates['rates']:
            try:
                amount = float(amount)
                conversion_rate = rates['rates'][to_currency] / rates['rates'][from_currency]
                converted_amount = amount * conversion_rate
            except ValueError:
                error_message = "Please enter a valid amount."
        else:
            error_message = "Selected currencies are not valid."

    return render(request, 'converter/index.html', {
        'available_currencies': available_currencies,
        'converted_amount': converted_amount,
        'error_message': error_message,
    })

