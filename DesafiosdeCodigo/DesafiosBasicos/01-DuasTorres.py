entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

icm = distancia / (diametro1 + diametro2)

print(f'{icm:.2f}')
