def gera_vetor(n):
    perg = []
    print('Você está com febre alta entre 39 °C e 40 °C ?')
    op = str(input('Sim ou Não ?'))
    perg.append(op)

    print('Você está Nauseas ?')
    op = str(input('Sim ou Não ?'))
    perg.append(op)

    print('Você está Vomitando ?')
    op = str(input('Sim ou Não ?'))
    perg.append(op)

    print('Você está com dor de cabeça ?')
    op = str(input('Sim ou Não ?'))
    perg.append(op)

    print('Você está com dor atrás dos olhos ?')
    op = str(input('Sim ou Não ?'))
    perg.append(op)

    print('Você está com manchas vermelhas na pele ?')
    op = str(input('Sim ou Não ?'))
    perg.append(op)

    print('Você está com mau estar geral ?')
    op = str(input('Sim ou Não ?'))
    perg.append(op)

    print('Você está com cansaço excessivo ?')
    op = str(input('Sim ou Não ?'))
    perg.append(op)

    return perg
