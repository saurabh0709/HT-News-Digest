import requests
from bs4 import BeautifulSoup
import lxml
from fake_useragent import UserAgent
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Function to get headlines from Hindustan Times
def fetch_headlines():
    headers = {
        'User-Agent': UserAgent().random,
        "Referer": "https://www.hindustantimes.com/",
        "Sec-Ch-Ua": '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1"
    }

    url = 'https://www.hindustantimes.com/world-news'

    r = requests.get(url, headers=headers)
    html = r.text

    soup = BeautifulSoup(html, 'lxml')

    head_lines = soup.find_all(['h2', 'h3'], class_='hdg3')
    headlines = []

    for h in head_lines:
        link = h.find('a')
        if link and link.text.strip():
            text = link.text.strip()
            href = link.get('href', '').split('"')[0]  # fix malformed links
            full_link = 'https://www.hindustantimes.com' + href if href.startswith('/') else href
            headlines.append((text, full_link))

    return headlines


# Function to send email
def send_email(headlines_with_links):

    sender_email = os.environ['SENDER_EMAIL']
    receiver_email = os.environ['RECEIVER_EMAIL']
    app_password = os.environ['APP_PASSWORD']


    subject = "Your Daily Hindustan Times Headlines 🗞️"

    # HTML Email Body
    html_body = "<h2>Today's Top Headlines:</h2><ul>"
    for text, link in headlines_with_links:
        html_body += f'<li><a href="{link}" target="_blank">{text}</a></li>'
    html_body += "</ul><p>Stay informed! ☕</p>"

    # Constructing the email
    message = MIMEMultipart('alternative')
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(html_body, 'html'))

    # Sending email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(message)

    print('✅ Email sent successfully!')

# Run
daily_headlines = fetch_headlines()
send_email(daily_headlines)

# qoji hwxt pomf smvi