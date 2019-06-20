from termcolor import colored
from pyfiglet import figlet_format as ff
# help(termcolor) -- Shows documentation

text = colored('Hi There!', color='yellow',
               on_color='on_cyan', attrs=['blink'])
# print(text)

valid_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

msg = input('What would youlike to print? ')
color = input('What color? ')

if color not in valid_colors:
    color = 'magenta'


ascii_art = ff(msg)
colored_ascii = colored(ascii_art, color=color)
print(colored_ascii)
