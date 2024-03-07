def pago():

    diasTrabajados = input('Ingrese la cantidad de dias trabajados: ')
    horasExtras = input('Ingrese las horas extras trabajadas: ')
    valorDia = input('Ingrese el valor del día: ')

    descuentoxCafeteria =input('Ingrese el descuento por cafeteria: ')
    cuotaPrestamo = input('Ingrese la cuota del prestamo')

    pagoData= {
        'diasTrabajados': diasTrabajados,
        'horasExtras': horasExtras,
        'valorDia': valorDia,
        'descuentosxCafeteria': descuentoxCafeteria,
        'cuotaPrestamo': cuotaPrestamo
    }

    calculo = diasTrabajados * valorDia 
    print(calculo)
