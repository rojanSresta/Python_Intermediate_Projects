from bs4 import BeautifulSoup
import requests
import json

url = ('https://www.hangmanwords.com/words')

def web_scrap_json_data():
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        script_tag = soup.find(id="__NEXT_DATA__")
        if script_tag:
            json_data = script_tag.string

            try:
                data = json.loads(json_data)
                return data

                # i used this code to make the output.json just to see the data clearly as the terminal can't show that huge amount of data but we can use jupyter notebook as alternate
                # with open('output.json', 'w', encoding='utf-8') as json_file:
                #     json.dump(data, json_file, ensure_ascii=False, indent=2)

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

        else:
            print("Script tag not found with the specified id.")

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

web_scrap_json_data()