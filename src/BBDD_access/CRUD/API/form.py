from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

import json

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SPREADSHEET_ID = '1_J8Z8ZuWjMYmV7565dSG_pEWt6Ao99wuyLd31W-bsno'

def main(RANGE_NAME):

    ## configuración del token de acceso a la API de Gooogle Sheet ##
    
    creds = None
    if os.path.exists('token.json'):
    # El archivo token.json almacena los tokens de actualización y de acceso del usuario, y se crea automáticamente cuando se autoriza por primera vez.
    # El fichero credentials.json lo hemos descargado mediante la consola de Google Cloud
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid: # Si no hay credenciales (válidas) disponibles, permita que el usuario inicie sesión.
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Guarda las credenciales para la próxima vez que se ejecute
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


    ## Petición de los datos a la API ##

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()

    request = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME)
    response = request.execute()
    values = response["values"]

    if not values:
        print('No hay datos registrados')
    else:
        # Segun nuestra estructura de la BBDD: las llaves de los documentos no cambian, por tanto solo importamos los valores
        # La ultima fila tiene la entrada del formulario mas reciente, por tanto, los valores que utilizaremos para hacer CRUD
        lastRowValues = values[-1]

        return lastRowValues
