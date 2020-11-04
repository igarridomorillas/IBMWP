# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
Programa IBMWP

@author: Yanira Fernandez Requena


"""

import math as mt

# MENU
menu = 1
while menu != 5:
    print ("\nMENU\n\n1: Clave Dicotomica:\n\tClave para la identificacion de macroinvertebrados acuaticos\n\n2: Indice Macroinvertebrados:\n\tDescripcion de los macroinvertebrados identificados en la clave\n\n3: Calculo IBMWP:\n\tCalculo del indice IBMWP en la muestra estudiada\n\n4: Media IBMWP\n\tCalculo de la media, varianza y desviacion estandar del IBWMP para un conjunto de muestras\n\t\n5: Salir")    
    menu = int(input("\n\tIntroduzca 1 / 2 / 3 / 4 / 5: "))
 
    
    # MUESTRAS
    if menu == 4:
        print ("\nMEDIA IBMWP")
        # Entradas
        listram = []
        ntram = (int(input("\nNumero de muestras estudiadas: ")))
        print ("\nIndice IBMWP en cada muestra:")
        for k in range (ntram):
            listram.append(int(input("\tMuestra {}: ".format(k + 1))))
            
        # Operaciones
            #Media
        sumtram = 0
        for k in listram:
            sumtram += k
        
        media = sumtram / ntram
        
            # Varianza
        listvar = []
        for y in listram:
            listvar.append((media - y) ** 2)
        sumvar = 0
        for z in listvar:
            sumvar += z
        varianza = sumvar / ntram
        
            #Desviacion estandar
        desvest = mt.sqrt(varianza)
        
        if media > 100:
            calidad = ("Muy Buena. Aguas muy limpias, no contaminadas ni alteradas de forma apreciable")
        elif media <= 100 and media > 60:
            calidad = ("Aceptable. Aguas con algún signo evidente de contaminación")
        elif media <=60 and media > 35:
            calidad = ("Dudosa. Aguas claramente contaminadas")
        elif media <= 35 and media > 15:
            calidad = ("Critica. Aguas muy contaminadas")
        elif media <= 15:
            calidad = ("Muy Critica. Aguas fuertemente contaminadas")
        # Salidas
        print ("\nRESULTADOS:\n\tMedia: {}\n\tVarianza: {}\n\tDesviacion estandar: {}\n\nCalidad del agua: {}".format(media, varianza, desvest, calidad))


    # CALCULO IBMWP
    elif menu == 3:
        # Entradas
        invertebrados = {
        "OLIGOCHAETA": 1,
        "MOLLUSCA": 3,
        "CRUSTACEA": 6,
        "ARACHNIDA": 4,
        "DIPTERA": 4,
        "TRICHOPTERA": 10,
        "EPEMEROPTERA": 8,
        "PLECOPTERA": 10,
        "LEPIDOPTERA": 4,      
        "HEMIPTERA": 3, 
        "MEGALOPTERA": 5,      
        "ODONATA": 8,
        "COLEOPTERA": 4,}
        print ("\nCALCULO DEL INDICE IBMWP\n\nIntroduzca el numero de individuos de cada grupo encontrados en la muestra:\n")
        
        # Operaciones
        for k in invertebrados.keys():
            x = int(input("Numero de {}:\t".format(k)))
            invertebrados[k] = invertebrados[k] * x
        
        IBMWP = sum(invertebrados.values())
        
        if IBMWP > 100:
            calidad = ("Muy Buena")
        elif IBMWP <= 100 and IBMWP > 60:
            calidad = ("Aceptable")
        elif IBMWP <=60 and IBMWP > 35:
            calidad = ("Dudosa")
        elif IBMWP <= 35 and IBMWP > 15:
            calidad = ("Critica")
        elif IBMWP <= 15:
            calidad = ("Muy Critica")
        
        # Salidas
        print ("\nINDICE IBMWP: {}\n\nCALIDAD DEL AGUA: {}".format(IBMWP,calidad))

    elif menu == 2:
        print ("\nINDICE DE MACROINVERTEBRADOS")
        # Diccionario
        inv = {
        "OLIGOCHAETA": [1, "Subclase del filo Annelida (anélidos o gusanos segmentados), clase Clitellata (que poseen un clitelo o 'collar' que forma un capullo reproductivo)", "Alta"],
        "MOLLUSCA": [3, "Invertebrados protóstomos celomados, triblásticos de simetría bilateral no segmentados, de cuerpo blando, desnudo o protegido por una concha", "Alta"],
        "CRUSTACEA": [6, "Subfilo de artrópodos fundamentalmente acuáticosdos con pares de antenas. Tienen al menos un par de maxilas y pasan por periodos de muda e intermuda para poder crecer", "Media"],
        "ARACHNIDA": [4, "Artrópodos quelicerados. El cuerpo posee dos regiones o Tagmas más o menos diferenciados, el prosoma (o cefalotórax) y el opistosoma (o abdomen). Los apéndices se insertan en el prosoma y son un par de quelíceros, junto a la boca, un par de pedipalpos, a veces muy desarrollados y cuatro pares de patas locomotoras. Carecen de antenas,​ y suelen tener uno o más pares de ojos simples, en lugar de grandes ojos compuestos como los insectos", "Media"],
        "DIPTERA": [4, "Insectos neópteros caracterizados porque sus alas posteriores se han reducido a halterios. larvas acuáticas, con cabeza esclerotizada formando una cápsula cefálica que puede estar reducida a ganchos bucales. La cápsula cefálica de los braquíceros, por otra parte, es blanda y gelatinosa. Los escleritos pueden estar ausentes o muy reducidos. Muchas de estas larvas pueden retraer la cabeza dentro del tórax", "Media"],
        "TRICHOPTERA": [10, "Insectos endopterigotos (con metamorfosis completa), emparentados con los lepidópteros (mariposas y polillas), cuyas larvas y pupas son acuáticas, y viven dentro de pequeños estuches en forma de tubo que ellas mismas fabrican a base de seda a la que adhieren granos de arena, restos vegetales, etc.", "Baja"],
        "EPHEMEROPTERA": [8, "Insectos pterigotos hemimetábolos acuáticos. Sus etapas inmaduras son formas acuáticas de agua dulce, de tipo campodeiforme,​ con patas y antenas bien desarrolladas, con un cuerpo alargado cilíndrico o algo aplanado; pasa por una serie de estadios, mudando y aumentando de tamaño cada vez", "Baja"],    
        "PLECOPTERA": [10, "Insectos neópteros. Ninfas acuáticas, viven en la zona más profunda de lagos y arroyos. Las ninfas de los plecópteros son cazadores de otros artrópodos acuáticos o comedores de vegetales. Algunos buscan alimento incluso las algas bénticas", "Baja"],
        "LEPIDOPTERA": [4, "Insectos holometábolos. Sus larvas son vermiformes, y poseen una serie de 5 patas falsas al final del abdomen", "Media"],      
        "HEMIPTERA": [3, "Insectos neópteros. Piezas bucales modificadas formando una estructura en forma de pico denominada rostro adaptado para perforar y succionar líquidos de plantas (como savia) y animales (por ejemplo, sangre). En el rostro, las mandíbulas y las maxilas tienen forma de aguja y están envueltas por el labio; todo el conjunto está normalmente plegado en la parte ventral del cuerpo cuando no se utiliza", "Alta"], 
        "MEGALOPTERA": [5, "Insectos endopterigotos de grandes alas con venación ornamentada; sus larvas son acuáticas, llegando a ser las más grandes entre los insectos.", "Media"],
        "ODONATA": [8, "Insectos con ninfas acuaticas. Las ninfas tienen la cabeza pentagonal o rectangular, provista de un par de grandes ojos compuestos, tres ocelos y un par de cortas antenas. Su principal característica es su aparto bucal: el labio está muy modificado formando la máscara, un dispositivo que mantiene plegado bajo la cabeza y que proyecta adelante de manera repentina para capturar las presas. El tórax es similar al del adulto, pero sólo lleva unos esbozos de alas. El abdomen puede llevar tres láminas branquiales apicales", "Baja"],
        "COLEOPTERA": [4, "Insectos con piezas bucales de tipo masticador, y las alas delanteras (primer par de alas) transformadas en rígidas armaduras, llamadas élitros, que protegen la parte posterior del tórax, incluido el segundo par de alas, y el abdomen. Los élitros no se usan para el vuelo, pero deben (en la mayoría de las especies) ser levantadas para poder usar las alas traseras. Cuando se posan, las alas traseras se guardan debajo de los élitros", "Media"],
        }
        an = (input("\nIntroduzca el nombre del grupo, tal como aparece en la clave:\n\n")).upper()
        
        # Salidas
        print ("\nCARACTERISTICAS : {}\n\nTolerancia a la contaminacion: {}\tValor IBMWP: {}".format(inv[an][1],inv[an][2],inv[an][0]))

    # CLAVE
    elif menu == 1:
        print ("\nCLAVE DICOTÓMICA\n\n1: Con concha\n2: Sin concha")
        opc1 = int(input("\n\tIntroduzca 1 / 2: ")) 
        
        # Con concha (opc1)
        if opc1 == 1:
            grupo = ("MOLLUSCA")
            
        # Sin concha(opc1)
        elif opc1 == 2:
            print ("\n1: Con patas\n2: Sin patas")
            opc2 = int(input("\n\tIntroduzca 1 / 2: "))
            
            # Con Patas (opc2)
            if opc2 == 1:
                print ("\n1: Seis patas\n2: Ocho patas\n3: Diez o más patas")
                opc3 = int(input("\n\tIntroduzca 1 / 2 / 3: "))
                
                # 6 patas (opc3)
                if opc3 == 1:
                    print ("\nINSECTA\n\n1: Constructores de casas. Con dos ganchos terminales\n2: Sin estas características")
                    opc4 = int(input("\n\tIntroduzca 1 / 2: "))
                    
                    # Casas (opc4)
                    if opc4 == 1:
                        grupo = ("TRICHOPTERA")
                    
                    # Sin casas (opc4)
                    elif opc4 == 2:
                        print ("\n1: Con colas y antenas largas\n2: Colas y antenas cortas")
                        opc5 = int(input("\n\tIntroduzca 1 / 2: "))
                        
                        # Antenas largas (opc5)
                        if opc5 == 1:
                            print ("\n1: Dos o tres cercos terminales. Una uña Tarsal. Branquias abdominales\n2: Dos cercos abdominales. Dos uñas tarsales. Sin branquias abdominales")
                            if opc5 == 1:
                                grupo = ("EPEMEROPTERA")
                            elif opc5 == 2:
                                grupo = ("PLECOPTERA")
                        
                        # Antenas cortas (opc5)
                        elif opc5 == 2:
                            print ("\n1: Mandibulas bien desarrolladas\n2: Pseudópodos abdominales\n3: Piezas bucales en estilete")
                            opc6 = int(input("\n\tIntroduzca 1 / 2 / 3 / 4: "))
                            
                            # Mandíbulas no desarrolladas (opc6)
                            if opc6 == 2:
                                grupo = ("LEPIDOPTERA")    
                            elif opc6 == 3:
                                grupo = ("HEMIPTERA")
                            
                            # Mandíbulas desarrolladas (opc6)
                            elif opc6 == 1:
                                print ("\n1: Prolongaciones laterales. Dos uñas tarsales\n2: Mandibulas prolongables\n3: Antenas con mas de tres segmentos. Tarso generalmente con uña.")
                                opc7 = int(input("\n\tIntroduzca 1 / 2 / 3: "))
                                if opc7 == 1:
                                    grupo = ("MEGALOPTERA")
                                elif opc7 == 2:
                                    grupo = ("ODONATA")
                                elif opc7 == 3:
                                    grupo = ("COLEOPTERA")
                            
                # Mas de 6 patas (opc3)           
                elif opc3 == 2:
                    grupo = ("ARACHNIDA")
                elif opc3 == 3:
                    grupo = ("CRUSTACEA")
                
            # Sin patas (opc2)
            elif opc2 == 2:
                print ("\n1: Con colas y protuberancias\n2: Forma de gusano, sin estas caracteristicas")
                opc8 = int(input("\n\tIntroduzca 1 / 2: "))
                if opc8 == 1:
                    grupo = ("DIPTERA")
                elif opc8 == 2:
                    grupo = ("OLIGOCHAETA")
        
        # Resultado Clave          
        print ("\nGrupo al que pertenece el organismo:\n\n\t{}".format(grupo))
   
    # ERROR
    elif menu == 5:
        print ("FIN")
    else:
        print ("\nERROR: Por favor, introduzca un numero del 1 al 5")