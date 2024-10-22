from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .base import BaseApiView

@method_decorator(csrf_exempt, name='dispatch')
class ProductApiView(BaseApiView, View):

    def get(self, request, *args, **kwargs):
        """Devuelve la lista de productos o un producto específico por ID."""
        products = self.read_json()
        product_id = kwargs.get('id')

        if product_id:
            product = next((p for p in products if p['id'] == product_id), None)
            if not product:
                return JsonResponse({'error': 'Producto no encontrado'}, status=404)
            return JsonResponse(product)
        return JsonResponse(products, safe=False)

    def post(self, request, *args, **kwargs):
        new_product = json.loads(request.body)
        data = self.read_json()

        # Encontrar el mayor ID actual en los productos y autoincrementar el ID
        if data:
            max_id = max(product['id'] for product in data)
            new_product['id'] = max_id + 1
        else:
            new_product['id'] = 1  # Si no hay productos, asignar el primer ID como 1
        
        new_product['is_active'] = True

        data.append(new_product)
        self.write_json(data)
        return JsonResponse(new_product, status=201)

    def put(self, request, *args, **kwargs):
        # Obtener el ID del producto de la URL
        product_id = int(kwargs.get('id'))  # Asegúrate de que `id` esté en la URL
        updated_product = json.loads(request.body)
        
        # Leer los datos existentes
        data = self.read_json()

        # Buscar y actualizar el producto correspondiente
        for product in data:
            if product['id'] == product_id:
                product.update(updated_product)  # Actualizar el producto
                break
        else:
            return JsonResponse({"error": "Product not found."}, status=404)

        # Guardar los cambios en el archivo JSON
        self.write_json(data)

        return JsonResponse({"message": "Product updated successfully.", "product": product})

    def delete(self, request, *args, **kwargs):
        # Obtener el ID del producto de la URL
        product_id = int(kwargs.get('id'))

        # Leer los datos existentes
        data = self.read_json()

        # Buscar y eliminar el producto correspondiente
        for product in data:
            if product['id'] == product_id:
                data.remove(product)  # Eliminar el producto
                break
        else:
            return JsonResponse({"error": "Product not found."}, status=404)

        # Guardar los cambios en el archivo JSON
        self.write_json(data)

        return JsonResponse({"message": "Product deleted successfully."})