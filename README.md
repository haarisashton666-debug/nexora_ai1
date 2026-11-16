NEXORA AI — Intelligence Universe

A futuristic Streamlit workspace with account registration/login, SQLite-backed tasks, CSV/Excel analytics, interactive Plotly charts, linear trend forecasting, PDF text extraction, and an optional Gemini-powered assistant.


Features


User registration and sign-in (PBKDF2 password hashing)

Command Centre dashboard

AI Intelligence chat (offline guidance by default; Gemini API when configured)

CSV/XLSX upload, data profiling, charts, correlation matrix and linear trend baseline

PDF text extraction and AI summary

Smart Planner with SQLite task persistence

Responsive purple/electric-blue glassmorphism UI


Run locally

Python 3.10+ recommended.


python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py

Optional Gemini AI

Create .streamlit/secrets.toml locally (do not commit it):


GEMINI_API_KEY = "YOUR_API_KEY"

On Streamlit Community Cloud, open your app settings → Secrets and paste the same TOML line. The app uses the Gemini API only when this key exists; otherwise it runs its built-in offline assistant.


Deploy from GitHub


Create a GitHub repository named nexora-ai.

Upload all files and folders from this project. Ensure app.py and requirements.txt are at the repository root.

Visit https://share.streamlit.io and sign in with GitHub.

Choose Create app, select your repository, branch main, and main file path app.py.

Deploy. Add GEMINI_API_KEY in Advanced settings → Secrets if you want generative AI.

Never place API keys in app.py, README, or a public GitHub commit.


Official guide: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy


Important prototype limitations


SQLite is suitable for a learning prototype, but Community Cloud local disk is not durable storage. Use Supabase/PostgreSQL before depending on persistent accounts/tasks or multi-user production use.

This app's linear forecast is a simple baseline, not a validated prediction service.

PDF extraction works for text-based PDFs. Scanned PDFs need OCR, which is not included.

The app is not a native Android APK. It is a responsive web app that can be opened in a mobile browser.

Do not upload confidential, medical, financial-account, or otherwise sensitive data to this prototype.


Project structure

nexora-ai/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── config.toml
