import json
import sqlite3

# Connect to database
conn = sqlite3.connect("simplotel.db")
cursor = conn.cursor()


with open("data/faq.json", "r") as file:
    faqs = json.load(file)   


for question, answer in faqs.items():
    cursor.execute(
        "INSERT INTO faq (question, answer) VALUES (?, ?)",
        (question.lower(), answer)
    )


conn.commit()
conn.close()

print("Data successfully inserted into SQLite database")
