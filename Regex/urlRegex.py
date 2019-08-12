import re

url_regex = re.compile(
    r"(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)")
match = url_regex.search('https://www.youtube.com/movies')
print(f"Protocol: {match.group(1)}")
print(f"Doman: {match.group(2)}")
print(f"Everything Else: {match.group(3)}")
