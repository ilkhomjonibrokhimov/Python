import requests
import sqlite3
import csv
from bs4 import BeautifulSoup
from datetime import datetime

db_name = "jobs.db"
url = "https://realpython.github.io/fake-jobs"

requests.get(url)

def init_db():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
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

def scrape_jobs():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_cards = soup.find_all("div", class_ = 'card-content')
    
    jobs = []

    for job in job_cards:
        title = job.find("h2", class_= 'title is-5').text.strip()
        company = job.find("h3", class_= 'subtitle is-6 company').text.strip()
        location = job.find("p", class_= 'location').text.strip()
        description = (' ').join(job.find("div", class_= 'content').text.strip().split())
        link = job.find("a", string= 'Apply')["href"]

        jobs.append((title, company, location, description, link))

    return jobs

def upsert_jobs(jobs):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    for job in jobs:
        title, company, location, description, link = job
        cursor.execute("""
            SELECT description, application_link
            FROM jobs
            WHERE job_title=? AND company=? AND location=?
        """, (title, company, location))

        existing = cursor.fetchone()

        if existing is None:
            # insert new job
            cursor.execute("""
                INSERT INTO jobs 
                (job_title, company, location, description, application_link)
                VALUES (?, ?, ?, ?, ?)
            """, job
            )
            print(f"Inserted: {title} | {company}")
        else:
            old_desc, old_link = existing
            if old_desc != description or old_link != link:
                cursor.execute("""
                    UPDATE jobs
                    SET description=?, application_link=?, last_updated=?
                    WHERE job_title=? AND company=? AND location=?
                """, (description, link, datetime.now(), title, company, location))
                print(f"Updated: {title} | {company}")
    conn.commit()
    conn.close()

def filter_jobs(location = None, company = None):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    query = "SELECT job_title, company, location, description, application_link FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")

    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")
    
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result


def export_to_csv(jobs, filename = 'filtered_jobs.csv'):
    headers = ["job title", "Company", "Location", "Description", "Application Link"]

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(jobs)

    print(f"Exported {len(jobs)} jobs to {filename}")


if __name__ == "__main__":
    init_db()

    scraped_jobs = scrape_jobs()
    upsert_jobs(scraped_jobs)
    filtered = filter_jobs()
    export_to_csv(filtered)

