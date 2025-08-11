import requests # http requests
from bs4 import BeautifulSoup # web scraping
import smtplib # send the email
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime

now = datetime.datetime.now()

content = '' # email content placeholder

# extracting

def extract_news(url):
    