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

print(elaboraTreino_requestBody['dados']['dados_usuario']['tipo_corpo'])

'''itens = [
{
    "nome": "Rotação de tronco",
    "descricao": "Este exercício promove a mobilidade da coluna vertebral e aquece os músculos do core.",
    "instrucoes": [
        "Fique em pé com os pés afastados na largura dos ombros e os joelhos levemente flexionados.",
        "Mantenha os braços estendidos à sua frente, paralelos ao chão.",
        "Gire o tronco para a direita, levando o braço direito para trás e o esquerdo para frente, mantendo o core firme.",
        "Retorne à posição inicial e repita o movimento para o lado esquerdo.",
        "Continue alternando os lados, realizando o movimento de forma suave e controlada."
    ],
    "series": 3,
    "repeticoes": 10,
    "descanso": 10,
    "tipo": "Alongamento",
    "ordemExec": 0
},
{
    "nome": "Puxada articulada",
    "descricao": "Este exercício trabalha os músculos das costas, principalmente o latíssimo do dorso, além de fortalecer bíceps e antebraços.",
    "instrucoes": [
        "Sente-se na máquina de puxada articulada, ajustando o apoio para as coxas de forma que seus joelhos fiquem flexionados a 90 graus.",
        "Segure a barra com uma pegada pronada (palmas para baixo), um pouco mais larga que a largura dos ombros.",
        "Incline o tronco levemente para trás, mantendo o peito elevado e o core firme.",
        "Puxe a barra em direção ao peito, concentrando a força nos músculos das costas.",
        "Mantenha os cotovelos próximos ao corpo durante todo o movimento.",
        "Desça a barra lentamente de volta à posição inicial, controlando o movimento."
    ],
    "series": 4,
    "repeticoes": 10,
    "descanso": 30,
    "tipo": "Musculação",
    "ordemExec": 1
},
{
    "nome": "Remada curva",
    "descricao": "Este exercício fortalece os músculos das costas, principalmente o latíssimo do dorso, trapézio e romboides.",
    "instrucoes": [
        "Fique em pé com os pés afastados na largura dos ombros, segurando uma barra com pegada pronada (palmas para baixo), um pouco mais larga que a largura dos ombros.",
        "Flexione o tronco para frente, mantendo as costas retas e o core firme. O tronco deve estar quase paralelo ao chão.",
        "Mantenha os joelhos levemente flexionados e a barra pendurada na direção do chão.",
        "Puxe a barra em direção ao abdômen, mantendo os cotovelos próximos ao corpo.",
        "Contraia os músculos das costas no topo do movimento.",
        "Desça a barra lentamente de volta à posição inicial, controlando o movimento."
    ],
    "series": 4,
    "repeticoes": 10,
    "descanso": 30,
    "tipo": "Musculação",
    "ordemExec": 2
}
]'''