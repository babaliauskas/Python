import requests
from bs4 import BeautifulSoup
# from time import sleep
from random import choice


BASE_URL = 'http://quotes.toscrape.com'


def scrape_quotes():
    url = '/page/1'
    all_quotes = []
    while url:
        res = requests.get(f'{BASE_URL}{url}')
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_='quote')

        for quote in quotes:
            all_quotes.append({
                'text': quote.find(class_='text').get_text(),
                'author': quote.find(class_='author').get_text(),
                'bio-link': quote.find('a')['href']
            })
        next_btn = soup.find(class_='next')
        url = next_btn.find('a')['href'] if next_btn else None
    # sleep(2)
    return all_quotes


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


quotes = scrape_quotes()
start_game(quotes)
