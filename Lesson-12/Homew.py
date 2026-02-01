import requests
import sqlite3
import csv
from bs4 import BeautifulSoup
from datetime import datetime

DB_NAME = "jobs.db"
URL = "https://realpython.github.io/fake-jobs"

# -------------------------------
# Database Setup
# -------------------------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            application_link TEXT,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(job_title, company, location)
        )
    """)
    conn.commit()
    conn.close()


# -------------------------------
# Scraping Logic
# -------------------------------
def scrape_jobs():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    job_cards = soup.find_all("div", class_="card-content")

    jobs = []

    for job in job_cards:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find("div", class_="content").text.strip()
        link = job.find("a", string="Apply")["href"]

        jobs.append((title, company, location, description, link))

    return jobs


# -------------------------------
# Incremental Load + Update Logic
# -------------------------------
def upsert_jobs(jobs):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    for job in jobs:
        title, company, location, description, link = job

        cur.execute("""
            SELECT description, application_link
            FROM jobs
            WHERE job_title=? AND company=? AND location=?
        """, (title, company, location))

        existing = cur.fetchone()

        if existing is None:
            # Insert new job
            cur.execute("""
                INSERT INTO jobs 
                (job_title, company, location, description, application_link)
                VALUES (?, ?, ?, ?, ?)
            """, job)
            print(f"Inserted: {title} | {company}")

        else:
            old_desc, old_link = existing
            if old_desc != description or old_link != link:
                # Update existing job
                cur.execute("""
                    UPDATE jobs
                    SET description=?, application_link=?, last_updated=?
                    WHERE job_title=? AND company=? AND location=?
                """, (description, link, datetime.now(), title, company, location))
                print(f"Updated: {title} | {company}")

    conn.commit()
    conn.close()


# -------------------------------
# Filtering Logic
# -------------------------------
def filter_jobs(location=None, company=None):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    query = "SELECT job_title, company, location, description, application_link FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")

    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")

    cur.execute(query, params)
    results = cur.fetchall()
    conn.close()
    return results


# -------------------------------
# Export to CSV
# -------------------------------
def export_to_csv(jobs, filename="filtered_jobs.csv"):
    headers = ["Job Title", "Company", "Location", "Description", "Application Link"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(jobs)

    print(f"Exported {len(jobs)} jobs to {filename}")


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    init_db()

    scraped_jobs = scrape_jobs()
    upsert_jobs(scraped_jobs)

    # Example filtering
    filtered = filter_jobs(location="Remote")
    export_to_csv(filtered, "remote_jobs.csv")

