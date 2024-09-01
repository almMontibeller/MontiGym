import streamlit as st

st.title("🎈 My new app")

training, calendar, exercises, results = st.tabs(["Treinos", "Calendário", "Exercícios", "Resultados"])

with training:
    for i in range(5):
        st.subheader(f"exercicio {i}")
        st.write("x series de y repetições")
        st.write("placeholder pro video e ultimas x cargas")
        st.number_input(f"Carga executada (kg) (somente variáveis) {i}")
        st.checkbox(f"Each side {i}", value=False)
        st.number_input(f"Carga acessório (kg) (fixa pra cada exercicio/instrumento){i}", value=10)
        st.divider