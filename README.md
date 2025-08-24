💼 Remote Python Jobs Scraper

A Python script that scrapes the latest remote Python job listings from RemoteOK
, saves them to a CSV file, and emails the results.

🚀 Features

🌍 Web Scraping: Extracts job title, company, and link from RemoteOK.

📂 CSV Export: Saves scraped job listings to remote_python_jobs.csv.

📧 Email Notifications: Automatically emails the job list to your inbox.

🔐 Secure Credentials: Uses environment variables via .env file.

🛠 Tech Stack

Python 3

Libraries:

requests – fetch HTML content

beautifulsoup4 – parse job listings

csv – save data to CSV

smtplib, email.mime – send job listings via email

python-dotenv – manage environment variables

⚙️ Setup & Installation
1️⃣ Clone the repository
git clone https://github.com/DebanilBora/remote-python-jobs.git
cd remote-python-jobs

2️⃣ Create & activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Create a .env file
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=receiver_email@gmail.com


⚠️ Use an App Password if using Gmail.

▶️ Usage

Run the script:

python main.py


✅ Scrapes job data from RemoteOK

✅ Saves jobs to remote_python_jobs.csv

✅ Sends an email with the latest job listings

📂 Example CSV Output
Title	Company	Link
Python Developer	Acme Inc.	https://remoteok.com/12345

Backend Engineer	DevWorks	https://remoteok.com/67890
🏷 Tags

#Python #WebScraping #Automation #EmailBot #RemoteJobs #PortfolioProject
