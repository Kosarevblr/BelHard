# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int


numb = int(input('Vvedi chislo: '))


def perevod(numb):
    schisl = input('Vyberi sistemy shisleniya dlya perevoda(decimal/binary): d/b').lower()

    if schisl == 'b':
        new_numb = ''
        while numb > 0:
            new_numb = str(numb % 2) + new_numb
            numb = numb // 2

    elif schisl == 'd':
        numb = str(numb)
        new_numb = 0
        for i in range (0,len(numb)):
            new_numb += int(numb[i])*(2**(len(numb)-i-1))

    return new_numb
print(perevod(numb))