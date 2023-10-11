import json
import requests
from time import sleep


COMMON_PAIRS = {
    '1': "EURUSD",
    '2': "EURGBP",
    '3': "GBPUSD",
    '4': "USDJPY",
    '5': "AUDUSD",
    '6': "USDCHF",
    '7': "NZDUSD",
    '8': "USDCAD",
    '9': "USDZAR"
}


def get_data():
    url = f"https://www.freeforexapi.com/api/live?pairs={get_quote(COMMON_PAIRS)}"

    try:
        request = requests.get(url)
        response = request.json()
        final_response = json.dumps(response, indent=4)

        return final_response

    except requests.exceptions.RequestException as ex:
        print("ERROR")


def get_quote(COMMON_PAIRS):
    try:
        holder_pairs = []
        while True:
            print(COMMON_PAIRS)
            chose_quotes = [quote for quote in input(f"Chose quotes you want like enter number in quote.").split()]

            for wrong_input in chose_quotes:
                if not 1 <= int(wrong_input) <= 9:
                    print(f"Wrong input: {wrong_input}")
                    chose_quotes.remove(wrong_input)

            holder_pairs += [COMMON_PAIRS.get(x) for x in chose_quotes]

            command = input("Do you want to add more quotes Y/N: ")

            if command.upper() == 'Y':
                continue
            elif command.upper() == 'N':
                set(holder_pairs)
                wanted_quotes = ','.join(holder_pairs)

                return wanted_quotes
            else:
                print("Invalid key!")

    except ValueError:
        print("Your input is incorrect!")
        sleep(5)


print(get_data())
