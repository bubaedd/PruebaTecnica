"""
Autor:Benjamin Manuel Vargas Bürger, Ingeniero Civil en computación con mencion en informatica
Asunto: Prueba Tecnica, Ejercicio1
Fecha de creación:29/05/2021
"""

import  json

if __name__ == '__main__':

        #manejo de excepciones
        try:
            # apertura de datos json
            with open('C:/Users/Bemjamin Vargas/Desktop/prueba tecnica/data1.json') as f:
                # Inicialización de variables

                cantidad_ciudades = 0
                sum_var1 = 0
                sum_var2 = 0
                list_var1 = []
                # inicialización de variables booleanas
                boolProvincia2 = False
                boolRegion4 = False
                # Carga de datos de json
                data = json.load(f)

                for i in range(len(data)):
                    # obtencion de datos de regiones
                    regions_dict = data[i]
                    # filtro para region4
                    if (regions_dict['name'] == 'Region4'):
                        boolRegion4 = True
                    else:
                        boolRegion4 = False
                    # obtención de datos de provincia
                    list_childrensRegions = regions_dict['children']
                    for i in range(len(list_childrensRegions)):
                        # obtención de datos de para diccionario de pronvincias
                        provincia_dict = list_childrensRegions[i]
                        # Filtro para provincia2
                        if (provincia_dict['name'] == 'Provincia2'):
                            boolProvincia2 = True
                        else:
                            boolProvincia2 = False
                        # obtención de datos de ciudades
                        list_ciudades = provincia_dict['children']
                        for i in range(len(list_ciudades)):
                            # obtención de datos de para diccionario de ciudades
                            ciudades_dict = list_ciudades[i]
                            # suma de var1
                            sum_var1 += ciudades_dict['values']['var1']
                            # si es provincia2 se empieza la suma de valores para var2
                            if (boolProvincia2):
                                sum_var2 += ciudades_dict['values']['var2']
                            # si la region es la 4 se guardan los valores de var1
                            if (boolRegion4):
                                list_var1.append(ciudades_dict['values']['var1'])
                        # variable para obtener la candidad de ciudades por provincia
                        cantidad_ciudades += len(list_ciudades)
                # despliegue de datos
                print("Promedio var1:", (sum_var1 / cantidad_ciudades))
                print("suma var2 Provincia2:", sum_var2)
                print("max var1 Region 4:", max(list_var1))


        except(Exception) :
            print("ERROR:",Exception)


