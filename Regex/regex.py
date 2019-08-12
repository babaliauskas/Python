import re


def extract_number(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None


# print(extract_number('My number is: 123 456-7890 or call me at 132 444-8797'))
# print(extract_number('My number is: 123 456-1237890'))


###############################################

def extract_all_numbers(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input)


# print(extract_all_numbers('My number is: 123 456-7890 or call me at 132 444-8797'))
# print(extract_all_numbers('My number is: 123 456-1237890'))


#################################################

def is_valid_phone(input):
    phone_regex = re.compile(r'^\b\d{3} \d{3}-\d{4}\b$')
    match = phone_regex.search(input)
    if match:
        return True
    return False


# print(is_valid_phone('123 456-1237'))
# print(is_valid_phone('My number is: 123 456-7890 or call me at 132 444-8797'))
# print(is_valid_phone('My number is: 123 456-1237'))


#################################################

def is_valid_phone2(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False


# print(is_valid_phone2('123 456-1237'))
# print(is_valid_phone2('My number is: 123 456-7890 or call me at 132 444-8797'))
# print(is_valid_phone2('My number is: 123 456-1237'))


#####################################################


def parse_name(input):
    name_regex = re.compile(
        r"^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<name>[A-Za-z]+) (?P<last>[A-Za-z]+)$")
    matches = name_regex.search(input)
    print(matches.groups())
    print(matches.group('name'))
    print(matches.group('last'))


parse_name('Mrs. Tilda Swinton')
