import json
from bs4 import BeautifulSoup


def convertHtmlfile(name):
    f = open("./html_files/{}.html".format(name))
    soup = BeautifulSoup(f, features="html.parser")

    table = soup.find(id='grd_itemlist')
    rows = table.findChildren('tr', recursive=False)
    head_row = rows[0]

    headers = []

    for header in head_row.stripped_strings:
        title = header.replace('.', ' ')
        headers.append(title)

    # Body rows

    def create_dict_row(row_number):
        row = rows[row_number]

        row_list = []

        for text in row.stripped_strings:
            row_list.append(text)

        data = dict(zip(headers, row_list))

        return data

    steel_mines_data = []

    for i in range(len(rows)):
        j = i + 1
        try:
            dict_data = create_dict_row(j)
            steel_mines_data.append(dict_data)
        except IndexError:
            break

    with open('./json_files/{}.json'.format(name), 'w') as fp:
        json.dump(steel_mines_data, fp)
