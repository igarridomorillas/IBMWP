#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
import ssl


# OPTION CARDS

my_json = [
  {
    "option" : "Inicio",
    "cards" : [
      {
        "id" : 1,
        "description" : "Con concha.", # Mollusca
        "image" : ""
      },
      {
        "id" : 2,
        "description" : "Sin concha.",
        "image" : ""
      }
    ]
  },
  {
    "option" : "Sin concha.",
    "cards" : [
      {
        "id" : 3,
        "description" : "Con patas.",
        "image" : ""
      },
      {
        "id" : 4,
        "description" : "Sin patas.",
        "image" : ""
      }
    ]
  },
   {
    "option" : "Sin patas",
    "cards" : [
      {
        "id" : 5,
        "description" : "Con colas y protuberancias.", # Diptera
        "image" : ""
      },
      {
        "id" : 6,
        "description" : "Forma de gusano, sin estas caracteristicas.", # Oligochaeta
        "image" : ""
      }
    ]
  },
  {
    "option" : "Con patas.",
    "cards" : [
      {
        "id" : 7,
        "description" : "Seis patas.", 
        "image" : ""
      },
      {
        "id" : 8,
        "description" : "Ocho patas.", # Arachnida
        "image" : ""
      },
      {
        "id" : 9,
        "description" : "Diez o más patas.", # Crustacea
        "image" : ""
      }
    ]
  },
  {
    "option" : "Seis patas.",
    "cards" : [
      {
        "id" : 10,
        "description" : "Constructores de casas. Con dos ganchos terminales.", # Trichoptera
        "image" : ""
      },
      {
        "id" : 11,
        "description" : "Sin estas características.",
        "image" : ""
      }
    ]
  },
  {
    "option" : "Sin estas características.",
    "cards" : [
      {
        "id" : 12,
        "description" : "Colas y antenas largas.",
        "image" : ""
      },
      {
        "id" : 13,
        "description" : "Colas y antenas cortas.",
        "image" : ""
      }
    ]
  },
  {
    "option" : "Colas y antenas largas.",
    "cards" : [
      {
        "id" : 14,
        "description" : "Dos o tres cercos terminales. Una uña Tarsal. Branquias abdominales.", # Ephemeroptera
        "image" : ""
      },
      {
        "id" : 15,
        "description" : "Dos cercos abdominales. Dos uñas tarsales. Sin branquias abdominales.", # Plecoptera
        "image" : ""
      }
    ]
  },
  {
    "option" : "Colas y antenas cortas.",
    "cards" : [
      {
        "id" : 16,
        "description" : "Mandibulas bien desarrolladas.",
       "image" : ""
      },
      {
        "id" : 17,
        "description" : "Pseudópodos abdominales.", # Lepidoptera
        "image" : ""
      },
      {
        "id" : 18,
        "description" : "Piezas bucales en estilete.", # Hemiptera
        "image" : ""
      }
    ]
  },
  {
    "option" : "Mandibulas bien desarrolladas.",
    "cards" : [
      {
        "id" : 19,
        "description" : "Prolongaciones laterales. Dos uñas tarsales.", # Megaloptera
        "image" : ""
      },
      {
        "id" : 20,
        "description" : "Mandibulas prolongables.", # Odonata
        "image" : ""
      },
      {
        "id" : 21,
        "description" : "Antenas con mas de tres segmentos. Tarso generalmente con uña.", # Coleoptera
        "image" : ""
      }
    ]
  },
]


# MACROINVERTEBRATES

macroinvertebrates = [
  {
    "name" : "oligochaeta",
    "id" : 1000,
    "index" : 1,
    "description" : "Subclase del filo Annelida (anélidos o gusanos segmentados), clase Clitellata (que poseen un clitelo o 'collar' que forma un capullo reproductivo)",
    "tolerance" : "alta"
  },
  {
    "name" :"mollusca",
    "id" : 1001,
    "index" : 3,
    "description" : "Invertebrados protóstomos celomados, triblásticos de simetría bilateral no segmentados, de cuerpo blando, desnudo o protegido por una concha",
    "tolerance" : "alta"
  },
  {
    "name" :"crustacea",
    "id" : 1002,
    "index" : 6,
    "description" : "Subfilo de artrópodos fundamentalmente acuáticosdos con pares de antenas. Tienen al menos un par de maxilas y pasan por periodos de muda e intermuda para poder crecer",
    "tolerance" : "media"
  },
  {
    "name" :"arachnida",
    "id" : 1003,
    "index" : 4,
    "description" : "Artrópodos quelicerados. El cuerpo posee dos regiones o Tagmas más o menos diferenciados, el prosoma (o cefalotórax) y el opistosoma (o abdomen). Los apéndices se insertan en el prosoma y son un par de quelíceros, junto a la boca, un par de pedipalpos, a veces muy desarrollados y cuatro pares de patas locomotoras. Carecen de antenas,​ y suelen tener uno o más pares de ojos simples, en lugar de grandes ojos compuestos como los insectos",
    "tolerance" : "media"
  },
  {
    "name" :"diptera",
    "id" : 1004,
    "index" : 4, 
    "description" : "Insectos neópteros caracterizados porque sus alas posteriores se han reducido a halterios. larvas acuáticas, con cabeza esclerotizada formando una cápsula cefálica que puede estar reducida a ganchos bucales. La cápsula cefálica de los braquíceros, por otra parte, es blanda y gelatinosa. Los escleritos pueden estar ausentes o muy reducidos. Muchas de estas larvas pueden retraer la cabeza dentro del tórax",
    "tolerance" : "media"
  },
  {
    "name" : "trichoptera",
    "id" : 1005,
    "index" : 10,
    "description" : "Insectos endopterigotos (con metamorfosis completa), emparentados con los lepidópteros (mariposas y polillas), cuyas larvas y pupas son acuáticas, y viven dentro de pequeños estuches en forma de tubo que ellas mismas fabrican a base de seda a la que adhieren granos de arena, restos vegetales, etc.",
    "tolerance" : "baja"
  },
  {
    "name" : "ephemeroptera",
    "id" : 1006,
    "index" : 8,
    "description" : "Insectos pterigotos hemimetábolos acuáticos. Sus etapas inmaduras son formas acuáticas de agua dulce, de tipo campodeiforme,​ con patas y antenas bien desarrolladas, con un cuerpo alargado cilíndrico o algo aplanado; pasa por una serie de estadios, mudando y aumentando de tamaño cada vez",
    "tolerance" : "baja"
  },    
  {
    "name" : "plecoptera",
    "id" : 1007,
    "index" : 10,
    "description" : "Insectos neópteros. Ninfas acuáticas, viven en la zona más profunda de lagos y arroyos. Las ninfas de los plecópteros son cazadores de otros artrópodos acuáticos o comedores de vegetales. Algunos buscan alimento incluso las algas bénticas",
    "tolerance" : "baja"
  },
  {
    "name" : "lepidoptera",
    "id" : 1008,
    "index" : 4,
    "description" : "Insectos holometábolos. Sus larvas son vermiformes, y poseen una serie de 5 patas falsas al final del abdomen",
    "tolerance" : "media"
  },      
  {
    "name" : "hemiptera",
    "id" : 1009,
    "index" : 3,
    "description" : "Insectos neópteros. Piezas bucales modificadas formando una estructura en forma de pico denominada rostro adaptado para perforar y succionar líquidos de plantas (como savia) y animales (por ejemplo, sangre). En el rostro, las mandíbulas y las maxilas tienen forma de aguja y están envueltas por el labio; todo el conjunto está normalmente plegado en la parte ventral del cuerpo cuando no se utiliza",
    "tolerance" : "alta"
  }, 
  {
    "name" : "megaloptera",
    "id" : 1010,
    "index" : 5,
    "description" : "Insectos endopterigotos de grandes alas con venación ornamentada; sus larvas son acuáticas, llegando a ser las más grandes entre los insectos.",
    "tolerance" : "media"
  },
  {
    "name" : "odonata",
    "id" : 1011,
    "index" : 8,
    "description" : "Insectos con ninfas acuaticas. Las ninfas tienen la cabeza pentagonal o rectangular, provista de un par de grandes ojos compuestos, tres ocelos y un par de cortas antenas. Su principal característica es su aparto bucal: el labio está muy modificado formando la máscara, un dispositivo que mantiene plegado bajo la cabeza y que proyecta adelante de manera repentina para capturar las presas. El tórax es similar al del adulto, pero sólo lleva unos esbozos de alas. El abdomen puede llevar tres láminas branquiales apicales",
    "tolerance" : "baja"
  },
  {
    "name" : "coleoptera",
    "id" : 1012,
    "index" : 4,
    "description" : "Insectos con piezas bucales de tipo masticador, y las alas delanteras (primer par de alas) transformadas en rígidas armaduras, llamadas élitros, que protegen la parte posterior del tórax, incluido el segundo par de alas, y el abdomen. Los élitros no se usan para el vuelo, pero deben (en la mayoría de las especies) ser levantadas para poder usar las alas traseras. Cuando se posan, las alas traseras se guardan debajo de los élitros",
    "tolerance" : "media"
  },
]


# print ("\nCLAVE DICOTÓMICA\n\n1: Con concha\n2: Sin concha") #### my_json[].cards
# opc1 = int(input("\n\tIntroduzca 1 / 2: "))
    #if opc1 == 1:  #### macroinvertebrates[].name
    # grupo = ("MOLLUSCA")

# Sin concha(opc1) 
    #elif opc1 == 2: #### my_json[].cards
    #  print ("\n1: Con patas\n2: Sin patas")
    #  opc2 = int(input("\n\tIntroduzca 1 / 2: "))



class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):   # http://localhost:4443/?camino=con-concha,con-patas
        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # ---

        parametros_str=parsed_path.query

        parametros_arr=parametros_str.split("=")

        camino=parametros_arr[1].split(",")

        print(camino)

        self.wfile.write(json.dumps(my_json).encode())

        # --
        return

def run(host='localhost', port=4443):
    #server = HTTPServer((host, port), RequestHandler)
    # To generate key and cert files with OpenSSL use following command:
    # openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365
    server = HTTPServer((host, port), RequestHandler)

    print('Starting server at http://'+host+':'+str(port))
    server.serve_forever()


if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()