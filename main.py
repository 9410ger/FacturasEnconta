from enconta import Enconta

def main():
    #Se inicializa la clase que va a hacer los calculos
    e = Enconta()
    #Se piden los parámetros 
    iden = input("Ingrese el identificador: ")
    fi = input("Ingrese la fecha inicial con el formato YYYY-MM-DD: ")
    ff = input("Ingrese la fecha final con el formato YYYY-MM-DD: ")
    #En caso de que algún parámetro no esté se le notifica al usuario y se le da la oportunidad de volver a ingresar
    #los parámetros
    while(len(iden) == 0 or len(fi) == 0 or len(ff) == 0):
        print("Faltan parámetros")
        iden = input("Ingrese el identificador: ")
        fi = input("Ingrese la fecha inicial con el formato YYYY-MM-DD: ")
        ff = input("Ingrese la fecha final con el formato YYYY-MM-DD: ")
    #Se llama a la función recurrente
    res = e.consulta(iden,fi,ff)
    #Si la respuesta es menor a 100 imprimirá el número de facturas y de llamadas realizadas
    if(res < 100):
        print("Numero de facturas: "+str(res))
        print("Numero de llamadas: "+str(e.getCalls()))
    #Si la respuesta es mayor a 100, se imprimirá el aviso, el número de facturas y la cantidad de llamadas
    else:
        print("Hay más de 100 resultados")
        print("Número de facturas: "+str(res))
        print("Numero de llamadas: "+str(e.getCalls()))


#si la función se llama main se inicia
if __name__ == '__main__':
    main()
