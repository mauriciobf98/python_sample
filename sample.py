def input_point_comment():
    while True:
     print('Por favor, introduzca una puntuación en una escala de 1 a 5')
     point = input()
     if point.isdecimal():
          point = int(point)
          if   point <= 0 or point > 5: # Expresión condicional de menor que 0 o mayor que 5.
               print('Indíquelo en una escala de 1 a 5')
               point = input()
          else:
                print('Introduzca sus comentarios.')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                file_pc = open("data.txt", 'a')
                file_pc.write(f'{ post } \n')
                file_pc.close()
                break
     else:
         print('Introduzca los puntos de valoración como números')

def output_point_comment():
    print('Resultados hasta la fecha.')
    read_file = open("data.txt", "r")
    print( read_file.read() )
    read_file.close()  

def finish_point_comment():
    print('Terminación.')
   


while True:
    print('Seleccione el proceso que desea aplicar')
    print('1:Introducir puntos de evaluación y comentarios')
    print('2:Comprueba los resultados hasta ahora.')
    print('3:Terminar.')
    num = input()

    if num.isdecimal():
        num = int(num)
        if num == 1:
            input_point_comment()   
        elif num == 2:
            output_point_comment()
        elif num == 3:
            finish_point_comment()
            break  # Sintaxis para terminar un proceso repetitivo.
        else:
            print('Introduzca de 1 a 3')
    else:
        print('Introduzca de 1 a 3')