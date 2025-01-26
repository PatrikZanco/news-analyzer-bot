from transformers import pipeline
import os

pipe = pipeline("summarization", model="facebook/bart-large-cnn")

with open(
    "/Users/patrikzanco/projects/news-analyzer-bot/scrapper/data/artigo_extraido.txt",
    "r",
    encoding="utf-8",
) as arquivo:
    conteudo = arquivo.read()

sumarization = pipe(conteudo, max_length=800, min_length=600, do_sample=False)

if sumarization:
    summary_text = sumarization[0]["summary_text"]

    os.makedirs("/Users/patrikzanco/projects/news-analyzer-bot/scrapper/data", exist_ok=True)
    file_path = os.path.join("/Users/patrikzanco/projects/news-analyzer-bot/scrapper/data", "artigo_sumarizado.txt")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(summary_text)
        print(f"Resumo salvo com sucesso em '{file_path}'")
else:
    print("O pipeline não conseguiu gerar um resumo.")
