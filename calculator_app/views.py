from django.http import HttpResponse
from django.shortcuts import render

def calculate(request, operation, num1, num2):
    if operation == 'add':
        result = num1 + num2
        template = 'calc/add.html'
    elif operation == 'subtract': 
        result = num1 - num2
        template = 'calc/subtract.html'
    elif operation == 'multiply': 
        result = num1 * num2 
        template = 'calc/multiply.html'
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
            template = 'calc/divide.html'
        else:
            return HttpResponse("Error: Division by zero!")
    else:
        return HttpResponse("Invalid operation!")

    parts = {
        'num1': num1,
        'num2': num2,
        'result' : result,
    }
    return render(request, template, parts)