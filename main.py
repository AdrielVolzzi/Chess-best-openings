import streamlit as st
import pandas as pd

# Carregar os dados
@st.cache
def load_data():
    data = pd.read_csv('openings.csv')
    return data

data = load_data()

# Título da aplicação
st.title('Recomendador de Aberturas de Xadrez')

# Campo de entrada para a sequência de movimentos
user_moves = st.text_input('Digite a sequência de movimentos:', '')

# Função para encontrar a melhor abertura com base nos movimentos
def find_best_opening(moves):
    filtered_data = data[data['Moves'].str.contains(moves, case=False, na=False)]
    if not filtered_data.empty:
        best_opening = filtered_data.loc[filtered_data['Player Win %'].idxmax()]
        return best_opening
    else:
        return None

# Botão para buscar a melhor abertura
if st.button('Buscar melhor abertura'):
    best_opening = find_best_opening(user_moves)
    if best_opening is not None:
        st.write(f"Melhor abertura: {best_opening['Opening']}")
        st.write(f"Taxa de vitória: {best_opening['Player Win %']}%")
        st.write(f"Número de jogos: {best_opening['Num Games']}")
        st.write(f"Detalhes dos movimentos: {best_opening['Moves']}")
    else:
        st.write("Nenhuma abertura encontrada com os movimentos fornecidos.")


