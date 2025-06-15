# Analizzatore di Immagini Multimodale

Applicazione web per l'analisi di immagini basata sull'API multimodale di Google Gemini. Il sistema è progettato per estrarre informazioni strutturate da dati visivi non strutturati e per consentire un'interrogazione di approfondimento in linguaggio naturale.

---

### Architettura e Funzionalità

Il software implementa un'interfaccia utente proattiva che esegue un'analisi preliminare automatica al caricamento dell'immagine. I risultati vengono resi persistenti su file di log per consultazioni future.

-   **Analisi Proattiva dei Dati Visivi:** All'input di un'immagine, il sistema esegue l'estrazione automatica di metadati testuali, includendo:
    -   Una descrizione sintetica del contenuto visivo.
    -   Una classificazione degli oggetti principali rilevati.
    -   Il riconoscimento ottico dei caratteri (OCR) per qualsiasi testo presente.
-   **Interfaccia Conversazionale di Follow-up:** Dopo l'analisi iniziale, l'utente può interrogare il sistema con domande specifiche per ottenere ulteriori dettagli o elaborazioni basate sul contesto dell'immagine.
-   **Persistenza dei Dati:** Ogni analisi generata viene salvata con un timestamp in un file di archivio locale (`.txt`), garantendo la tracciabilità e la consultazione storica dei risultati.

---

### Stack Tecnologico

-   **Linguaggio:** Python
-   **Framework:** Streamlit
-   **API & Modelli:** Google Gemini (API Vision)
-   **Librerie Core:** `Pillow`, `google-generativeai`, `streamlit`

---

---

<details>
<summary><strong>⚙️ Istruzioni per l'Avvio in Locale</strong></summary>

1.  Clonare il repository: `git clone https://github.com/Dado20395/occhio-ai-analizzatore-immagini`
2.  Navigare nella cartella del progetto.
3.  Installare le dipendenze: `pip install streamlit Pillow google-generativeai`
4.  Impostare la variabile d'ambiente `GOOGLE_API_KEY` con la propria chiave API di Google.
5.  Lanciare l'app: `streamlit run analizzatore_immagini.py`
</details>
