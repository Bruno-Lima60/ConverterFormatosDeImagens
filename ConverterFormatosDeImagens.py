import os
from PIL import Image

img_formatos = {
    "bmp": "BMP",
    "dds": "DDS",
    "gif": "GIF",
    "ico": "ICO",
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "tif": "TIFF",
    "tiff": "TIFF",
    "tga": "TGA",
    "pcx": "PCX",
    "pbm": "PPM",
    "pgm": "PPM",
    "png": "PNG",
    "ppm": "PPM",
    "webp": "WEBP"
}

def converter_imagens():
    print("Formatos Suportados:\n")

    for x in img_formatos:
        print(f"{x}\n", end="")

    formato = input("\nEscolha um formato para converter: ").lower()

    while not any(f.lower().endswith(f".{formato}") for f in os.listdir() if os.path.isfile(f)):
        print("Não foi encontrado nenhum arquivo com esse formato!")
        formato = input("\nEscolha um formato para converter: ").lower()

    while formato not in img_formatos:
        print("Inválido!")
        formato = input("\nEscolha um formato para converter:  ").lower()

    formato_dois = input("Para qual formato deseja converter esses arquivos? ").lower()

    while formato_dois not in img_formatos:
        print("Inválido!")
        formato_dois = input("Para qual formato deseja converter esses arquivos? ").lower()

    if not os.path.exists("novas_imagens"):
        os.mkdir("novas_imagens")

    for arquivo in os.listdir():
        nome, ext = os.path.splitext(arquivo)
        if ext.lower().lstrip('.') == formato.lower():
            filename = os.path.basename(nome)
            formato_novo = formato_dois
            output = os.path.join("novas_imagens", filename + f".{formato_novo.lower()}")

            if os.path.exists(output):
                print(f"'{arquivo}' já foi convertido para '{formato_novo}'!")
                continue

            try:
                with Image.open(arquivo).convert("RGB") as im:
                    im.save(output, img_formatos[formato_novo])
                    print(f"'{arquivo}' convertido para '{output}' com sucesso!")
                    break
            except OSError:
                print("Conversão não foi possível!", arquivo)
                
converter_imagens()