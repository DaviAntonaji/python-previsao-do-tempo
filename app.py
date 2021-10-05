from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

import os
import sys
from dotenv import load_dotenv
load_dotenv()

chave = os.getenv("KEY")

owm = OWM(chave)
mgr = owm.weather_manager()

if len(sys.argv) != 3:
    print("Use: python3 app.py <cidade> <país>")
else:
    cidade = sys.argv[1]
    pais = sys.argv[2].upper()

    lista_paises = ["BR"]
    if pais in lista_paises:

        observation = mgr.weather_at_place(cidade + ',' + pais)
        w = observation.weather

        print("Status:", w.detailed_status)         
        print("Vento:",w.wind())                  
        print("Chuva:",w.rain)                   
        print("Índice de calor:",w.heat_index)              
        print("Nuvens:",w.clouds)                  
    else:
        print("País invalido.")