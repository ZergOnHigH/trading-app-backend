# 🛠️ trading-app-backend

Projekt backendu aplikacji do zarządzania użytkownikami, zadaniami (`tasks`) oraz obsługą maili, oparty na **Python Flask + MongoDB**.

## 📦 Technologie

- Python 3.x
- Flask
- Flask-PyMongo
- Flask-JWT-Extended
- Flask-Mail
- python-dotenv
- Marshmallow
- MongoDB

---

## 📁 Struktura projektu

```
trading-app-backend/
├── auth/                   # logika rejestracji i logowania użytkowników
├── tasks/                  # moduł CRUD dla tasków
├── emails/                 # obsługa wysyłki e-maili
├── db/                     # konfiguracja połączenia z MongoDB
├── config.py               # konfiguracja aplikacji (np. Mongo URI)
├── extensions.py           # inicjalizacja rozszerzeń Flask (MongoDB, JWT)
├── app.py                  # główny plik uruchamiający aplikację Flask
├── .env                    # zmienne środowiskowe
├── requirements.txt        # zależności projektu
└── README.md               # dokumentacja projektu
```

---

## 🚀 Jak uruchomić projekt lokalnie

```bash
# 1. Utwórz i aktywuj środowisko wirtualne
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

# 2. Zainstaluj zależności
pip install -r requirements.txt

# 3. Uruchom aplikację
flask --app app --debug run
```

---

## 🔐 Endpointy API

### 🔑 Użytkownicy (`/api/auth`)

- `POST /register` – rejestracja użytkownika
- `POST /login` – logowanie użytkownika

### ✅ Taski (`/api/tasks`)

- `POST /add` – dodanie nowego taska
- `GET /all` – pobranie wszystkich tasków
- `DELETE /remove` – usunięcie taska po nazwie

### ✉️ E-maile (`/api/emails`)

- `POST /send` – wysłanie e-maila (potrzebne dane odbiorcy i wiadomości)

---

## 🧪 Testowanie (Postman)

- Wysyłaj zapytania na `http://localhost:5000`
- Wybierz odpowiednią metodę (POST, GET, DELETE)
- Ustaw `Body` → `raw` → `JSON`
- Nagłówki: `Content-Type: application/json`
- (Dla zabezpieczonych endpointów – token JWT w Authorization)

---

## 📄 Przykładowe Body (dodawanie taska)

```json
{
  "nazwa": "Zrobić zakupy",
  "opis": "Mleko, chleb, jajka",
  "priorytet": "średni",
  "termin": "2025-06-01T15:00:00"
}
```

## 📄 Przykładowe Body (wysyłka maila)

```json
{
  "to": "przyklad@email.com",
  "subject": "Test",
  "body": "Wiadomość testowa"
}
```

---

## 🧹 .gitignore (rekomendowane wpisy)

```
venv/
.venv/
__pycache__/
*.pyc
.env
.vscode/
.idea/
.DS_Store
Thumbs.db
*.log
```

---

## 📌 Autor

Projekt stworzony w celach edukacyjnych i jako portfolioAutor: **Paweł Bonisławski**
