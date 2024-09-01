#%% Imports
import streamlit as st
import pandas as pd

#%% Access databases
# path = r'C:\\Users\\almmo\Documents\\Python Scripts\\GitHub\\MontiGym\\data_montigym - Database exercicios.csv'
df_ex = pd.read_csv(r'C:\\Users\\almmo\Documents\\Python Scripts\\GitHub\\MontiGym\\data_montigym - Database exercicios.csv')
df_ex.set_index('ID')
df_log = pd.read_csv(r'C:\\Users\\almmo\Documents\\Python Scripts\\GitHub\\MontiGym\\data_montigym - Training log.csv')
df_log.sort_values(by='Date', inplace=True)
df_log = df_log.reset_index(drop=True)

training_plan = ["A","B","C"]
active_plan = 1

#%% Functions

def decide_next_training_session(training_variations=["A","B","C"]):
    if df_log['Training plan'].iloc[-1] == active_plan:
        last_training = df_log['Training'].iloc[-1]
        last_index = training_plan.index(last_training)
        next_index = last_index + 1
        if next_index > len(training_variations)-1:
            next_index = 0  # Reset to 0 after reaching the last (probably 2=C)
        next_training = f'{active_plan}-{training_variations[next_index]}'
    else:
        next_training = f"{active_plan}-{training_variations[0]}"
    return next_training

#%% Layout
st.title("My gym app")
training_companion, calendar, exercises, results = st.tabs(["Treinos", "Calendário", "Exercícios", "Resultados"])

with training_companion:
    for i in range(5):
        st.subheader(f"exercicio {i}")
        st.write("x series de y repetições")
        st.write("placeholder pro video e ultimas x cargas")
        st.number_input(f"Carga executada (kg) (somente variáveis) {i}")
        st.checkbox(f"Cada lado {i}", value=False)
        # st.number_input(f"Carga acessório (kg) (fixa pra cada exercicio/instrumento){i}", value=10)
        st.divider()