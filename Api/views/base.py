import json
import os
from django.http import JsonResponse

class BaseApiView:
    json_file_path = os.path.join(os.path.dirname(__file__), '..', 'json', 'products.json')

    @staticmethod
    def read_json():
        """Lee los datos del archivo JSON."""
        with open(BaseApiView.json_file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def write_json(data):
        """Escribe los datos en el archivo JSON."""
        with open(BaseApiView.json_file_path, 'w') as file:
            json.dump(data, file, indent=4)
