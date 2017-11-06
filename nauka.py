
def censor(line, word):
    zdanie = line.split(' ')
    wyraz = ''

    for x in range (0, len(zdanie)):
        for y in word:
            if zdanie[x] == y:
                zdanie[x]='*'*len(y)
            elif zdanie[x] == (y+','):
                zdanie[x] = '*'*len(y)+','
            elif zdanie[x] == (y+'.'):
                zdanie[x] = '*'*len(y)+'.'

        wyraz = wyraz + zdanie[x] + ' '

    wyraz = ''.join(wyraz)
    print (wyraz)
def count(sequence, item):
    ilosc = 0
    for x in sequence:
        if x == item:
            ilosc+=1
    return ilosc
def purify(lista):
    lista2 = []
    poz = len(lista) - 1
    for x in lista:
        if x % 2 == 0:
            lista2.append(x)

    return lista2
def remove_duplicates(lista):
    lista2 = []

    lista=sorted(lista)
    lista2=[lista[0]]
    for x in lista:
        if x > lista2[-1]:
            lista2.append(x)
    return lista2
def mediana(lista):
    lista2=sorted(lista)
    if len(lista)%2 == 0:
        temp1=lista[int((len(lista)/2)-1)]
        temp2=lista[int(len(lista)/2)]
        temp=(temp1+temp2)/2
    elif len(lista)%2 !=0:
        temp = lista[int(len(lista)/2-1)]

    return temp
def flip_bit(number, n):
  mask = 0b00000001 << (n-1)
  result = number ^ mask
  return bin(result)
