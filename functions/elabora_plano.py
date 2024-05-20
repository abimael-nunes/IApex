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
def elabora_plano(dados):
    '''Recebe as informações do usuário e elabora o plano de treino baseado na quantidade de dias desejada, objetivos e especificidades do usuário.
    
    Parameters:
        dados (obj): tipo_corpo (str): "ECTOMORFO", "MESOMORFO" ou "ENDOMORFO" | altura (str): Pode ser informado no formato "181cm" ou "1.81m" | peso (str): Deve ser informado no formato "72.5kg" | dores (str): Informar caso o usuário possua dores ou limitações, separando por vírgulas | objetivo (str): Texto nas palavras do usuário, definindo suas metas e objetivos | dias_semana (int) | sexo (str): "Masculino" ou "Feminino"
    
    Returns:
        data (list[dict[str, str]]): Lista de objetos gerada pelo Gemini em que cada objeto é constituído por uma key 'alfa' (ordem do treino, em ordem alfabética crescente), e uma key 'grupos' (grupos musculares a serem trabalhados neste treino)
    '''
    genai.configure(api_key=GOOGLE_API_KEY)

    tipo_corpo = dados['tipo_corpo']
    altura = dados['altura']
    peso = dados['peso']
    dores = dados['dores']
    objetivo = dados['objetivo']
    dias_semana = dados['dias_semana']
    sexo = dados['sexo']

    model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config, safety_settings=safety_settings)

    grupos = model.generate_content(["Elabore um plano de treino de {} dias seguidos (sem descanso) para uma pessoa do sexo {} com um corpo do tipo {}, {} de altura e pesando {}. Considere que o objetivo deste treino é {}, e esta pessoa possui as seguintes restrições: {}. Retorne o resultado em uma string json, sendo este json uma lista de ojetos, em que cada objeto é composto por duas chaves: 'alfa' (Esta chave determina a ordem do treino, em ordem alfabética crescente, sendo assim, no primeiro objeto o valor da chave 'alfa' deve ser 'A', e assim por diante), 'grupos' (Os grupos musculares que serão trabalhados neste dia, em string, separados por vírgula)".format(dias_semana, sexo, tipo_corpo, altura, peso, objetivo, dores)])
    grupos.resolve()

    # Remove marcação extra
    string_json = grupos.text.replace("```json\n", "").replace("\n```", "")

    # Converte para JSON
    data = json.loads(string_json)
    
    return data