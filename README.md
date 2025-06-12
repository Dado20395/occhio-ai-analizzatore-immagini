# 👁️ Occhio AI: Analizzatore di Immagini Proattivo

Un'applicazione web multimodale che analizza immagini caricate dall'utente per estrarre dati e insight in automatico, e permette di "dialogare" con l'immagine per ottenere approfondimenti.

## 📸 Screenshot
https://github.com/Dado20395/occhio-ai-analizzatore-immagini/blob/main/Immagine%202025-06-12%20175000.jpg
https://github.com/Dado20395/occhio-ai-analizzatore-immagini/blob/main/Immagine%202025-06-12%20175327.jpg


## 🚀 Funzionalità Principali

- **Analisi Automatica Proattiva:** Al caricamento di un'immagine, l'app genera istantaneamente una "Scheda Dati" che include:
    - Una descrizione testuale dell'immagine.
    - Una lista degli oggetti principali rilevati.
    - L'estrazione di qualsiasi testo presente nell'immagine (OCR).
- **Interfaccia Conversazionale:** Dopo l'analisi automatica, l'utente può porre domande di approfondimento in linguaggio naturale per ottenere maggiori dettagli.
- **Archivio Persistente:** Ogni analisi viene automaticamente salvata con data e ora in un file di log (`archivio_analisi.txt`) grazie al File I/O di Python, creando una cronologia consultabile.
- **Interfaccia a Schede:** L'interfaccia è divisa in una scheda per l'analisi in tempo reale e una per la consultazione dell'archivio storico.

## 🛠️ Tecnologie Utilizzate

- **Linguaggio:** Python
- **Framework Web:** Streamlit
- **Modello AI:** Google Gemini (API multimodale Vision)
- **Librerie Principali:** `Pillow` (per la gestione delle immagini), `streamlit`, `google-generativeai`

## ⚙️ Come Avviare il Progetto

1.  Clonare il repository: `git clone https://github.com/Dado20395/occhio-ai-analizzatore-immagini`
2.  Navigare nella cartella del progetto.
3.  Installare le dipendenze: `pip install streamlit Pillow google-generativeai`
4.  Impostare la variabile d'ambiente `GOOGLE_API_KEY` con la propria chiave API di Google.
5.  Lanciare l'app: `streamlit run analizzatore_immagini.py`
