from operator import itemgetter

def most_fequent(lista):
    lista2 = tuple(lista.lower())
    char_lista2 = (set(lista2))
    a = []
    for i in range(0,len(char_lista2)):
        a.append(0)
    lista3 = list(zip(char_lista2,a))
    lista3 = dict(lista3)
    for x in lista3:
        for y in lista2:
            if x ==y:
                lista3[x]+=1
    lista3 = tuple(zip(lista3.keys(), lista3.values()))
    lista3 = sorted(lista3, key=itemgetter(1), reverse=1)
    print ((lista3))
    
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] +=1
    return d


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


def rotate_word(tekst, m):
    alfabet_p = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    tekst = tekst.lower()
    new_tekst = ''
    print (tekst)

    for x in tekst:
        for y in alfabet:
            if x == y:
                if (alfabet.find(y)) + s < 0:
                    new_tekst += alfabet[0]
                elif (alfabet.find(y) + s) > (len(alfabet)-1):
                    new_tekst += alfabet[len(alfabet)-1]
                else:
                    new_tekst += alfabet[alfabet.find(y) + s]
    print (new_tekst)
    
def nested_sum(lista):
    count = 0
    for x in lista:
        for y in x:
            count+=y
    return count

def cumsum(lista):
    lista2=[]
    count = 0
    for x in lista:
        count+=x
        lista2.append(count)
    return lista2

def middle(lista):
    lista2 = []
    count = 0
    for x in lista:
        if 0<count<len(lista):
            lista2.append(x)
        count+=1
    return lista2

def chop(lista):
    lista2 = []
    count = 0
    for x in lista:
        if 0==count or count==(len(lista)-1):
            lista.remove(x)
        count+=1
    print(lista)
   

def is_sorted(lista):
    lista2 = sorted(lista)
    if lista2 == lista:
        return True
    else:
        return False
    
def is_anagram(s1, s2):
    if len(s1)==len(s2):
        s12 = sorted(list(s1))
        s22 = sorted(list(s2))
        if s12==s22:
            return True
        else:
            return False
    else:
        return False

def has_duplicate(s1):
    s11=sorted(s1)
    count = 0
    ok = 0
    for x in s11:
        if count<(len(s11)-1):
            if x == s11[count+1]:
                ok+=1
        count+=1
    if ok>0: return True
    else: return False

def reverse_pair(lista):
    s11=[]
    s11.extend(lista)
    lista3 = []
    for x in s11:
        for y in s11:
            if x==y[::-1]:
                lista2=[]
                lista2.append(x)
                lista2.append(y)
                lista3.append(lista2)
                s11.remove(y)

    print (lista,'\n', lista3)   
