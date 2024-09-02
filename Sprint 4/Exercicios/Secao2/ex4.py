operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

def calcular_valor_maximo(operadores, operandos) -> float:
    def aplicar_operacao(op, a_b):
        a, b = a_b
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        elif op == '%':
            return a % b

    resultados = map(lambda x: aplicar_operacao(*x), zip(operadores, operandos))
    return max(resultados)

print(float(calcular_valor_maximo(operadores, operandos)))
