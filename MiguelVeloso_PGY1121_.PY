entradas=[]
disponibilidad=["disponible,X,disponible, disponile,disponible,x"]
asistentes=[]
totalcantidad=[]
tipo=[]

def ganacias():
    print(f"""GANANCIAS TOTALES
          
          TIPO DE ENTRADA: {totalcantidad}
          
          """)

def listado():
    asistentes=int(input("ingrese su rut: "))
    asistentes.append.lista
    print(asistentes)


def comprar():
    print("************Tipo de entrada**************")
    print("1. platinum $(120000)")
    print("2. Gold $(80000)")
    print("3. Silver $(50000)")
    entradas=input("ingrese que tipo de entrada quiere: ")
    match entradas:
        case "1":
            input("indique su nombre: ")
            input("indique su apellido: ")
            int(input("indique su rut: "))
            print("platinum")
            cantidad1=int(input("ingrese entre 1 a 3 entradas: "))
            total=(cantidad1*120000)
            print("el total de sus compra de entradas:")
            print(total)

            
        case "2":
            input("indique su nombre: ")
            input("indique su apellido: ")
            int(input("indique su rut: "))
            print("gold")
            cantidad2=int(input("ingrese entre 1 a 3 entradas: "))
            total=(cantidad2*80000)
            print("el total de sus compra de entradas:")
            print(total)

        case "3":
            input("indique su nombre: ")
            input("indique su apellido: ")
            int(input("indique su rut: "))
            print("silver")
            cantidad3=int(input("ingrese entre 1 a 3 entradas: "))
            total=(cantidad3*50000)
            print("el total de sus compra de entradas:")
            print(total)





def disponibilidad():
    print("estas estan disponible:")










while True:
        print("""

            **********PRODUCTORA DE EVENTOS CREATIVOS.CL**********
        1. comprar entradas
        2. Mostrar ubicaciones disponbles 
        3. ver listado de asistentes
        4. Mostrar ganacias totales 
        5. Salir 
                                            """)
        opcion=input("ingrese una opcion: ")
        match opcion:
            case "1":
                comprar()
            case "2":
                disponibilidad()
            case "3":
                listado()
            case "4":
                ganacias()
            case "5":
                print("salir...")
                break



            

