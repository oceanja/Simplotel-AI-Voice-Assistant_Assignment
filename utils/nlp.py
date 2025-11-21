import sqlite3
import difflib

DB_PATH = "simplotel.db"


def get_best_response(user_text):
    user_text = user_text.lower().strip()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM faq")
    faqs = cursor.fetchall()

    conn.close()

    questions = [q[0] for q in faqs]

   
    closest_match = difflib.get_close_matches(user_text, questions, n=1, cutoff=0.4)

    if closest_match:
        for q, a in faqs:
            if q == closest_match[0]:
                return a

    for q, a in faqs:
        if q == "default":
            return a

    return "Sorry, I couldn't understand that."

get_response = get_best_response
