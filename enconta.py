import requests
import datetime
import time

class Enconta:
    
    def __init__(self):
        #Inicializar variable que llevará la cuenta de las llamadas
        self.calls = 0 
        
    def consulta(self,iden,fi,ff):
        #Petición GET que se le hace al servidor pasandole cómo parámetro el id la fecha inicio y la fecha de fin
        req = requests.get('http://34.209.24.195/facturas?id='+iden+'&start='+fi+'&finish='+ff)
        #Verificar si la respuesta que dio el servidor es númerica
        if(str(req.json()).isdigit()):
            #Retorna el número de facturas cuando es inferior a 100
            return req.json()
        else:
            #Cuando la respuesta es superior a 100, se toman las dos fechas que están en formato String
            #y se separan los datos por el simbolo "-" para obtener año, mes y día en un arreglo
            fI = fi.split('-');
            fF = ff.split('-');
            #Se pasan las fechas a días, como la librería time maneja los años con los 2 últimos digitos
            #por ejemplo 2017 -> 17, entonces se utiliza el [:2] para obtener los 2 últimos dígitos
            fechaI = time.strptime(fI[0][:2]+" "+fI[1]+" "+fI[2], "%y %m %d").tm_yday
            fechaF = time.strptime(fF[0][:2]+" "+fF[1]+" "+fF[2], "%y %m %d").tm_yday
            #Se obtiene la diferencia de días entre las dos fechas
            m = (fechaF - fechaI)//2
            #Se suma la diferencia de días a la fecha inicial para obtener la fecha de la mitad
            mitad = fechaI + m
            #Cada vez que hayan más de 100 resultados se sumará una llamada más a la función consultar
            self.calls+=1
            #Se hace la suma del resultado de la función recurrente de la fecha inicial hasta la mitad y de la mitad + 1 hasta la fecha
            #final
            req.close()
            return self.consulta(iden,fi,self._conversion(mitad,fI[0])) + self.consulta(iden,self._conversion(mitad+1,fI[0]),ff)
    
    #Convierte los días del año que representa la fecha de la mitad en fecha
    def _conversion(self,mitad,year):
        fechaM = str(datetime.datetime.strptime(year+" "+str(mitad), '%Y %j').strftime('%Y-%m-%d'))
        return fechaM
    
    #Retorna el número de llamadas que se le hizo a la función consultar
    def getCalls(self):
        return self.calls
    
        

