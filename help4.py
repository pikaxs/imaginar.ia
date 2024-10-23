import requests
import os
from openai import OpenAI

# Inicializa el cliente de OpenAI
client = OpenAI()

# Especifica la carpeta donde deseas guardar las imágenes
output_folder = 'carpeta_imagenes'
os.makedirs(output_folder, exist_ok=True)

# Número de imágenes a generar
num_images = 3

# Itera para generar múltiples imágenes
for i in range(num_images):
    # Genera una imagen
    response = client.images.generate(
        model="dall-e-3",
        prompt="a white siamese cat",
        size="1024x1024",
        quality="standard",
        n=1,  # Debe ser 1 para este modelo
    )

    # Obtén la URL de la imagen generada
    image_url = response.data[0].url
    image_name = f"gato_siamese_blanco_{i+1}.png"  # Nombre de archivo único para cada imagen
    output_path = os.path.join(output_folder, image_name)

    # Descarga y guarda la imagen
    image_response = requests.get(image_url)
    
    if image_response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(image_response.content)
        print(f"Imagen {i+1} guardada en: {output_path}")
    else:
        print(f"Error al descargar la imagen {i+1}.")

