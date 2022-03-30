import requests
import json
import pandas as pd
import sys
import codecs

#:

def proceso():
    url  = 'https://arclim.mma.gob.cl/media//FeatureSets/comunas//clima/amenazas_comunas_annual.geojson'
    response = requests.get(url)
    decoded_data=codecs.decode(response.content, 'utf-8-sig')
    d = json.loads(decoded_data)
    out_file = open("Comunal/amenazas_comunas_annual.geojson", "w")    
    json.dump(d, out_file, indent = 1)         
    out_file.close()   

if __name__ == '__main__':    
    try:
        proceso()
    except:
        error = sys.exc_info()[1]
        print(error)
    
