#Definimos una función para generar un oligonucleotido, las funciones son importantes para que sea más fácil leer el código
def genera_oligonucleotido(bases, oligonucleotidos):
#Las funciones funcionan como máquinas a las que le metes cosis para trabajar y ellas hacen el trabajo, adentro del paréntesis metemos las cosis que necesita la función
	from random import choice
	oligonucleotido = choice(bases) + choice(bases) + choice(bases) + choice(bases) #Los sumamos para que se concatenen y se vuelvan un solo elemento
#Definimos una lista con las bases
bases = ['A','C','G','T']
#Definimos una lista vacía donde guardaremos los oligonucleótidos que se irán formando
oligonucleotidos = []
#Aquí invocaremos al a función y le pasaremos las cosis que va a utilizar
while i <= 256: #i es una abreviación de iterador, es decir, un número que nos ayudará a contar cuantas veces hemos repetido algo
	#a continuación utilizaremos la función que creamos hace rato
	genera_oligonucleotido(bases, oligonucleotidos)
	#en esta linea declararemos que por default el oligonucleotido generado no está en la lista (porque no lo hemos buscado)
	ya_esta = "false"
	#en la siguiente linea buscaremos que el oligonucleotido generado ya esté en nuestra lista de oligonucleotidos
	for numero in oligonucleotidos:
		#Si el oligonucleotido que generamos está en la lista, nuestra diremos que el oligonucleotido ya está contenido
		if oligonucleotido == oligonucleotidos[numero]:
			ya_esta = "true"
	#Si el oligo nucleotido NO esta en nuestra lista, lo agregamos y lo mostramos en pantalla
	if ya_esta != "true":
		oligonucleotidos[i] = oligonucleotido
		print oligonucleotido
		i = i + 1 #como agregamos un oligonucleotido entonces decimos que ya tenemos uno más de los 256

