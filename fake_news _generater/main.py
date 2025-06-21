# 1. Import random module
import random

subjects = [
    "Salman Khan",
    "Shahrukh Khan",
    "Deepika Padukone",
    "Amitabh Bachchan",
    "Alia Bhatt",
    "Taj Mahal",
    "Lal Qila",
    "Gateway of India",
    "Mumbai Police",
    "Delhi University",
    "Banaras Ghat",
    "Charminar",
    "India Gate",
    "Bollywood",
    "Chandni Chowk",
    "Ranveer Singh",
    "Sonu Sood",
    "Hrithik Roshan",
    "Kashi Vishwanath Temple",
    "Indian Railways"
]

actions = [
    "sets a new record",
    "finds hidden treasure",
    "gives a shocking statement",
    "announces marriage",
    "spotted with aliens",
    "launches a new app",
    "mysterious event happens",
    "claims to have superpowers",
    "releases a new song",
    "haunted rumors spread",
    "distributes free food",
    "faces sudden flood",
    "invents something new",
    "signs a new film",
    "UFO sighted",
    "quits social media",
    "secret wedding revealed",
    "gold mine discovered",
    "creates a new dance step",
    "mysterious illness spreads"
]

place_or_things = [
    "Marine Drive",
    "Qutub Minar",
    "Howrah Bridge",
    "Lotus Temple",
    "Juhu Beach",
    "Gateway of India",
    "Victoria Memorial",
    "Sunderbans",
    "Red Fort",
    "Raj Ghat",
    "ISKCON Temple",
    "Salar Jung Museum",
    "Golconda Fort",
    "Hawa Mahal",
    "Ajanta Caves",
    "Sanchi Stupa",
    "Rashtrapati Bhavan",
    "Connaught Place",
    "Dilli Haat",
    "Film City Mumbai"
]


while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)

    headlines = f" Breaking news : {subject} {action} {place_or_thing}"
    print("\n" + headlines)

    user_input = input("\n Do you want another headline (yes/no) : ").strip().lower()

    if user_input=='no':
        print("\n Thanks for using this app :)")
        break
