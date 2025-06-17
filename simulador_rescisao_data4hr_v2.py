
import streamlit as st

st.set_page_config(page_title="Simulador Rescisão Data4HR", layout="wide")

st.title("Simulador Rescisão Data4HR")

menu = st.sidebar.radio("Navegue pelas seções", ["1. Simulação", "2. Premissas de Cálculo", "3. Resultados"])

# Sessão 1: Simulação
if menu == "1. Simulação":
    st.header("1. Simulação Consolidada")

    col1, col2 = st.columns(2)
    with col1:
        hc = st.number_input("Total de colaboradores (HC)", min_value=0, value=1000)
        salario_medio = st.number_input("Média salarial mensal (R$)", min_value=0, value=3500)
        perc_vol = st.slider("% de desligamento voluntário", 0, 100, 20)
        perc_invol = st.slider("% de desligamento involuntário", 0, 100, 5)

    with col2:
        prazo_subs = st.number_input("Prazo médio de substituição (dias)", min_value=0, value=51)
        encargo_extra = st.number_input("Encargos médios por desligamento (%)", min_value=0, value=35)
        custo_dia_vaga = st.number_input("Custo diário da posição vaga (R$)", min_value=0, value=150)

    if st.button("Calcular Simulação"):
        qtd_vol = hc * perc_vol / 100
        qtd_invol = hc * perc_invol / 100
        turnover_total = (qtd_vol + qtd_invol) / hc * 100
        custo_rescisao_medio = salario_medio * (1 + encargo_extra / 100)
        custo_total_resc = (qtd_vol + qtd_invol) * custo_rescisao_medio
        custo_vacancia = qtd_invol * prazo_subs * custo_dia_vaga
        total_geral = custo_total_resc + custo_vacancia

        st.subheader("Resultados da Simulação")
        st.metric("Turnover Total", f"{turnover_total:.2f}%")
        st.metric("Custo Médio por Rescisão", f"R$ {custo_rescisao_medio:,.2f}")
        st.metric("Custo Total com Rescisões", f"R$ {custo_total_resc:,.2f}")
        st.metric("Custo com Vacância", f"R$ {custo_vacancia:,.2f}")
        st.metric("Custo Total da Operação", f"R$ {total_geral:,.2f}")

# Sessão 2: Premissas de Cálculo
elif menu == "2. Premissas de Cálculo":
    st.header("2. Premissas de Cálculo")

    with st.expander("📌 Verbas Rescisórias"):
        aviso = st.number_input("Aviso Prévio (R$)", min_value=0, value=26000)
        medica = st.number_input("Assistência Médica (R$)", min_value=0, value=55000)
        vida = st.number_input("Seguro de Vida (R$)", min_value=0, value=15000)
        consignado = st.number_input("Consignado (R$)", min_value=0, value=40000)
        outros_resc = st.number_input("Outros (R$)", min_value=0, value=20000)

    with st.expander("📌 Custo com Atração e Seleção"):
        consultorias = st.number_input("Consultorias (R$)", value=100000)
        testes = st.number_input("Testes e Pesquisas (R$)", value=3000000)
        exames_adm = st.number_input("Exames ADM (R$)", value=96000)
        horas_lideranca = st.number_input("Horas de Liderança (R$)", value=25455)

    with st.expander("📌 Custos Relacionados a Voluntários"):
        curva_aprend = st.number_input("Curva de Aprendizagem (R$)", value=4800000)
        treinamento = st.number_input("Treinamento (R$)", value=235000)
        perda = st.number_input("Perda de Produção (R$)", value=4080000)
        exames_dem = st.number_input("Exames DEM (R$)", value=25600)

    with st.expander("📌 Demais Investimentos"):
        epis = st.number_input("EPIs (R$)", value=82600)
        transporte = st.number_input("Transporte Integração (R$)", value=51600)
        onboarding = st.number_input("Integração / Onboarding (R$)", value=23600)
        hospedagem = st.number_input("Hospedagem / Alojamento (R$)", value=137600)
        alimentacao = st.number_input("Alimentação Integração (R$)", value=18500)
        sistemas = st.number_input("Sistemas e Acessos (R$)", value=10600)

    st.success("Premissas prontas para uso nos cálculos finais.")

# Sessão 3: Resultados
elif menu == "3. Resultados":
    st.header("3. Resultados Finais")

    st.markdown("⚙️ Os resultados consolidados finais poderão ser construídos a partir das simulações e premissas.")
    st.markdown("👉 Em versões futuras, adicionaremos exportação em PDF e comparação entre cenários.")
