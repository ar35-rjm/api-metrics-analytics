import asyncio
import random
import time
import httpx

BASE_URL = "http://127.0.0.1:8000"

# Exemplo de rotas e dados de teste (ajusta para os endpoints da tua API)
ENDPOINTS = [
    {"method": "GET", "path": "/"},
    {"method": "GET", "path": "/docs"},
    {"method": "GET", "path": "/api/v1/tasks/"},
    # Adiciona aqui as tuas rotas reais, ex:
    {"method": "POST", "path": "/api/v1/tasks/", "json": {"title": "example task"}},
]

async def send_request(client: httpx.AsyncClient):
    endpoint = random.choice(ENDPOINTS)
    url = f"{BASE_URL}{endpoint['path']}"
    method = endpoint["method"]
    json_payload = endpoint.get("json")

    start_time = time.time()
    try:
        if method == "GET":
            response = await client.get(url)
        elif method == "POST":
            response = await client.post(url, json=json_payload)
        
        elapsed = (time.time() - start_time) * 1000
        print(f"[{response.status_code}] {method} {endpoint['path']} - {elapsed:.2f}ms")
    except Exception as e:
        print(f"Erro na requisição ({method} {endpoint['path']}): {e}")

async def main(total_requests: int = 100, delay_range: tuple = (0.1, 0.5)):
    print(f"🚀 A iniciar simulação de tráfego para {BASE_URL}...")
    async with httpx.AsyncClient() as client:
        for i in range(total_requests):
            await send_request(client)
            await asyncio.sleep(random.uniform(*delay_range))
    print("✅ Simulação concluída!")

if __name__ == "__main__":
    asyncio.run(main(total_requests=50, delay_range=(0.05, 0.3)))