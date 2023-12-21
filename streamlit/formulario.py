import streamlit as st

def app(df):
    st.sidebar.success("En este apartado podrás enviar datos adicionales sobre fatalidades en el conflicto entre Israel y Palestina.")
    st.sidebar.success('IMPORTANTE: Los datos deben de ser respaldados por una fuente fiable')

    if 'data_history' not in st.session_state:
        st.session_state.data_history = []

    def es_numero_entero(cadena):
        try:
            int(cadena)
            return True
        except ValueError:
            return False

    # FORMULARIO PARA DETALLES DE FATALIDAD
    with st.form(key='fatalidades_form'):
        st.title("Registro de Fatalidades")
        name = st.text_input("Nombre de la víctima:")
        date_of_event = st.text_input("Fecha del evento (aaaa-mm-dd):")
        age = st.text_input("Edad de la víctima:")
        citizenship = st.text_input("Nacionalidad de la víctima:")
        event_location = st.text_input("Ubicación del evento:")
        source_url = st.text_input("URL de la Fuente:")
        
        # Botón para enviar datos
        submit_button = st.form_submit_button(label='Enviar Datos')

    # Validar y procesar los datos enviados
    if submit_button:
        if es_numero_entero(age) and es_numero_entero(date_of_event.replace('-', '')):
            datos_fatalidad = {
                "Nombre": name,
                "Fecha del Evento": date_of_event,
                "Edad": int(age),
                "Nacionalidad": citizenship,
                "Ubicación del Evento": event_location,
                "Fuente": source_url
            }
            st.session_state.data_history.append(datos_fatalidad)
            st.success("Datos enviados correctamente.")
        else:
            st.error("Por favor, ingresa valores numéricos válidos para la edad y la fecha del evento.")

    # Mostrar los datos recopilados si el usuario lo solicita
    if st.button("¿Quieres ver los datos recopilados?"):
        st.table(st.session_state.data_history)


