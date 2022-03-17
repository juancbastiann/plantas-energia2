plantas = {
    'Quito': ('Coca Codo Sinclair', 'Sopladora'),
    'Guayaquil': ('Coca Codo Sinclair', 'Sopladora'),
    'Loja': ('Sopladora'),
    'Tena': ('Sopladora'),
    'Manta': ('Sopladora')
}

consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84}
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Tena': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Manta': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32}
    },
}

informacion = {
    'Costa': ('Guayaquil', 'Manta'),
    'Sierra': ('Quito', 'Ambato', 'Loja'),
    'Oriente': ('Tena', 'Nueva Loja')
}

region = input('Region: ')

for regiones, ciudades in informacion.items():
#    print(regiones, ':', ciudades)
    if region in regiones:
        total_coca = ((sum(consumo_energia['Coca Codo Sinclair']['{}'.format(ciudades[0])]['consumos']))*(consumo_energia['Coca Codo Sinclair']['{}'.format(ciudades[0])]['tarifa']))
        total_sopladora = ((sum(consumo_energia['Sopladora']['{}'.format(ciudades[0])]['consumos']))*(consumo_energia['Sopladora']['{}'.format(ciudades[0])]['tarifa']))

        total_costa = total_coca + total_sopladora
        print('{} :'.format(region),'$',total_costa)

