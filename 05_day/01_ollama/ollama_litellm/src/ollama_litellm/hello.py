from litellm import completion

def hello():
    response = completion(
        model="ollama/deepseek-r1:1.5b",  # specify the Ollama model
        messages=[{"role": "user", "content": "write a poem about a cat"}],
        api_base="http://localhost:11434"  # change if your server is remote
    )
    print(response["choices"][0]["message"]["content"])

