Remote Python Job Scraper and Data Logger 🐍
This project is an automated Python script designed to help with the job search. It scrapes the latest remote Python job listings from the Remote OK website, saves the structured data to a CSV file for long-term tracking, and sends a summary of the listings directly to your email inbox.

Features
Web Scraping: Uses the requests library to fetch the HTML content of the Remote OK website and BeautifulSoup to intelligently parse and extract key job information.

Data Persistence: Demonstrates data handling skills by saving the scraped job title, company, and link to a remote_python_jobs.csv file, allowing for historical analysis and tracking.

Automated Email Alerts: Sends a neatly formatted email with a summary of the latest job listings, keeping you informed without manual effort.

Secure Credentials: Utilizes a .env file to securely store and access sensitive information like email addresses and passwords, ensuring your credentials are never exposed in the code or on a public repository.

Technologies Used
Python: The core programming language.

requests: For making HTTP requests to the website.

BeautifulSoup: For parsing HTML content.

dotenv: For managing environment variables.

smtplib & email: For sending emails.

csv: Python's built-in module for reading and writing CSV files.