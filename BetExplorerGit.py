from multiprocessing.sharedctypes import Value
from socket import timeout  
import requests
from bs4 import BeautifulSoup
import csv
from re import sub
import re
from os.path import abspath, realpath, join, dirname

def getMatches():
    r = requests.get('https://www.betexplorer.com/soccer/italy/serie-a/results/', timeout=2000)
    soup = BeautifulSoup(r.content, 'html.parser')
    with open('D:/Bet Predictor/matches.csv', 'w', encoding='UTF8', newline='') as f:
        for tr in soup.find_all('tr'):
            match_tds = tr.find_all('td', attrs = {'class': 'h-text-left'})
            for item in match_tds:
                matches = item.find_all('a')
                for a in matches:
                    print('https://www.betexplorer.com' + a['href'], file=f)

##############################################  To-do/Notepad  #######################################################
#RegEx (re) get match name from matches.csv                              #DONE#
#Write match name to output_cleaned                                      #DONE#
#Save getDetails() to JSON/CSV file
#Change the formatting to fit JSON/CSV
#Set delimiter before/after sections       or     use matrix to split data
#
#

#def addHeaders():
        #file1 = open('D:/Bet Predictor/Tabela.csv')
        #file2 = open('D:/Bet Predictor/details.csv', 'w+')
        #csvreader = csv.reader(file1)
        #header = []
        #header = next(csvreader)
       # header
       # file1.close()
       # csvwriterH = csv.writer(file2)
       # csvwriterH.writerow(header)
       # file2.close()

def addHeaders():
    with open('D:/Bet Predictor/details.csv', 'w') as csvfile:
        kolumny = ['mecz', 'data', 'gole1', 'gole2']
        for i in kolumny:
            writer = csv.DictWriter(csvfile, fieldnames=kolumny, delimiter=',')
            writer.writerows()


def getDetails():
    df = open('D:/Bet Predictor/output.txt', 'w')
    with open('D:/Bet Predictor/matches.csv', 'r', encoding='UTF8', newline='') as f:
        for i in f:
            #name = i.split('/')
            #match = name[6]
            r = requests.get(i, timeout=2000)
            soup = BeautifulSoup(r.content, 'lxml')
            #print(match, file=df)
            #for tr in soup.find_all('ul'):
            wynik = soup.find_all('li', class_='list-details_item') #attrs = ({'class' : 'list-details__item', 'id' : 'js-partial'}))
            Time = soup.find_all('li', class_ = 'list-details__item')
            for item in wynik:
                    #wynik2 = item.find('h2')
                wynik2 = item.h2.text
                text = wynik2.text.strip()
            for item in Time:
                TimeTr = item.find_all('td')
                print('\\' + item.text, file=df)
            

                            


# Penalty kick znajduje się przed minutą, w krórej padła bramka
#file = abspath(join(dirname(__file__), 'Output.txt'))
#file_open = open(file, 'r')
#file_read = file_open.read()
#file_open.close()

#new_file = abspath(join(dirname(__file__), 'Output_cleaned.txt'))
#new_file_open = open(new_file, 'w')


def replace_content(dict_replace, target):
    """Based on dict, replaces key with the value on the target."""

    for check, replacer in list(dict_replace.items()):
        target = sub(check, replacer, target)
        # target = target.replace(check, replacer)

    return target


# check : replacer
dict_replace = {
    '<td></td>': '',
    '<td style="width: 4ex; text-align: right;">': 'Time: ',
    '</td>' : '',
    '<td>' : 'Player: '
}

#new_content = replace_content(dict_replace, file_read)
#new_file_open.write(new_content)
#ew_file_open.close()

#def matchName():
    




# Test
#print(file_read)

#print(new_content)


getMatches()
getDetails()
