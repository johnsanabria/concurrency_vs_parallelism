#
# Definición recursiva de la obtención de la posición n en la serie de 
# Fibonacci
#
# Autor: John Sanabria - john.sanabria@correounivalle.edu.co
# Fecha: 2023-01-10
#
def fibo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibo(n - 1) + fibo(n - 2)
