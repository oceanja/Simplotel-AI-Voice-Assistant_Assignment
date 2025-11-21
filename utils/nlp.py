import json

def load_faq():
    with open("data/faq.json", "r") as file:
        return json.load(file)

def get_response(user_text):
    user_text = user_text.lower()
    faq_data = load_faq()

    for key in faq_data:
        if key in user_text:
            return faq_data[key]

    return faq_data["default"]
