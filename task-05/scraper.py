

import os
import requests
import csv
from bs4 import BeautifulSoup


def score():
    #livescore

    url = "https://www.espncricinfo.com/live-cricket-score"
    src = requests.get(url)
    src.raise_for_status()
    parse = BeautifulSoup(src.text, 'html.parser')
    data = []

    #STATUS
    header = parse.find('div', class_="ds-flex ds-justify-between ds-items-center")
    status = header.find('span', class_="ds-text-tight-xs ds-font-bold ds-uppercase ds-leading-5").text

    #SCORE
    match_tag = parse.find('div', class_="ds-border-b ds-border-line ds-border-r ds-w-1/2")
    this = match_tag.find_all('div', class_ = "ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1")
    for t in this:
        team_p = t.p.contents
        team_div = t.find_all('div')[1].contents
        over = team_div[0].text
        score = team_div[1].text
        team = {'name': team_p[0], 'score': score,'over': over }
        data.append(team)

    #SUMMARY
    summary = parse.find('p', class_="ds-text-tight-s ds-font-regular ds-truncate ds-text-typo").span.text

    result = {'status': status, 'summary': summary}
    data.append(result) 

    return data


    '''RESULT
    loser:  ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-opacity-50 ds-my-1
    winner: ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1
    '''

def resultant():
    url = "https://www.espncricinfo.com/live-cricket-score"
    src = requests.get(url)
    src.raise_for_status()
    parse = BeautifulSoup(src.text, 'html.parser')


    data = []

    header = parse.find('div', class_="ds-flex ds-justify-between ds-items-center")
    status = header.find('span', class_="ds-text-tight-xs ds-font-bold ds-uppercase ds-leading-5").text

    match_tag = parse.find('div', class_="ds-border-b ds-border-line ds-border-r ds-w-1/2")
    winner = match_tag.find_all('div', class_ = "ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1")
    loser = match_tag.find_all('div', class_ = "ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-opacity-50 ds-my-1")

    for t in winner:
        team_p = t.p.contents
        team_div = t.find_all('div')[1].contents
        over = team_div[0].text
        score = team_div[1].text
        team = {'name': team_p[0], 'score': score,'over': over }
        data.append(team)
    
    for t in loser:
        team_p = t.p.contents
        team_div = t.find_all('div')[1].contents
        over = team_div[0].text
        score = team_div[1].text
        team = {'name': team_p[0], 'score': score,'over': over }
        data.append(team)


    
    summary = parse.find('p', class_="ds-text-tight-s ds-font-regular ds-truncate ds-text-typo").span.text

    result = {'status': status, 'summary': summary}
    data.append(result) 

    return data


def generator():
    directory = 'livescores'
    base_filename = 'livescore'
    file_extension = 'csv'
    
    counter = 1
    while True:
        file_name = f'{base_filename}_{counter}.{file_extension}'
        file_path = os.path.join(directory, file_name)

        if not os.path.exists(file_path):
            break
        counter += 1

    data = score()
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data.keys())
        csv_writer.writerow(data.values())


def upcoming():

    url = "https://www.espncricinfo.com/live-cricket-match-schedule-fixtures"
    src = requests.get(url)
    src.raise_for_status()
    parse = BeautifulSoup(src.text, 'html.parser')
    data = []

    match_tag = parse.find('div', class_="ds-bg-fill-content-prime ds-py-3 ds-px-4 ds-flex ds-justify-between hover:ds-bg-ui-fill-translucent ds-space-x-6 ds-border-b ds-border-line")
    name = match_tag.find('p', class_="ds-text-compact-s ds-font-bold ds--mb-1 ds-text-typo").text
    data.append(name)

    time_finder = match_tag.find('div', class_="ds-flex-none ds-w-40")
    time = time_finder.find('span', class_="ds-text-compact-xs ds-font-bold ds-block ds--mb-1 ds-mt-[3px] ds-text-typo-mid1").text
    data.append(time)

