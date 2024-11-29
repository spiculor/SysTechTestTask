import requests

API_BASE_URL = "http://localhost:8000"

def process_text(text):
    endpoint = f"{API_BASE_URL}/process/"
    payload = {"text": text}
    response = requests.post(endpoint, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка обработки текста: {response.status_code}")
        print(response.text)

def search_text(query):
    endpoint = f"{API_BASE_URL}/search/"
    payload = {"text": query}
    response = requests.post(endpoint, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка выполнения поиска: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    text_to_process = "Пример текста для обработки."
    processed_result = process_text(text_to_process)
    print("Результат обработки текста:")
    print(processed_result)
    query = "технологии"
    search_result = search_text(query)
    print("\nРезультат поиска:")
    print(search_result)
