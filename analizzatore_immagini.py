import streamlit as st
from PIL import Image
import google.generativeai as genai
from datetime import datetime
import os 

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Occhio AI", page_icon="👁️")

# --- CONFIGURAZIONE API ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("Chiave API non trovata! Assicurati di aver impostato la variabile d'ambiente GOOGLE_API_KEY.")
    st.stop() # Interrompe l'esecuzione se la chiave non c'è

genai.configure(api_key=GOOGLE_API_KEY)
# Usiamo il modello Flash che ha una quota gratuita più generosa
model = genai.GenerativeModel('gemini-1.5-flash-latest')

NOME_FILE_ARCHIVIO = "archivio_analisi.txt"

# --- INIZIALIZZAZIONE STATO DI SESSIONE ---
if 'analisi_default' not in st.session_state:
    st.session_state.analisi_default = None
if 'nome_file_processato' not in st.session_state:
    st.session_state.nome_file_processato = None

# --- FUNZIONE DI ANALISI ---
def analizza_immagine(prompt, image_input):
    try:
        response = model.generate_content([prompt, image_input])
        return response.text
    except Exception as e:
        st.error(f"Si è verificato un errore: {e}")
        if "quota" in str(e).lower():
            st.error("Hai raggiunto la tua quota di richieste gratuite. Riprova più tardi.")
        return None

# --- INTERFACCIA UTENTE ---
st.title("👁️ Occhio AI: L'Analizzatore di Immagini")
st.write("Carica un'immagine e fammi una domanda su ciò che vedi. L'AI risponderà per te.")

uploaded_file = st.file_uploader("Scegli un'immagine...", type=["jpg", "jpeg", "png"])

image = None 
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Immagine Caricata", use_container_width=True)

    if uploaded_file.name != st.session_state.nome_file_processato:
        with st.spinner("L'AI sta analizzando l'immagine in automatico..."):
            
            prompt_default = """
            Analizza l'immagine fornita e crea una "Scheda Dati" strutturata usando il formato Markdown.
            La scheda deve contenere le seguenti sezioni, anche se una sezione dovesse risultare vuota:
            
            ### Descrizione Concisa
            (Scrivi qui un riassunto di 1-2 frasi.)

            ### Oggetti Principali Rilevati
            (Elenca qui con dei trattini gli oggetti o i soggetti più importanti visibili.)

            ### Testo Trovato nell'Immagine (OCR)
            (Trascrivi qui qualsiasi testo leggibile presente nell'immagine. Se non c'è testo, scrivi "Nessun testo rilevato".)

            IMPORTANTE: Tutta la risposta deve essere esclusivamente in lingua italiana.
            """
            
            analisi = analizza_immagine(prompt_default, image)
            
            if analisi:
                st.session_state.analisi_default = analisi
                st.session_state.nome_file_processato = uploaded_file.name
                
                try:
                    with open(NOME_FILE_ARCHIVIO, "a", encoding="utf-8") as f:
                        f.write(f"--- Analisi del {datetime.now().strftime('%d-%m-%Y %H:%M:%S')} ---\n")
                        f.write(f"File Immagine: {uploaded_file.name}\n\n")
                        f.write(analisi)
                        f.write("\n\n")
                    st.toast("✅ Analisi salvata nell'archivio!", icon="📝")
                except Exception as e:
                    st.error(f"Errore durante il salvataggio del file: {e}")

    if st.session_state.analisi_default:
        with st.expander("➡️ Clicca qui per vedere l'Analisi Automatica"):
            st.markdown(st.session_state.analisi_default)

    st.markdown("---")
    st.header("❓ Fai una Domanda Specifica")
    prompt_utente = st.text_input("La tua domanda di approfondimento:", placeholder="Es. Che tipo di fiore è quello sulla sinistra?", label_visibility="collapsed")

    if st.button("✨ Chiedi all'AI", type="primary"):
        if prompt_utente:
            with st.spinner("L'AI sta cercando una risposta..."):
                
                prompt_specifico_completo = f"""
                Basandoti sull'immagine fornita, rispondi alla seguente domanda dell'utente.
                La tua risposta deve essere esclusivamente in lingua italiana.

                Domanda dell'utente: "{prompt_utente}"
                """

                risposta_specifica = analizza_immagine(prompt_specifico_completo, image)
                
                if risposta_specifica:
                    st.info(risposta_specifica)
        else:
            st.warning("Per favore, inserisci una domanda.")
