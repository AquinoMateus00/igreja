import streamlit as st
import random

st.set_page_config(page_title="Bingo Online", layout="wide")
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
        }
    </style>
""", unsafe_allow_html=True)


# Inicializar estados
if 'numeros_bingo' not in st.session_state:
    st.session_state.numeros_bingo = list(range(1, 76))
    random.shuffle(st.session_state.numeros_bingo)
    st.session_state.numeros_sorteados = []
    st.session_state.numero_sorteado_rodada = None

# Função para sortear número
def sortear_numero():
    if st.session_state.numeros_bingo:
        numero = st.session_state.numeros_bingo.pop(0)
        st.session_state.numeros_sorteados.append(numero)
        st.session_state.numero_sorteado_rodada = numero

# Função para identificar a letra do número sorteado
def letra_bingo(numero):
    if 1 <= numero <= 15:
        return 'B'
    elif 16 <= numero <= 30:
        return 'I'
    elif 31 <= numero <= 45:
        return 'N'
    elif 46 <= numero <= 60:
        return 'G'
    elif 61 <= numero <= 75:
        return 'O'
    return ''

# Layout dividido em duas colunas
col1, col2 = st.columns([2, 3])

# --- COLUNA ESQUERDA ---
with col1:
    # Título e frase
    st.markdown("<h1 style='text-align: left;'>🎉 Bingo do N.A ♾️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:18px; color: gray; margin-top: -15px;'>Essa é a alegria que vem de Deus!🥰</p>", unsafe_allow_html=True)

    # Botões abaixo da frase
    col_sortear, col_reiniciar = st.columns([1, 1])
    with col_sortear:
        if st.button("🎯 Sortear Número"):
            sortear_numero()
    with col_reiniciar:
        if st.button("🔄 Reiniciar Bingo"):
            st.session_state.numeros_bingo = list(range(1, 76))
            random.shuffle(st.session_state.numeros_bingo)
            st.session_state.numeros_sorteados = []
            st.session_state.numero_sorteado_rodada = None

    # Exibir número sorteado da rodada
    numero_atual = st.session_state.numero_sorteado_rodada
    if numero_atual is not None:
        letra = letra_bingo(numero_atual)
        st.markdown(f"""
            <div style='
                font-size: 48px; 
                font-weight: 700; 
                color: red; 
                border: 3px solid red; 
                border-radius: 12px; 
                width: 120px; 
                height: 120px; 
                display: flex; 
                justify-content: center; 
                align-items: center;
                margin-top: 20px;
                font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
                '>
                {letra}-{numero_atual:02d}
            </div>""", unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style='
                font-size: 48px; 
                font-weight: 700; 
                color: transparent; 
                border: 3px solid transparent; 
                border-radius: 12px; 
                width: 120px; 
                height: 120px; 
                display: flex; 
                justify-content: center; 
                align-items: center;
                margin-top: 5px;
                font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
                '>
                &nbsp;
            </div>""", unsafe_allow_html=True)

# --- COLUNA DIREITA: TABELA BINGO ---
with col2:
    def gerar_coluna(inicio, fim):
        return [i for i in range(inicio, fim+1)]

    colunas_bingo = {
        'B': gerar_coluna(1, 15),
        'I': gerar_coluna(16, 30),
        'N': gerar_coluna(31, 45),
        'G': gerar_coluna(46, 60),
        'O': gerar_coluna(61, 75),
    }

    html = """
    <style>
        .bingo-container {
            width: 100%;
            max-width: 500px;
            overflow-x: auto;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            table-layout: fixed;
        }
        th, td {
            border: 2px solid #999;
            padding: 6px;            
            text-align: center;
            width: 16%;
            height: 5px;
            font-size: 11px;
            font-weight: bold;
        }
        th {
            background-color: white;
            color: black;
            font-size: 18px;
            text-align: center
        }
        .sorteado {
            border: 3px solid red;
            border-radius: 10%;
            background-color: #ffe6e6;
            font-weight: bold;
            color: red;
        }
    </style>
    <div class="bingo-container">
    <table>
    <tr>
            <th style="text-align:center;">B</th>
            <th style="text-align:center;">I</th>
            <th style="text-align:center;">N</th>
            <th style="text-align:center;">G</th>
            <th style="text-align:center;">O</th>
        </tr>
        """

    for i in range(15):
        html += "<tr>"
        for letra in ['B', 'I', 'N', 'G', 'O']:
            coluna = colunas_bingo[letra]
            if i < len(coluna):
                num = coluna[i]
                if num in st.session_state.numeros_sorteados:
                    html += f'<td class="sorteado">{num:02d}</td>'
                else:
                    html += f'<td>{num:02d}</td>'
            else:
                html += "<td></td>"
        html += "</tr>"

    html += "</table></div>"

    st.markdown(html, unsafe_allow_html=True)



#Para Rodar 
# cd "C:\Users\mateu\OneDrive\PROJETOS_PYTHON\Projetos_Pessoais"
# streamlit run bingo_online_na.py

