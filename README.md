# Introducción
El programa fue desarrollado en Python 3, consta de 3 archivos, enconta.py el cual contiene la clase y métodos que realizan los calculos, main.py el cual recibe los parámetros y llama a la clase enconta para posteriormente mostrar la respuesta y por último testEnconta.py el cual contiene pruebas de unidad. 


# Instrucciones

  - Clonar los programas del siguiente repositorio en Git.
```sh
$ git clone https://github.com/9410ger/FacturasEnconta.git
```
 - En la terminal abrir la ubicación de los programas anteriormente mencionados.
```sh
$ cd /home/FacturasEnconta
```
 - Para ejecutar el código se realiza el siguiente comando.
 ```sh
$ py main.py
```
- Si hay algún error con la librería "requests", se ejecuta este comando para instalarlo
 ```sh
$ py -m pip install requests
```
 - Cuando se accede al programa, se le pedirá al usuario 3 parámetros, el id, la fecha inicial y la fecha final, estas dos últimas en formato (YYYY-MM-DD), se coloca el valor y luego presionar ENTER para seguir.
 ```sh
$ py main.py
Ingrese el identificador: 4e25ce61-e6e2-457a-89f7-116404990967
Ingrese la fecha inicial con el formato YYYY-MM-DD: 2017-01-01
Ingrese la fecha final con el formato YYYY-MM-DD: 2017-03-17
```
 - Al final el programa le mostrará al usuario, el número de facturas y llamadas que se realizaron a la función, en caso de que hayan más de 100 resultados se le notificará al usuario.
  ```sh
Hay más de 100 resultados
Número de facturas: 248
Numero de llamadas: 3
```
- Para ejecutar las pruebas, en la misma carpeta se ingresa el siguiente comando.
```sh
$ py testEnconta.py
```
 - Se le mostrará al usuario si las pruebas pasaron o no.
 
```sh
...
----------------------------------------------------------------------
Ran 3 tests in 2.716s
OK
```