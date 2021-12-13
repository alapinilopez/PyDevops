## Función para comprobar que se han creado los archivos markdown ##
def check_file_exists(file_path):
    try:
        with open(file_path, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False