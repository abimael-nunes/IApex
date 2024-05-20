# Importar módulos
import google.generativeai as genai
import json
import conf

# Obter configurações do Gemini
GOOGLE_API_KEY = conf.GOOGLE_API_KEY
model_name = conf.model
generation_config = conf.generation_config
safety_settings = conf.safety_settings

# Definir função
def elabora_treino(dados):
    '''Recebe os grupos musculares de deverão ser trabalhado neste treino e as informações do usuário e elabora a lista de exercícios para este determinado dia de treino, de acordo com os objetivos e especificidades do usuário.
    
    Parameters:
        dados (obj): grupos (str) | dados_usuario (obj): tipo_corpo (str): "ECTOMORFO", "MESOMORFO" ou "ENDOMORFO" | altura (str): Pode ser informado no formato "181cm" ou "1.81m" | peso (str): Deve ser informado no formato "72.5kg" | dores (str): Informar caso o usuário possua dores ou limitações, separando por vírgulas | objetivo (str): Texto nas palavras do usuário, definindo suas metas e objetivos | dias_semana (int) | sexo (str): "Masculino" ou "Feminino".
    
    Returns:
        (list[dict[]]): Lista de ojetos, em que cada objeto é composto pelas seguintes chaves: 'nome' (Nome do exercício); 'descricao' (uma breve descrição sobre este exercício); 'instrucoes' (Lista de strings contendo as instruções para a execução do exercício, em que cada string é uma instrução ou passo da execução); 'series' (String informando a quantidade de séries); 'repeticoes' (String informando a quantidade de repetições); 'descanso' (Número inteiro informando o tempo recomendado de descanso entre as séries, em segundos); 'tipo' (Tipo do exercício, devendo ser Funcional, Musculação, Cardio ou Alongamento); 'ordemExec' (Esta chave determina a ordem do treino, em ordem numérica crescente, sendo assim, no primeiro objeto o valor da chave 'ordemExec' deve ser '1', e assim por diante).    '''
    
    genai.configure(api_key=GOOGLE_API_KEY)

    grupos_musculares = dados['grupos']
    tipo_corpo = dados['dados_usuario']['tipo_corpo']
    altura = dados['dados_usuario']['altura']
    peso = dados['dados_usuario']['peso']
    dores = dados['dados_usuario']['dores']
    objetivo = dados['dados_usuario']['objetivo']
    sexo = dados['dados_usuario']['sexo']

    model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config, safety_settings=safety_settings)

    treino = model.generate_content(["Elabore um treino dos seguintes grupos musculares: {}. Para uma pessoa do sexo {} com um corpo do tipo {}, {} de altura e pesando {}. Considere que o objetivo deste treino é {}, e esta pessoa possui as seguintes restrições: {}. Retorne o resultado em uma string json, sendo este json uma lista de ojetos, em que cada objeto é composto pelas seguintes chaves: 'nome' (Nome do exercício); 'descricao' (uma breve descrição sobre este exercício); 'instrucoes' (Lista de strings contendo as instruções para a execução do exercício, em que cada string é uma instrução ou passo da execução); 'series' (String informando a quantidade de séries); 'repeticoes' (String informando a quantidade de repetições); 'descanso' (Número inteiro informando o tempo recomendado de descanso entre as séries, em segundos); 'tipo' (Tipo do exercício, devendo ser Funcional, Musculação, Cardio ou Alongamento); 'ordemExec' (Esta chave determina a ordem do treino, em ordem numérica crescente, sendo assim, no primeiro objeto o valor da chave 'ordemExec' deve ser '1', e assim por diante).".format(grupos_musculares, sexo, tipo_corpo, altura, peso, objetivo, dores)])
    treino.resolve()

    # Remove marcação extra
    string_json = treino.text.replace("```json\n", "").replace("\n```", "")

    # Converte para JSON
    data = json.loads(string_json)

    return data