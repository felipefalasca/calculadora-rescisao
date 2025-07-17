
import streamlit as st

st.set_page_config(page_title="Simulador Rescisão Data4HR", layout="wide")

st.title("Simulador Rescisão Data4HR")

menu = st.sidebar.radio("Navegue pelas seções", ["1. Simulação", "2. Premissas Editáveis", "3. Resultados"])

# Sessão 1: Simulação Consolidada
if menu == "1. Simulação":
    st.header("1. Simulação Consolidada")

    col1, col2 = st.columns(2)
    with col1:
        hc = st.number_input("HC Ativo", min_value=0, value=1000)
        admitidos = st.number_input("Quantidade Admitidos", min_value=0, value=400)
        demitidos_vol = st.number_input("Demitidos Voluntários", min_value=0, value=200)
        demitidos_invol = st.number_input("Demitidos Involuntários", min_value=0, value=50)

    with col2:
        prazo_fechamento = st.number_input("Prazo Médio Fechamento Vagas (dias)", min_value=0, value=51)
        salario_medio = st.number_input("Média Salarial Mensal (R$)", min_value=0, value=3500)
        custo_dia_vaga = st.number_input("Custo Diário de Vaga (R$)", min_value=0, value=150)

    if st.button("Calcular Simulação"):
        turnover = (demitidos_vol + demitidos_invol) / hc * 100
        custo_rescisao_medio = salario_medio * 1.35  # encargo fixo estimado
        custo_total_resc = (demitidos_vol + demitidos_invol) * custo_rescisao_medio
        custo_vacancia = demitidos_invol * prazo_fechamento * custo_dia_vaga
        total_geral = custo_total_resc + custo_vacancia

        st.subheader("Resultados da Simulação")
        st.metric("Turnover Total", f"{turnover:.2f}%")
        st.metric("Custo Médio por Rescisão", f"R$ {custo_rescisao_medio:,.2f}")
        st.metric("Custo Total com Rescisões", f"R$ {custo_total_resc:,.2f}")
        st.metric("Custo com Vacância", f"R$ {custo_vacancia:,.2f}")
        st.metric("Custo Total Estimado", f"R$ {total_geral:,.2f}")

# Sessão 2: Premissas Editáveis
elif menu == "2. Premissas Editáveis":
    st.header("2. Premissas Editáveis")

    with st.expander("📘 Premissas de Recrutamento"):
        consultorias = st.number_input("Valor com Consultorias por Vaga (R$)", value=1000)
        time_rs = st.number_input("Valor Time de R&S (R$)", value=2000)
        exames_adm_qtd = st.number_input("Qtd Exames Admissionais por Vaga", value=1)
        exames_adm_valor = st.number_input("Valor Médio Exame Admissional (R$)", value=120)
        exames_dem_qtd = st.number_input("Qtd Exames Demissionais por Vaga", value=1)
        exames_dem_valor = st.number_input("Valor Médio Exame Demissional (R$)", value=90)
        testes_qtd = st.number_input("Qtd Testes por Vaga", value=1)
        testes_valor = st.number_input("Valor Médio Teste (R$)", value=75)
        pesquisas_qtd = st.number_input("Qtd Pesquisas por Vaga", value=1)
        pesquisas_valor = st.number_input("Valor Médio Pesquisa (R$)", value=60)
        horas_lideranca = st.number_input("Horas de Liderança Dedicadas", value=5)
        valor_hora_lideranca = st.number_input("Valor Hora Liderança (R$)", value=100)

    with st.expander("📗 Curva de Aprendizagem e Perda de Produção"):
        valor_producao = st.number_input("Valor Médio Produção por Colaborador (R$)", value=12000)
        rentabilidade = st.number_input("Rentabilidade por Produção (%)", value=20)
        prazo_aprend = st.number_input("Prazo Médio Curva Aprendizagem (dias)", value=60)
        perda_producao = st.number_input("Perda Produção / Operacional por Colaborador (R$)", value=1500)
        treinamentos_qtd = st.number_input("Qtd Treinamentos por Colaborador", value=2)
        treinamentos_valor = st.number_input("Valor Médio por Treinamento (R$)", value=300)

    with st.expander("📙 Demais Custos e Perdas"):
        epis_qtd = st.number_input("Qtd EPIs", value=3)
        epis_valor = st.number_input("Valor Médio por EPI (R$)", value=80)
        transporte = st.number_input("Transporte (R$)", value=200)
        hospedagem = st.number_input("Hospedagem (R$)", value=600)
        alimentacao = st.number_input("Alimentação (R$)", value=300)
        integracao = st.number_input("Integração (R$)", value=250)
        uniformes = st.number_input("Uniformes (R$)", value=180)
        sistemas = st.number_input("Sistemas e Acessos (R$)", value=400)
        descontos_nao_efetuados = st.number_input("Descontos Não Efetuados (R$)", value=500)

# Sessão 3: Resultados
elif menu == "3. Resultados":
    st.header("3. Resultados Finais")

    st.info("⚙️ Esta seção pode ser usada para compilar todos os custos em um resumo final.")
    st.warning("👉 Cálculos completos com base nas premissas editáveis estarão disponíveis na próxima versão.")
