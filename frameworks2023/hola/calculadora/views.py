from django.shortcuts import render

def calculadora(request):
    if request.method == 'POST':
        if request.POST.get('operacion'):
            print(request.POST)
        oper = request.POST.get('operacion')
        num1 = float(request.POST.get('num1', None))
        num2 = float(request.POST.get('num2', None))
        cal = Calculadora()
        resultado = cal.operacion(oper, num1, num2)
        return render(request, 'calculadora.html', {'resultado': resultado})
    
    return render(request, 'calculadora.html')

class Calculadora:     
    def operacion(self, oper, num1, num2):
        operaciones = {
            '+': self.sumar(num1, num2),
            '-': self.restar(num1, num2),
            '*': self.multiplicar(num1, num2),
            '/': self.dividir(num1, num2)
        }
        return operaciones[oper]
    
    def sumar(self, num1, num2):
        return num1 + num2
    
    def restar(self, num1, num2):
        return num1 - num2
    
    def multiplicar(self, num1, num2):
        return num1 - num2
    
    def dividir(self, num1, num2):
        return num1 - num2