from sodapy import Socrata
import pandas as pd

 # Unauthenticated client only works with public data sets . Note ’None ’
 # in place of application token , and no username or password :
client = Socrata ("www.datos.gov.co", None )

# Example authenticated client ( needed for non - public datasets ):
# client = Socrata (www. datos .gov.co ,
# MyAppToken ,
# userame =" user@example . com" ,
# password =" AFakePassword ")

# First 2000 results , returned as JSON from API / converted to Python list of
# dictionaries by sodapy .

def func(nombre_departamento, limite_registros):
    results = client.get("gt2j-8ykr", limit = limite_registros , departamento = nombre_departamento )
    dataframe = pd.DataFrame.from_records( results )
    return results, dataframe