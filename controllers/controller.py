# ---------------------------- DATA CONTROLLER ------------------------------------


def get_data(url):
        """ Extrae los datos contenidos en un archivo .txt
            Retorna un diccionario

        Parameters
        ----------
        filename: str --> ruta del archivo
        """
        folder = "./data/ica-" + url + ".txt"
        data = []
        with open(str(folder), "r") as file:
            for line in file:                
                data.append(float(line))
        return data
