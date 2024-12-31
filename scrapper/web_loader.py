from bs4 import BeautifulSoup
import requests
import os

def valid_request(url):
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            return {"status": "success", "html": response.text}
        else:
            return {"status": f"error: {response.status_code}", "html": None}
    except requests.exceptions.RequestException as e:
        return {"status": f"error: {e}", "html": None}

url = "https://www.infomoney.com.br/mercados/luiz-barsi-neto-licoes-historias-caso-oi-no-mercado-financeiro/"

result = valid_request(url)

if result["status"] == "success":
    html_content = result["html"]
    soup = BeautifulSoup(html_content, "html.parser")

    content = soup.select_one("article.im-article.clear-fix")
    if content:
        if not os.path.exists("data"):
            os.makedirs("data")
        
        file_path = os.path.join("data", "artigo_extraido.txt")

        # Salva o conteúdo no arquivo
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content.get_text())
            print(f"Conteúdo salvo em '{file_path}'")
    else:
        print("Não foi possível encontrar o conteúdo do artigo.")
else:
    print(f"Erro ao acessar a URL: {result['status']}")
