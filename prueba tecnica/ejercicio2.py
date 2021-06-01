"""
Autor:Benjamin Manuel Vargas Bürger, Ingeniero Civil en computación con mencion en informatica
Asunto: Prueba Tecnica, Ejercicio2
Fecha de creación:29/05/2021
"""
import json
from  datetime import datetime ,timedelta



if __name__ == '__main__':
    #Manejo de excepciones en codigo
    try:
        #Carga de datos
        with open('C:/Users/Bemjamin Vargas/Desktop/prueba tecnica/data2.json') as f:
            #Obtencion de datos de json
            data = json.load(f)
            #Inicialización de lista para almacenar los tiempos de espera
            list_tiempoEspera = []
            #Variables usadas para los conteos de ciclos
            cont_cycle_tipo1 = 0
            cont_cycle_tipo2 = 0
            #Acceso de datos a json
            for i in range(len(data)):
                #Carga de datos de diccionario json
                dict_DataCamion = data[i]
                #Filtro para primedio de zonas de esperas
                if (dict_DataCamion['zone'] == 'AE1' or dict_DataCamion['zone'] == 'AE2' or dict_DataCamion[
                    'zone'] == 'BE1' or dict_DataCamion['zone'] == 'BE2'):
                    #Obtencion y conversión de tiempo  de inicio de los datos de json
                    t_in = datetime.strptime(dict_DataCamion['dt_in'].split('T')[1], '%H:%M:%S').time()
                    #Conversión de tiempo en segundos
                    t_in_s = t_in.second + t_in.minute * 60 + t_in.hour * 3600
                    # Obtencion y conversión de tiempo  de termino de los datos de json
                    t_out = datetime.strptime(dict_DataCamion['dt_out'].split('T')[1], '%H:%M:%S').time()
                    # Conversión de tiempo en segundos
                    t_out_s = t_out.second + t_out.minute * 60 + t_out.hour * 3600
                    #verificación de que no exista un resultado de tiempo negativo
                    if (t_in_s > t_out_s):
                        #obtención de diferencia de tiempo
                        def_t = t_in_s - t_out_s
                    else:
                        def_t = t_out_s - t_in_s
                    #adición de diferencia de tiempo a lista de tiempo de espera
                    list_tiempoEspera.append(def_t)
                #FIltro para zonas de trabajo de tipo 2
                if (dict_DataCamion['zone'] == 'AW2' or dict_DataCamion['zone'] == 'BW2'):
                    #Contador de ciclos encontrados
                    cont_cycle_tipo2 += 1
                #Filtro para zonas de trabajo de tipo 1
                if (dict_DataCamion['zone'] == 'AW1' or dict_DataCamion['zone'] == 'BW1'):
                    # Contador de ciclos encontrados
                    cont_cycle_tipo1 += 1
            #Inicialización de variable para la obtención de promedio de tiempo de espera
            average_time_s = 0.0
            #Sumatoria del tiempo de espera
            for i in range(len(list_tiempoEspera)):
                average_time_s += float(list_tiempoEspera[i])
            #obtencion del tiempo promedio de espera
            average_time_s = round(average_time_s / len(list_tiempoEspera))
            #impresión de tiempo promedio
            print("Tiempo promedio en zonas de espera:" + str(timedelta(seconds=average_time_s)))
            #Calculo de porcentajes de ciclos de faena que incluyeron trabajos tipo2
            porcentajeDeCiclosTipo2 = (cont_cycle_tipo2 * 100) / len(data)
            #Despliegue de porcentaje de ciclos
            print("porcentaje de ciclos en zonas de trabajo de tipo 2 (AW2 y BW2):" + str(
                round(porcentajeDeCiclosTipo2, 2)) + "%")
            # Calculo de porcentajes de ciclos de faena que incluyeron trabajos tipo1
            porcentajeDeCiclosTipo1 = (cont_cycle_tipo1 * 100) / len(data)
            # Despliegue de porcentaje de ciclos
            print("porcentaje de ciclos en zonas de trabajo de tipo 1 (AW1 y BW1):" + str(
                round(porcentajeDeCiclosTipo1, 2)) + "%")

    except(Exception):
        print("ERROR:"+Exception)


