print('iniciando programa....')

#texto a ingresar
texto = input(f'\nIngresa el texto a analizar: ').lower()

#letras a ingresar y transformarlas
lista = []
lista.append(input(f'Ingresa una letra para analizar: ').lower())
lista.append(input(f'Ingresa una letra para analizar: ').lower())
lista.append(input(f'Ingresa una letra para analizar: ').lower())

print(f'\n')
print('CANTIDAD DE LETRAS')
#mostrar datos solicitados de las letras
print(f'La letra "{lista[0]}" aparece {texto.count(lista[0])} veces en el texto')
print(f'La letra "{lista[1]}" aparece {texto.count(lista[1])} veces en el texto')
print(f'La letra "{lista[2]}" aparece {texto.count(lista[2])} veces en el texto')

#mostrar datos solicitados del texto
print(f'\n')
print('CANTIDAD DE PALABRAS')
texto_lista = texto.split()
print(f'El texto tiene {len(texto_lista)} palabras')

print(f'\n')
print('PRIMER Y ULTIMO CARACTER')
print(f'El primer caracter del texto es: {texto[0]} \nEl ultimo caracter del texto es: {texto[-1]}')

print(f'\n')
print('TEXTO INVERTIDO')
texto_lista.reverse()
texto_inverso = " ".join(texto_lista[::])
print(f'El texto invertido se veria asi: \n{texto_inverso}')

print(f'\n')
print('BUSCAR LA PALABRA PYTHON EN TEXTO')
python = "python" in texto
dic = {True:"Si", False:"No"}
print(f'La palabra "python" se encuentra en el texto? : {dic[python]}')
