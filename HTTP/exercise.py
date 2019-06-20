import requests
from random import randint as ran

url = 'https://icanhazdadjoke.com/search'

term = input('Let me tell you a joke! Give me a topic: ')


def jokes(term):
    response = requests.get(
        url,
        headers={'Accept': 'application/json'},
        params={
            'term': term
        }
    ).json()
    num_jokes = response['total_jokes']
    data = response['results']
    if num_jokes == 1:
        return print(f"I've got one joke about {term}. Here it is: {data[0]['joke']}")
    elif num_jokes > 1:
        return print(f"I've got {num_jokes} jokes about {term}. Here's one: {data[ran(0,num_jokes)]['joke']}")
    return print(f"Sorry, I don't have any jokes about {term}! Please try again.")


jokes(term)
