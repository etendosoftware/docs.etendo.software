import os
from bs4 import BeautifulSoup
from algoliasearch.search.client import SearchClientSync


# Configure your Algolia app
client = SearchClientSync("XMLZ1ZZEY7", "fcfbff215223081526cae74652f4f884")

# Specify the path to your MkDocs output directory
output_dir = "site"

# Función para leer los archivos HTML y indexarlos
def index_docs(output_dir):
    objects = []

    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    soup = BeautifulSoup(f, "html.parser")

                    # Extraer el contenido relevante del archivo HTML
                    title = soup.title.string if soup.title else ""
                    body_content = soup.get_text(separator=" ", strip=True)

                    # Crear el objeto para Algolia
                    objects.append({
                        "objectID": os.path.relpath(file_path, output_dir),
                        "title": title,
                        "content": body_content,
                        "url": os.path.relpath(file_path, output_dir).replace("\\", "/")
                    })

    # Subir los objetos al índice de Algolia
    if objects:
        client.save_objects(
            index_name= "test",
            objects=objects 
        )
        print(f"{len(objects)} documentos indexados correctamente.")
    else:
        print("No se encontraron documentos HTML para indexar.")


# Index the docs
index_docs(output_dir)
