# Definir body da solicitação para testes

requestBody = {
    'tipo_request': 'ELABORA_PLANO',    # Para solicitações deste tipo, a IA irá elaborar um plano completo de treino
    'dados': {
        'tipo_corpo': 'ECTOMORFO',      # ECTOMORFO, MESOMORFO ou ENDOMORFO
        'altura': '181cm',              # Pode ser informado no formato "181cm" ou "1.81m"
        'peso': '72.5kg',               # Deve ser informado no formato "72.5kg"
        'dores': 'Dor leve no pulso direito ao praticar flexão de punho',                   # Informar caso o usuário possua dores ou limitações, separando por vírgulas
        'objetivo': 'Definir parte superior do corpo e hipertrofiar pernas e glúteos',      # Texto nas palavras do usuário, definindo suas metas e objetivos
        'dias_semana': 6,               # Quantidade de dias que o usuário pretende treinar por semana
        'sexo': 'Masculino'             # "Masculino" ou "Feminino"
    },
}

'''requestBody = {
    'tipo_request': 'SUBSTITUI_ITEM',    # Para solicitações deste tipo, a IA irá substituir determinado exercicio por outro sugerido, com base no motivo informado pelo usuário
    'dados': {
        'exercicio': '',                # Nome do exercício a ser substituído
        'aparelho': '',                 # Aparelho no qual o exercício é realizado
        'motivo': '',                   # Motivo pelo qual deve ser substituído
    },
}'''

# Importar módulos
'''from geminiFunctions import elabora_plano, substitui_item
'''
import google.generativeai as genai

# Configurar API key

GEMINI_KEY = 'AIzaSyBhzecrZgtwrdL0kzzu5DsH6q5dcwFOHkU'