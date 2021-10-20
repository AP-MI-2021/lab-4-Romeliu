def read_list():
    #returneaza doua liste de intregi
    lista1_int = []
    lista2_int = []
    lista1 = input("Dati prima lista de numere intregi separate prin spatii: ")
    lista2 = input("Dati a doua lista de numere intregi separate prin spatii: ")
    lista1_str = lista1.split(' ')
    lista2_str = lista2.split(' ')
    for nr1 in lista1_str:
        lista1_int.append(int(nr1))
    for nr2 in lista2_str:
        lista2_int.append(int(nr2))
    return lista1_int, lista2_int

def number_of_evens(lista)->int:
    #retureaza numarul de numere pare din lista primita ca parametru
    numar_de_pare = 0
    for element in lista:
        if element % 2 == 0:
            numar_de_pare += 1
    return numar_de_pare

def test_number_of_evens():
    assert number_of_evens([1,12,3,42,2]) == 3
    assert number_of_evens([1,3,5,6,9]) == 1
    assert number_of_evens([14,52,3,34,35,25,4]) == 4

def same_number_of_evens(lista1, lista2)->bool:
    #returneaza true daca listele primite ca parametrii contin acelasi numar de numere pare
    if number_of_evens(lista1) == number_of_evens(lista2):
        return True
    return False

def intersection(lista1, lista2):
    #returneaza o lista de intregi care reprezinta intersectia listelor primite ca parametru
    lista_intersectie = []
    for element in lista1:
        if lista2.count(element) >= 1:
            lista_intersectie.append(element)
            while lista2.count(element) != 0:
                lista2.remove(element)
    return lista_intersectie

def test_intersection():
    assert intersection([1,2,4],[4,5,6]) == [4]
    assert intersection([1],[4]) == []
    assert intersection([1,2,3,4,14],[14,3,5,7]) == [3,14]

def show_intersection(lista1, lista2):
    lista3 = intersection(lista1, lista2)
    if len(lista3) == 0:
        print("Intersectia celor doua multimi este multimea vida")
    else:
        print(f"Intersectia celor doua multimi este multimea formata din elementele {lista3}")

def is_palindrom(nr)->bool:
    #verifica daca un numar este egal cu oglinditul sau
    oglinda = oglindit(nr)
    if nr == oglinda:
        return True
    else:
        return False

def test_is_palindrom():
    assert is_palindrom(1221) == True
    assert is_palindrom(131) == True
    assert is_palindrom(34123523) == False
    assert is_palindrom(4141) == False

def oglindit(nr)->int:
    #returneaza oglinitul numarului primit ca parametru
    oglinda = 0
    while nr:
        oglinda = oglinda * 10 + nr % 10
        nr = nr // 10
    return oglinda

def test_oglindit():
    assert oglindit(1234) == 4321
    assert oglindit(12) == 21
    assert oglindit(4124) == 4214
    assert oglindit(1221) == 1221

def get_lista_palindroame(lista1, lista2):
    lista_palindrom = []
    pozitie = 0
    while len(lista1) > pozitie and len(lista2) > pozitie:
        nr_str = str(lista1[pozitie]) + str(lista2[pozitie])
        if is_palindrom(int(nr_str)):
            lista_palindrom.append(int(nr_str))
        pozitie += 1
    return lista_palindrom

def show_palindrom(lista1, lista2):
    lista3 = get_lista_palindroame(lista1, lista2)
    if len(lista3) == 0:
        print("Nu exista niciun palindrom format prin concatenarea elementelor din lista de pe aceleasi pozitii")
    else:
        print(f"Lista de palindroame obtinute este: {lista3}")

def read_third_list():
    #citeste a treia lista de intregi
    lista = []
    lista_str = input("Dati a treia lista de numere intregi separate prin spatii: ")
    lista_str_lst = lista_str.split(' ')
    for nr1 in lista_str_lst:
        lista.append(int(nr1))
    return lista

def divizibil_cu_lista3(numar, lista3)->bool:
    #verifica daca numar este divizibil cu fiecare element din lista3
    for element in lista3:
        if numar % element != 0:
            return False
    return True

def genereaza_lista_cu_oglinidit(lista_init, lista3):
    index = 0
    while index < len(lista_init):
        if divizibil_cu_lista3(lista_init[index],lista3):
            lista_init[index] = oglindit(lista_init[index])
        index += 1
    return lista_init

def show_mirrored_lists(lista1, lista2, lista3):
    lista1 = genereaza_lista_cu_oglinidit(lista1, lista3)
    lista2 = genereaza_lista_cu_oglinidit(lista2, lista3)
    print(f"Listele obtinute sunt: {lista1} si {lista2}")

def menu():
    print("""
    Meniu:
    1. Introduceti cele doua liste de intregi.
    2. Afisati daca cele două liste au acelasi numar de elemente pare.
    3. Afiseaza intersectia listelor citite
    4. Afisati toate palindroamele obtinute prin concatenarea elementelor de pe aceleași pozitii in cele doua liste
    5. Cititi o a treia lista si afisati listele obtinute prin inlocuirea in cele doua liste citite la punctul 1 a
tuturor elementelor cu oglinditul lor daca indeplinesc urmatoarea regula: elementele sunt divizibile
cu toate elementele din a treia lista. Daca nu indeplinesc regula, pastrati elementul asa cum e.
    x. Iesire
    """)
    optiune = input("introduceti optiunea aleasa: ")
    lista1 = []
    lista2 = []
    lista3 = []
    while optiune != 'x':
        if optiune == '1':
            lista1, lista2 = read_list()
        elif optiune == '2':
            if same_number_of_evens(lista1, lista2):
                print("Cele doua liste au acelasi numar de elemente pare.")
            else:
                print("Cele doua liste NU au acelasi numar de elemente pare.")
        elif optiune == '3':
            show_intersection(lista1, lista2)
        elif optiune == '4':
            show_palindrom(lista1, lista2)
        elif optiune == '5':
            lista3 = read_third_list()
            show_mirrored_lists(lista1, lista2, lista3)
        else:
            print("Optiunea introdusa nu este valida!")
        optiune = input("introduceti optiunea aleasa: ")

def main():
    test_number_of_evens()
    test_is_palindrom()
    test_oglindit()
    test_intersection()
    menu()

main()