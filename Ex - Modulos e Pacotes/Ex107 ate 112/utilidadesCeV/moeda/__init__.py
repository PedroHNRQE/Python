def dobro(n=0.0, m=True):
    d = n * 2
    if m:
        d = moeda(d)
    return d


def metade(n=0.0, m=True):
    met = n / 2
    if m:
        met = moeda(met)
    return met


def aumentar(n=0.0, ta=0, m=True):
    a = ta * n / 100
    n += a
    if m:
        n = moeda(n)
    return n


def diminuir(n=0, ta=0, m=True):
    a = ta * n / 100
    n -= a
    if m:
        n = moeda(n)
    return n


def moeda(n=0.0):
    valor = f'R${n:.2f}'.replace('.', ',')
    return valor


def lin():
    print('-' * 30)


def resumo(n=0, a=0, d=0):
    lin()
    print('     RESUMO DO VALOR     ')
    lin()
    print(f'Preco analisado: \t{moeda(n)}')
    print(f'Dobro do preco: \t{dobro(n)}')
    print(f'Metade do preco: \t{metade(n)}')
    print(f'{a}% de aumento: \t{aumentar(n, a)}')
    print(f'{d}% de reducao: \t{diminuir(n, d)}')
    lin()