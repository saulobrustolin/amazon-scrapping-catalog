from components.catalog import acess

# acess : page_html
# catalog : link pages

def process_url(url: str):
    url = url.decode("utf-8") if isinstance(url, bytes) else url

    print(url)

    # Acessa o site usando Selenium
    result = acess(url)
    
    # Verifica o tipo de result
    if isinstance(result, bytes):
        result = result.decode("utf-8")  # Caso seja bytes, decodifique para string
    
    print(f"Result: {result}, type: {type(result)}")  # Verificando o tipo do resultado
    
    return {"result": result}
