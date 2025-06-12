@echo off
TITLE Occhio AI - Server

echo Avvio del server per Occhio AI...
echo.
echo QUESTA FINESTRA DEVE RIMANERE APERTA (puoi ridurla a icona).
echo.

rem CORREZIONE: rimossi gli apici singoli di troppo. Ora il percorso è solo tra doppi apici.
cd "C:\Users\david\OneDrive\Desktop\progetto_immagini"

rem Usiamo il percorso completo del tuo utente per streamlit
"C:\Users\david\AppData\Local\Programs\Python\Python313\Scripts\streamlit.exe" run analizzatore_immagini.py --server.headless=true

pause