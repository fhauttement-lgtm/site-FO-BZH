import os
from bs4 import BeautifulSoup

# Chemin du dossier contenant vos fichiers HTML
html_dir = "./"
favicon_path = "favicon.ico"

# Parcourir tous les fichiers HTML dans le dossier
for filename in os.listdir(html_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(html_dir, filename)

        # Lire le fichier HTML
        with open(filepath, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file.read(), "html.parser")

        # Vérifier si la balise favicon existe déjà
        favicon_exists = soup.find("link", rel="icon")

        if not favicon_exists:
            # Ajouter la balise favicon dans le <head>
            head = soup.head
            if head:
                new_link = soup.new_tag(
                    "link",
                    rel="icon",
                    href=favicon_path,
                    type="image/x-icon"
                )
                head.append(new_link)

                # Écrire les modifications dans le fichier
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(str(soup))
                print(f"Favicon ajouté à {filename}")
            else:
                print(f"Aucune balise <head> trouvée dans {filename}")
        else:
            print(f"Favicon déjà présent dans {filename}")