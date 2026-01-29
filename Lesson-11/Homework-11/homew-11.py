import sqlite3

# 1. Create (or connect to) the database
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# 2. Create the Roster table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 3. Insert data into the table
data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany(
    "INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)",
    data
)

# 4. Update Jadzia Dax to Ezri Dax
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

# Save changes and close connection
conn.commit()
conn.close()

print("Database created, data inserted, and update completed successfully.")
