import requests
from bs4 import BeautifulSoup

url = "https://es.wikipedia.org/wiki/Bogotazo"

page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')
else:
    raise ValueError("Error al cargar la pagina, verficar la URL e intentar de nuevo")

def title_extractor():
    title = soup.find('span', class_='mw-page-title-main')
    return title.get_text()

def section_extractor():
    content = soup.find_all('h2')
    sections = [section.get_text() for section in content]
    return sections

def paragraph_extractor(selected_sections):
    paragraphs = []
    current_section = None
    for e in soup.find_all(['h2','p','dl']):
        if e.name == 'h2':  
            current_section = e.get_text()
        if current_section in selected_sections:
            if e.name == 'p':  
                paragraphs.append(e.get_text())
            elif e.name == 'dl':  
                dd = e.find('dd')
                if dd:
                    quote = dd.find('i')
                    if quote:
                        paragraphs.append(quote.get_text())
    return paragraphs

#PROGRAMA PRINCIPAL

if __name__ == "__main__":

    
    title = title_extractor()
    print(f"Título: {title}\n")

    
    sections = section_extractor()
    print("Secciones disponibles:")
    for i, section in enumerate(sections):
        print(f"{i+1}. {section}")

   
    selected_indices = input("Selecciona las secciones por número (separadas por comas): ")
    selected_sections = [sections[int(i)-1] for i in selected_indices.split(",")]



    paragraphs = paragraph_extractor(selected_sections)
    print("\nPárrafos seleccionados:\n")
    for para in paragraphs:
        print(para)
        print("\n---\n")