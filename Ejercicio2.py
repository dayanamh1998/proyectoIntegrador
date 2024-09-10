#Elabore un programa para el Éxito que determine el salario de los 1897 empleados 
# de su compañía, teniendo en cuenta las comisiones y la seguridad social que
#  debe pagar, e imprima el listado de la información.

# creamos una funcion llamada calcularSalario y le damos el parametro numEmpleados 
def calcularSalario(numEmpleados):
    #Inicializamos el array 
    salarios =[]
    
    # creamo un ciclo para saber cuantos empleados van a ingresar ya que sabemos que son 1897
    for i in range(numEmpleados):
        salarioBase = float(input(f"Ingrese  el salario base del empleado {i + 1}: "))
        comision = float(input(f"Ingrese la comisión del empleado {i + 1}: "))
        seguridadSocial = float(input(f"Ingrese el monto de seguridad social del empleado {i + 1}: "))
        salarioTotal = salarioBase + comision - seguridadSocial
        salarios.append(salarioTotal)
    return salarios

numEmpleados = 1897
salario = calcularSalario(numEmpleados)
print("listado de salarios")

for i, lsalario in enumerate(salario):
    print(f"Empleado {i + 1}: ${lsalario:.2f}")

# Mostramos el listado de los salarios de los empleados 