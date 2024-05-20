import google.generativeai as genai
import json

generationConfig = {
    "candidate_count": 1,
    "temperature": 0.5,
    "max_output_tokens": 1000,
}

safetySettings = [
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

def elabora_plano(key, dados):
    '''Recebe as informações do usuário e elabora o plano de treino baseado na quantidade de dias desejada, objetivos e especificidades do usuário.
    
    Parameters:
        key (str): API Key do Gemini;
        dados (obj): tipo_corpo (str): "ECTOMORFO", "MESOMORFO" ou "ENDOMORFO" | altura (str): Pode ser informado no formato "181cm" ou "1.81m" | peso (str): Deve ser informado no formato "72.5kg" | dores (str): Informar caso o usuário possua dores ou limitações, separando por vírgulas | objetivo (str): Texto nas palavras do usuário, definindo suas metas e objetivos | dias_semana (int) | sexo (str): "Masculino" ou "Feminino"
    
    Returns:
        data (list[dict[str, str]]): Lista de objetos gerada pelo Gemini em que cada objeto é constituído por uma key 'alfa' (ordem do treino, em ordem alfabética crescente), e uma key 'grupos' (grupos musculares a serem trabalhados neste treino)
    '''
    genai.configure(api_key=key)

    tipo_corpo = dados['tipo_corpo']
    altura = dados['altura']
    peso = dados['peso']
    dores = dados['dores']
    objetivo = dados['objetivo']
    dias_semana = dados['dias_semana']
    sexo = dados['sexo']

    model = genai.GenerativeModel(model_name='gemini-1.0-pro', generation_config=generationConfig, safety_settings=safetySettings)

    grupos = model.generate_content(["Elabore um plano de treino de {} dias seguidos (sem descanso) para uma pessoa do sexo {} com um corpo do tipo {}, {} de altura e pesando {}. Considere que o objetivo deste treino é {}, e esta pessoa possui as seguintes restrições: {}. Retorne o resultado em uma string json, sendo este json uma lista de ojetos, em que cada objeto é composto por duas chaves: 'alfa' (Esta chave determina a ordem do treino, em ordem alfabética crescente, sendo assim, no primeiro objeto o valor da chave 'alfa' deve ser 'A', e assim por diante), 'grupos' (Os grupos musculares que serão trabalhados neste dia, em string, separados por vírgula)".format(dias_semana, sexo, tipo_corpo, altura, peso, objetivo, dores)])
    grupos.resolve()

    # Remove marcação extra
    string_json = grupos.text.replace("```json\n", "").replace("\n```", "")

    # Converte para JSON
    data = json.loads(string_json)
    
    return data

def elabora_treino(key, dados):
    genai.configure(api_key=key)

    grupos_musculares = dados['grupos']
    tipo_corpo = dados['dados_usuario']['tipo_corpo']
    altura = dados['dados_usuario']['altura']
    peso = dados['dados_usuario']['peso']
    dores = dados['dados_usuario']['dores']
    objetivo = dados['dados_usuario']['objetivo']
    sexo = dados['dados_usuario']['sexo']

    model = genai.GenerativeModel(model_name='gemini-1.0-pro', generation_config=generationConfig, safety_settings=safetySettings)

    treino = model.generate_content(["Elabore um treino dos seguintes grupos musculares: {}. Para uma pessoa do sexo {} com um corpo do tipo {}, {} de altura e pesando {}. Considere que o objetivo deste treino é {}, e esta pessoa possui as seguintes restrições: {}. Retorne o resultado em uma string json, sendo este json uma lista de ojetos, em que cada objeto é composto pelas seguintes chaves: 'nome' (Nome do exercício); 'descricao' (uma breve descrição sobre este exercício); 'instrucoes' (Lista de strings contendo as instruções para a execução do exercício, em que cada string é uma instrução ou passo da execução); 'series' (String informando a quantidade de séries); 'repeticoes' (String informando a quantidade de repetições); 'descanso' (Número inteiro informando o tempo recomendado de descanso entre as séries, em segundos); 'tipo' (Tipo do exercício, devendo ser Funcional, Musculação, Cardio ou Alongamento); 'ordemExec' (Esta chave determina a ordem do treino, em ordem numérica crescente, sendo assim, no primeiro objeto o valor da chave 'ordemExec' deve ser '1', e assim por diante).".format(grupos_musculares, sexo, tipo_corpo, altura, peso, objetivo, dores)])
    treino.resolve()

    # Remove marcação extra
    string_json = treino.text.replace("```json\n", "").replace("\n```", "")

    # Converte para JSON
    data = json.loads(string_json)

    return data=

def substitui_item(key, dados):
    pass


# Modelos testes

'''
elaboraPlano_requestBody = {
    'tipo_request': 'ELABORA_PLANO',
    'dados': {
        'tipo_corpo': 'ECTOMORFO',
        'altura': '181cm',
        'peso': '72.5kg',
        'dores': 'Dor leve no pulso direito ao praticar flexão de punho',
        'objetivo': 'Definir parte superior do corpo e hipertrofiar pernas e glúteos',
        'dias_semana': 5,
        'sexo': 'Masculino'
    },
}

print(elabora_plano(key='AIzaSyBhzecrZgtwrdL0kzzu5DsH6q5dcwFOHkU', dados=elaboraPlano_requestBody['dados']))
'''
'''
elaboraTreino_requestBody = {
    'tipo_request': 'ELABORA_TREINO',
    'dados': {
        'grupos': 'Peito, Tríceps, Ombro',
        'dados_usuario': {
            'tipo_corpo': 'ECTOMORFO',
            'altura': '181cm',
            'peso': '72.5kg',
            'dores': 'Dor leve no pulso direito ao praticar flexão de punho',
            'objetivo': 'Definir parte superior do corpo e hipertrofiar pernas e glúteos',
            'sexo': 'Masculino'
        }
    }
}

print(elabora_treino(key='AIzaSyBhzecrZgtwrdL0kzzu5DsH6q5dcwFOHkU', dados=elaboraTreino_requestBody['dados']))
'''