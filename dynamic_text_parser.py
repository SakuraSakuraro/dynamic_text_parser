import requests
from bs4 import BeautifulSoup
import keyboard

# lists for storing founds texts
found_texts = []

# infinite loop to loop the parser
while True:
    # send GET-requests to page
    url = "enter website url"
    response = requests.get(url)

    # creating object BeautifulSoup on based in HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # for find required tag
    end_tag = soup.find('a', {'name': 'enter name html tag'})

    # get text following the tag
    text = end_tag.next_sibling.strip()

    # check if this text is already in the list
    if text in found_texts:
        print("Such a text has been found before.")
    else:
        # add text to found list
        found_texts.append(text)

        # writing text to file
        with open('texts.txt', 'a', encoding='utf-8') as f:
            f.write(text + "\n")
            print("Text is successfully writed to the file")

    # check if the 'q' key is pressed to exit the loop
    if keyboard.is_pressed('q'):
        print("This program is shut by your command")
        break