#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
import ssl


# OPTION CARDS

my_json = [
  {
    "option" : "Inicio",
    "cards" : {
      "1" : {
        "id" : 1,
        "choice" : 0,
        "description" : "Con concha.", # Mollusca
        "image" : "",
        "next" : "mollusca"
      },
      "2" : {
        "id" : 2,
        "choice" : 0,
        "description" : "Sin concha.",
        "image" : "",
        "next" : 1
      }
    }
  },
  {
    "option" : "Sin concha.",
    "cards" : {
      "3" : {
        "id" : 3,
        "choice" : 1,
        "description" : "Con patas.",
        "image" : "",
        "next" : 3
      },
      "4" : {
        "id" : 4,
        "choice" : 1,
        "description" : "Sin patas.",
        "image" : "",
        "next" : 2
      }
    }
  },
   {
    "option" : "Sin patas",
    "cards" : {
      "5" : {
        "id" : 5,
        "choice" : 2,
        "description" : "Con colas y protuberancias.", # Diptera
        "image" : "",
        "next" : "diptera"
      },
      "6" : {
        "id" : 6,
        "choice" : 2,
        "description" : "Forma de gusano, sin estas caracteristicas.", # Oligochaeta
        "image" : "",
        "next" : "oligochaeta"
      }
    }
  },
  {
    "option" : "Con patas.",
    "cards" : {
      "7" : {
        "id" : 7,
        "choice" : 3,
        "description" : "Seis patas.", 
        "image" : "",
        "next" : 4
      },
      "8" : {
        "id" : 8,
        "choice" : 3,
        "description" : "Ocho patas.", # Arachnida
        "image" : "",
        "next" : "arachnida"
      },
      "9" : {
        "id" : 9,
        "choice" : 3,
        "description" : "Diez o más patas.", # Crustacea
        "image" : "",
        "next" : "crustacea"
      }
    }
  },
  {
    "option" : "Seis patas.",
    "cards" : {
      "10" : {
        "id" : 10,
        "choice" : 4,
        "description" : "Constructores de casas. Con dos ganchos terminales.", # Trichoptera
        "image" : "",
        "next" : "trichoptera"
      },
      "11" : {
        "id" : 11,
        "choice" : 4,
        "description" : "Sin estas características.",
        "image" : "",
        "next" : 5
      }
    }
  },
  {
    "option" : "Sin estas características.",
    "cards" : {
      "12" : {
        "id" : 12,
        "choice" : 5,
        "description" : "Colas y antenas largas.",
        "image" : "",
        "next" : 6
      },
      "13" : {
        "id" : 13,
        "choice" : 5,
        "description" : "Colas y antenas cortas.",
        "image" : "",
        "next" : 7
      }
    }
  },
  {
    "option" : "Colas y antenas largas.",
    "cards" : {
      "14" : {
        "id" : 14,
        "choice" : 6,
        "description" : "Dos o tres cercos terminales. Una uña Tarsal. Branquias abdominales.", # Ephemeroptera
        "image" : "",
        "next" : "ephemeroptera"
      },
      "15" : {
        "id" : 15,
        "choice" : 6,
        "description" : "Dos cercos abdominales. Dos uñas tarsales. Sin branquias abdominales.", # Plecoptera
        "image" : "",
        "next" : "plecoptera"
      }
    }
  },
  {
    "option" : "Colas y antenas cortas.",
    "cards" : {
      "16" : {
        "id" : 16,
        "choice" : 7,
        "description" : "Mandibulas bien desarrolladas.",
       "image" : "",
        "next" : 8
      },
      "17" : {
        "id" : 17,
        "choice" : 7,
        "description" : "Pseudópodos abdominales.", # Lepidoptera
        "image" : "",
        "next" : "lepidoptera"
      },
      "18" : {
        "id" : 18,
        "choice" : 7,
        "description" : "Piezas bucales en estilete.", # Hemiptera
        "image" : "",
        "next" : "hemiptera"
      }
    }
  },
  {
    "option" : "Mandíbulas bien desarrolladas.",
    "cards" : {
      "19":{
        "id" : 19,
        "choice" : 8,
        "description" : "Prolongaciones laterales. Dos uñas tarsales.", # Megaloptera
        "image" : "",
        "next" : "megaloptera"
      },
      "20":{
        "id" : 20,
        "choice" : 8,
        "description" : "Mandíbulas prolongables.", # Odonata
        "image" : "",
        "next" : "odonata"
      },
      "21":{
        "id" : 21,
        "choice" : 8,
        "description" : "Antenas con mas de tres segmentos. Tarso generalmente con uña.", # Coleoptera
        "image" : "",
        "next" : "coleoptera"
      }
    }
  },
]


# MACROINVERTEBRATES

macroinvertebrates = {
  "oligochaeta" : {
    "name" : "oligochaeta",
    "id" : 1000,
    "index" : 1,
    "description" : "Subclase del filo Annelida (anélidos o gusanos segmentados), clase Clitellata (que poseen un clitelo o 'collar' que forma un capullo reproductivo)",
    "tolerance" : "alta"
  },
  "mollusca": {
    "name" :"mollusca",
    "id" : 1001,
    "index" : 3,
    "description" : "Invertebrados protóstomos celomados, triblásticos de simetría bilateral no segmentados, de cuerpo blando, desnudo o protegido por una concha",
    "tolerance" : "alta"
  },
  "crustacea":{
    "name" :"crustacea",
    "id" : 1002,
    "index" : 6,
    "description" : "Subfilo de artrópodos fundamentalmente acuáticosdos con pares de antenas. Tienen al menos un par de maxilas y pasan por periodos de muda e intermuda para poder crecer",
    "tolerance" : "media"
  },
  "arachnida":{
    "name" :"arachnida",
    "id" : 1003,
    "index" : 4,
    "description" : "Artrópodos quelicerados. El cuerpo posee dos regiones o Tagmas más o menos diferenciados, el prosoma (o cefalotórax) y el opistosoma (o abdomen). Los apéndices se insertan en el prosoma y son un par de quelíceros, junto a la boca, un par de pedipalpos, a veces muy desarrollados y cuatro pares de patas locomotoras. Carecen de antenas,​ y suelen tener uno o más pares de ojos simples, en lugar de grandes ojos compuestos como los insectos",
    "tolerance" : "media"
  },
  "diptera":{
    "name" :"diptera",
    "id" : 1004,
    "index" : 4, 
    "description" : "Insectos neópteros caracterizados porque sus alas posteriores se han reducido a halterios. larvas acuáticas, con cabeza esclerotizada formando una cápsula cefálica que puede estar reducida a ganchos bucales. La cápsula cefálica de los braquíceros, por otra parte, es blanda y gelatinosa. Los escleritos pueden estar ausentes o muy reducidos. Muchas de estas larvas pueden retraer la cabeza dentro del tórax",
    "tolerance" : "media"
  },
  "trichoptera":{
    "name" : "trichoptera",
    "id" : 1005,
    "index" : 10,
    "description" : "Insectos endopterigotos (con metamorfosis completa), emparentados con los lepidópteros (mariposas y polillas), cuyas larvas y pupas son acuáticas, y viven dentro de pequeños estuches en forma de tubo que ellas mismas fabrican a base de seda a la que adhieren granos de arena, restos vegetales, etc.",
    "tolerance" : "baja"
  },
  "ephemeroptera":{
    "name" : "ephemeroptera",
    "id" : 1006,
    "index" : 8,
    "description" : "Insectos pterigotos hemimetábolos acuáticos. Sus etapas inmaduras son formas acuáticas de agua dulce, de tipo campodeiforme,​ con patas y antenas bien desarrolladas, con un cuerpo alargado cilíndrico o algo aplanado; pasa por una serie de estadios, mudando y aumentando de tamaño cada vez",
    "tolerance" : "baja"
  },    
  "plecoptera":{
    "name" : "plecoptera",
    "id" : 1007,
    "index" : 10,
    "description" : "Insectos neópteros. Ninfas acuáticas, viven en la zona más profunda de lagos y arroyos. Las ninfas de los plecópteros son cazadores de otros artrópodos acuáticos o comedores de vegetales. Algunos buscan alimento incluso las algas bénticas",
    "tolerance" : "baja"
  },
  "lepidoptera":{
    "name" : "lepidoptera",
    "id" : 1008,
    "index" : 4,
    "description" : "Insectos holometábolos. Sus larvas son vermiformes, y poseen una serie de 5 patas falsas al final del abdomen",
    "tolerance" : "media"
  },      
  "hemiptera":{
    "name" : "hemiptera",
    "id" : 1009,
    "index" : 3,
    "description" : "Insectos neópteros. Piezas bucales modificadas formando una estructura en forma de pico denominada rostro adaptado para perforar y succionar líquidos de plantas (como savia) y animales (por ejemplo, sangre). En el rostro, las mandíbulas y las maxilas tienen forma de aguja y están envueltas por el labio; todo el conjunto está normalmente plegado en la parte ventral del cuerpo cuando no se utiliza",
    "tolerance" : "alta"
  }, 
  "megaloptera":{
    "name" : "megaloptera",
    "id" : 1010,
    "index" : 5,
    "description" : "Insectos endopterigotos de grandes alas con venación ornamentada; sus larvas son acuáticas, llegando a ser las más grandes entre los insectos.",
    "tolerance" : "media"
  },
  "odonata":{
    "name" : "odonata",
    "id" : 1011,
    "index" : 8,
    "description" : "Insectos con ninfas acuaticas. Las ninfas tienen la cabeza pentagonal o rectangular, provista de un par de grandes ojos compuestos, tres ocelos y un par de cortas antenas. Su principal característica es su aparto bucal: el labio está muy modificado formando la máscara, un dispositivo que mantiene plegado bajo la cabeza y que proyecta adelante de manera repentina para capturar las presas. El tórax es similar al del adulto, pero sólo lleva unos esbozos de alas. El abdomen puede llevar tres láminas branquiales apicales",
    "tolerance" : "baja"
  },
  "coleoptera":{
    "name" : "coleoptera",
    "id" : 1012,
    "index" : 4,
    "description" : "Insectos con piezas bucales de tipo masticador, y las alas delanteras (primer par de alas) transformadas en rígidas armaduras, llamadas élitros, que protegen la parte posterior del tórax, incluido el segundo par de alas, y el abdomen. Los élitros no se usan para el vuelo, pero deben (en la mayoría de las especies) ser levantadas para poder usar las alas traseras. Cuando se posan, las alas traseras se guardan debajo de los élitros",
    "tolerance" : "media"
  },
}



class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):   # http://localhost:4443/?qu=0&ans=0
        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # ---  MIRAR FLASK

        parametros_str=parsed_path.query
        array_param = parametros_str.split("&")
        
        if array_param == ['qu=0', 'ans=0']:
            self.wfile.write(json.dumps(my_json[0]).encode())
        elif len(array_param) == 2:
            param_qu = array_param[0].split("=")
            param_ans = array_param[1].split("=")

            qu_id = int(param_qu[1])
            ans_id = param_ans[1]
            choses_qu = my_json[qu_id]

            sel_ans = choses_qu["cards"][ans_id]

            if type(sel_ans["next"]) == int:
                self.wfile.write(json.dumps(my_json[sel_ans["next"]]).encode())
            else:
                self.wfile.write(json.dumps(macroinvertebrates[sel_ans["next"]]).encode())

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