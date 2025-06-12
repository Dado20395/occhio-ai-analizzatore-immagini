import streamlit as st
from PIL import Image
import google.generativeai as genai
from datetime import datetime
import os

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Occhio AI - Archivio", page_icon="🗂️") # Icona finale: un archivio!

# --- CONFIGURAZIONE API ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") 
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Nome del file di archivio
NOME_FILE_ARCHIVIO = "archivio_analisi.txt"

# --- INIZIALIZZAZIONE STATO DI SESSIONE ---
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
st.title("🗂️ Occhio AI con Archivio")

# --- DEFINIZIONE DELLE SCHEDE (TABS) ---
tab_analisi, tab_archivio = st.tabs(["🔎 Analisi in Tempo Reale", "📚 Archivio Analisi"])

# --- CONTENUTO DELLA SCHEDA 1: ANALISI IN TEMPO REALE ---
with tab_analisi:
    st.header("Carica un'immagine per analizzarla")
    uploaded_file = st.file_uploader("Scegli un'immagine...", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Immagine Caricata", use_container_width=True)

        # Analisi automatica solo se è un nuovo file
        if uploaded_file.name != st.session_state.nome_file_processato:
            with st.spinner("L'AI sta analizzando l'immagine in automatico..."):
                prompt_default = """
                Analizza l'immagine fornita e crea una "Scheda Dati" strutturata usando il formato Markdown. La scheda deve contenere:
                ### Descrizione Concisa
                (Riassunto di 1-2 frasi.)
                ### Oggetti Principali Rilevati
                (Elenco puntato degli elementi più importanti.)
                ### Testo Trovato nell'Immagine (OCR)
                (Trascrivi qualsiasi testo leggibile. Se non c'è, scrivi "Nessun testo rilevato".)
                """
                analisi = analizza_immagine(prompt_default, image)
                
                if analisi:
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
        
        # Sezione per domande di approfondimento
        st.markdown("---")
        st.subheader("Fai una Domanda Specifica")
        prompt_utente = st.text_input("La tua domanda di approfondimento:", placeholder="Es. Che tipo di fiore è quello sulla sinistra?")

        if st.button("Chiedi all'AI", type="primary"):
            if prompt_utente:
                with st.spinner("L'AI sta cercando una risposta..."):
                    risposta_specifica = analizza_immagine(prompt_utente, image)
                    if risposta_specifica:
                        st.info(risposta_specifica)
            else:
                st.warning("Per favore, inserisci una domanda.")

# --- CONTENUTO DELLA SCHEDA 2: ARCHIVIO ---
with tab_archivio:
    st.header("Cronologia di Tutte le Analisi Salvate")
    st.write("Qui puoi consultare tutte le analisi che hai effettuato nel tempo.")

    if st.button("🔄 Aggiorna Archivio"):
        # Questo pulsante non fa nulla di attivo, ma forza Streamlit a ricaricare lo stato, 
        # utile se il file viene modificato esternamente.
        st.toast("Archivio ricaricato.")

    try:
        # Apriamo il file in modalità 'r' (read) per leggerlo
        with open(NOME_FILE_ARCHIVIO, "r", encoding="utf-8") as f:
            contenuto_archivio = f.read()
            # st.code è ideale per mostrare testo pre-formattato con barre di scorrimento
            st.code(contenuto_archivio, language=None)
    except FileNotFoundError:
        st.info("L'archivio è ancora vuoto. Effettua la tua prima analisi nella scheda 'Analisi in Tempo Reale' per iniziare.")
    except Exception as e:
        st.error(f"Impossibile leggere il file di archivio: {e}")