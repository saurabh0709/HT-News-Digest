# 📬 HT News Digest

A simple Python script that scrapes daily headlines from the [Hindustan Times - World News](https://www.hindustantimes.com/world-news) section and sends them as a **beautiful, clickable HTML email** every morning.

---

## 📌 Features

✅ Scrapes the latest news headlines from Hindustan Times  
✅ Sends headlines in a **well-formatted HTML email** with clickable links  
✅ Uses Gmail SMTP with app password for secure email delivery  
✅ Runs automatically using **Render Cron Jobs** (no need to keep your laptop on)  
✅ Keeps your credentials safe using environment variables  

---

## 🌐 Live Deployment

This project is hosted on **[Render](https://render.com/)** using:
- A **Background Worker** service that runs the script
- A **Cron Job** that executes the script daily

---

## 🧑‍💻 Tech Stack

- **Python 3**
- `requests`, `beautifulsoup4`, `lxml` for web scraping  
- `smtplib`, `email.mime` for sending emails  
- `fake-useragent` to simulate browser requests  
- Render cloud platform for deployment & scheduling

---

## 🛡️ Environment Variables

To keep sensitive info secure, the following environment variables are used:

| Variable         | Description                      |
|------------------|----------------------------------|
| `SENDER_EMAIL`   | Your Gmail address (used to send emails) |
| `RECEIVER_EMAIL` | The email address that receives the news |
| `APP_PASSWORD`   | App password for the sender Gmail account |

🔐 [Generate a Gmail App Password](https://support.google.com/accounts/answer/185833?hl=en)

---

## 📝 How It Works

1. Fetches the latest headlines from Hindustan Times using `requests` and `BeautifulSoup`
2. Builds a nice HTML layout with links to articles
3. Sends that email using Gmail SMTP with TLS encryption
4. Scheduled daily via Render so it runs even if your computer is off

---

## 🛠 Setup Instructions (for Local Use)

```bash
# 1. Clone the repo
git clone https://github.com/your-username/ht-news-digest.git
cd ht-news-digest

# 2. Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variables (optional: use a .env file or set manually)
export SENDER_EMAIL=your_email@gmail.com
export RECEIVER_EMAIL=receiver_email@gmail.com
export APP_PASSWORD=your_generated_app_password

# 5. Run the script
python main.py
