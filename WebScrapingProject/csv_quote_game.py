import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader
import io


BASE_URL = 'http://quotes.toscrape.com'


def read_quotes():
    with io.open('WebScrapingProject/quotes.csv', 'r', encoding="utf-8") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(all_quotes):
    quote = choice(all_quotes)
    remaining_guesses = 4
    guess = ''
    print("Here is the quote: ")
    print(quote['text'])
    print(quote['author'])

    while guess.lower() != quote['author'].lower() and remaining_guesses >= 1:
        guess = input(
            f"Who said this quote? Guesses remaining: {remaining_guesses} - ")
        if guess.lower() == quote['author'].lower():
            print("You got it right!")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, 'html.parser')
            birth_date = soup.find(class_='author-born-date').get_text()
            birth_location = soup.find(
                class_='author-born-location').get_text()
            print(
                f"Here is a hint: Author was born in {birth_date} {birth_location}")
        elif remaining_guesses == 2:
            print(
                f"Here is a hint: Author's first name starts with: {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote['author'].split(' ')[1][0]
            print(
                f"Here is a hint: Author's last name starts with: {last_initial}")
        else:
            print(
                f"Sorry you ran out of guesses. The answer was - {quote['author']}")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'not'):
        again = input("Would you like to play again (y/n)? ")
    if again.lower() in ('y', 'yes'):
        return start_game(all_quotes)
    else:
        print('Thank you for playing!')


quotes = read_quotes()
start_game(quotes)
