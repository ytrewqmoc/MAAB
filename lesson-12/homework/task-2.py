import requests
import sqlite3
import csv
from bs4 import BeautifulSoup

DB_NAME = "jobs.db"

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            application_link TEXT,
            UNIQUE(title, company, location) 
        )
    ''')
    conn.commit()
    conn.close()

def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    job_listings = []
    jobs = soup.find_all("div", class_="card-content")

    for job in jobs:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find("div", class_="content").text.strip()
        application_link = job.find("a", string="Apply").get("href")


        job_listings.append((title, company, location, description, application_link))

    return job_listings

def update_database(job_listings):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for job in job_listings:
        title, company, location, description, application_link = job

        cursor.execute("SELECT description, application_link FROM jobs WHERE title=? AND company=? AND location=?",
                       (title, company, location))
        existing_job = cursor.fetchone()

        if existing_job:
            if existing_job[0] != description or existing_job[1] != application_link:
                cursor.execute("UPDATE jobs SET description=?, application_link=? WHERE title=? AND company=? AND location=?",
                               (description, application_link, title, company, location))
                print(f"Updated job: {title} at {company}")
        else:
            cursor.execute("INSERT INTO jobs (title, company, location, description, application_link) VALUES (?, ?, ?, ?, ?)",
                           (title, company, location, description, application_link))
            print(f"Added new job: {title} at {company}")

    conn.commit()
    conn.close()

def filter_jobs(location=None, company=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    query = "SELECT title, company, location, description, application_link FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location=?"
        params.append(location)
    if company:
        query += " AND company=?"
        params.append(company)

    cursor.execute(query, tuple(params))
    results = cursor.fetchall()
    conn.close()

    return results

def export_to_csv(filtered_jobs, filename="filtered_jobs.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company", "Location", "Description", "Application Link"])
        writer.writerows(filtered_jobs)
    print(f"Filtered jobs exported to {filename}")

if __name__ == "__main__":
    create_database()
    job_listings = scrape_jobs()
    update_database(job_listings)

    filtered_jobs = filter_jobs(location="New York")
    export_to_csv(filtered_jobs)
