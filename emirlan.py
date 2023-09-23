import json
import random
import uuid

from faker import Faker

fake = Faker("ru_RU")  # Set Russian locale

categories = ["бизнес", "медицина", "образование", "экология", "суды", "религия"]

data = []

for i in range(50):
    entry = {
        "id": i,  # Generate and assign a UUID
        "title": fake.sentence(),
        "date": fake.date(pattern="%d.%m.%Y"),
        "text": fake.paragraph(),
        "voice": random.randint(1, 2000),
        "category": random.choice(categories),
    }
    data.append(entry)

# Serialize the data to JSON format
json_data = json.dumps(data, ensure_ascii=False, indent=4)

# Print or save the JSON data as needed
print(json_data)
