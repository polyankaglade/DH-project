# ВНИМАНИЕ!
# Этот код требует наличия следующих модулей:
# PyPDF2 и bs4
# Убедитесь что они установлены!

import time
import PyPDF2
import re
import os
import urllib.request
from bs4 import BeautifulSoup
import sys
from urllib.request import Request, urlopen
  

# открывает сстраницу и собирает все ссылки на статьи
def open_link_1(link):
    try:
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        #connect to that page
        f = urlopen(req)
    except urllib.error.HTTPError:  # вот тут очень плохое решение чтоб код не вылетал если 404
        print('An Error occured')
    else:
        #read it all in
        myfile = f.read()
        #build a document model
        soup = BeautifulSoup(myfile,'html.parser')
        articles = soup.findAll(attrs={"class" : "part-link"})
    return articles

# создает список ссылок на все полученные статьи
def get_articles():
    all_articles = []
    for i in range(1,48): #48
        link = 'https://www.cambridge.org/core/journals/journal-of-linguistics/most-cited?pageNum=%d' % i
        print(link)
        articles = open_link_1(link)
        for article in articles:
            art_link = re.search('href="(.*?)"',str(article))
            art_link = art_link.group(1)
            all_articles.append(art_link)
        #time.sleep(2)
    return all_articles

# создает файл, куда записывать список ссылок
def create_meta_txt():
    x = 'link\n'
    with open('all_camb_articles.txt','w',encoding='utf-8') as f:
        f.write(x)    

# записывает список в файл построчно
def write_meta_txt(all_articles):
    with open('all_camb_articles.txt','a',encoding='utf-8') as f:
        for link in all_articles:
            f.write(link)
            f.write('\n')

# функция для первого запуска
# запускает краулер по сайту кембриджа
def first_start():
    all_articles = get_articles()
    create_meta_txt()
    write_meta_txt(all_articles)
    print('''Ура! Теперь в этой же попке лежит файл all_camb_articles.txt
В нем - список ссылок на 934 статьи с www.cambridge.org/core/journals/journal-of-linguistics
Дальше программа все сделвет сама!''')

# достает список всех авторов и референсов
# ВНИМАНИЕ!
# для референсов - достает только фамилии
# для авторов - инициалы/имя и фамилию --- это надо дальше обрабатывать
def open_link_2(short_link):
    link = 'https://www.cambridge.org' + short_link
    references = []
    authors = []
    try:
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        #connect to that page
        f = urlopen(req)
    except urllib.error.HTTPError:  # вот тут очень плохое решение чтоб код не вылетал если 404
        print('An Error occured')
    else:
        #read it all in
        myfile = f.read()
        #build a document model
        soup = BeautifulSoup(myfile,'html.parser')

        references_raw = soup.findAll(attrs={"class" : "surname"})
        if len(references_raw)>0:
            for i in references_raw:
                x = i.get_text()
                references.append(x)
        else:
            references.append('no-references-found')

        authors_raw = soup.findAll(attrs={"class" : "more-by-this-author "})
        for ii in authors_raw:
            xx = ii.get_text()
            authors.append(xx)
    return references,authors

# ДОРАБОТАТЬ
# собирает связку автор+цитаты+(вес) и пишет её в файл
# def create_data():
    

# достает ссылку из файла и передает её в обработку
# возвращает (в идеале) файл который можноскормить Gephi и кол-во обработанных статей
# пока что для каждой статьи возвращает список авторов и список фамилий референсов
# если референсов нет - возращает список из одного элемента 'no-references-found'
def get_output_data():
    n = 0
    with open('all_camb_articles.txt','r',encoding='utf-8') as f: # delete "test"
        lines = f.readlines()
        #print(len(lines))
        for link in lines[1:11]: # ВНИМАНИЕ тут ограничение на 10 статей из списка, чтобы обработать все иcпользуйте [1:]
            references,authors = open_link_2(link)
            print(authors)
            if len(references)> 1:
                print(references[:2])
            else:
                print(references)
            #create_data()
            n += 1
    n = str(n)
    return n
    
# основная ф-ция
# спрашивает, нужно ли создавать файл с ссылками или он уже есть в той же папке
# выполняет основной код
# сообщает сколько статей обработано по завершении
def main():
    first = str(input('''Если вы запускаете этот код в первый раз, введите 1 и нажмите Enter.
Если вы запускаете не в первый и/или у вас уже есть файл со списком всех статей - просто нажмите Enter'''))
    if first == '1':
        first_start()
    elif first == '':
        print('Понел, работаю!')
    else:
        print('Ты долбаебка? Тебе русским по белому сказали че нажать! Перезапускай код теперь.')
        sys.exit()
    num = get_output_data()
    print('Done. Вы обработали %s статей.' % num) 


if __name__ == '__main__':
    main()
