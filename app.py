


import os
import requests
import csv
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables from .env file
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")


def scrape_remoteok():
    """
    Scrapes remote Python job listings from Remote OK and returns a list of dictionaries.
    """
    url = "https://remoteok.com/remote-python-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    jobs_data = []

    for row in soup.select("tr.job"):
        title_elem = row.select_one("h2")
        company_elem = row.select_one("h3")
        link_elem = row.select_one("a.preventLink")

        if title_elem and company_elem and link_elem:
            title = title_elem.get_text(strip=True)
            company = company_elem.get_text(strip=True)
            link = "https://remoteok.com" + link_elem["href"]

            jobs_data.append({
                "title": title,
                "company": company,
                "link": link
            })

    return jobs_data


def save_to_csv(jobs):
    """
    Saves the list of job dictionaries to a CSV file.
    """
    if not jobs:
        print("No jobs to save.")
        return

    csv_file = "remote_python_jobs.csv"
    keys = jobs[0].keys()

    with open(csv_file, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(jobs)

    print(f"💾 Job data successfully saved to {csv_file}!")


def send_email(jobs):
    """
    Formats the job data and sends it as an email.
    """
    if not jobs:
        print("No jobs found to send in email.")
        return

    # Format the jobs for the email body
    email_body_list = [f"{job['title']} - {job['company']}\n{job['link']}" for job in jobs]
    body = "\n\n".join(email_body_list)

    message = MIMEMultipart()
    message["From"] = EMAIL_ADDRESS
    message["To"] = EMAIL_RECEIVER
    message["Subject"] = "Latest Remote Python Jobs"
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(message)

    print("✅ Email sent successfully!")


if __name__ == "__main__":
    job_list = scrape_remoteok()
    save_to_csv(job_list)
    send_email(job_list)