# Configurações e parâmetros que deverão ser utilizados pelo Gemini para geração dos resultados.
# Todas as funções irão utilizar estes parâmetros.

GOOGLE_API_KEY = "SUA_API_KEY"              # Como obter: https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br

model = 'gemini-1.0-pro'

generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
    "max_output_tokens": 1000,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
]