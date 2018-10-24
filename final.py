# ВНИМАНИЕ!
# Этот код требует наличия следующих модулей:
# PyPDF2 и bs4
# Убедитесь что они установлены!

import PyPDF2
import re
import os
import urllib.request
from bs4 import BeautifulSoup
import sys
  

# открывает ссылку и собирает весь хтмл
def open_link(link):
    try:
        #connect to that page
        f = urllib.request.urlopen(link)
    except urllib.error.HTTPError:  # вот тут очень плохое решение чтоб код не вылетал если 404
        myfile = '<div class="cell-inner"><p>[Could not download page]<\p><\div>'*3
        soup = BeautifulSoup(myfile,'html.parser')
    else:
        #read it all in
        myfile = f.read()
        #build a document model
        soup = BeautifulSoup(myfile,'html.parser')
    return soup

# создает словарь вида "ссылка: автор(ы)"
# далее я назваю это списком ссылок
def get_articles():
    all_articles = {}
    for i in range(2000,2019): #2019
        link = 'http://www.dialog-21.ru/digest/%d/articles/' % i
        print(link)
        soup = open_link(link)
        articles = soup.findAll(attrs={"class" : "article-link"})
        for article in articles:
            authors = re.search('class="article-link-author">(.*?)<',str(article))
            authors = authors.group(1)
            link = re.search('class="article-link-title">[\s.]*<a href="(.*?)"',str(article))
            link = link.group(1)
            all_articles.update({link:authors})
    return all_articles

# создает файл, куда записывать список ссылок
def create_meta_txt():
    x = 'link\tauthors\n'
    with open('all_articles.txt','w',encoding='utf-8') as f:
        f.write(x)    

# записывает список в файл построчно
def write_meta_txt(all_articles):
    with open('all_articles.txt','a',encoding='utf-8') as f:
        for link,author in all_articles.items():
            y = link + '\t' + author + '\n'
            f.write(y)

# функция для первого запуска
# запускает краулер по сайту Диалога
def first_start():
    all_articles = get_articles()
    create_meta_txt()
    write_meta_txt(all_articles)
    print('''Ура! Теперь в этой же попке лежит файл all_articles.txt
В нем - список всех статей Диалога в формате
    кусок ссылки - табуляция - автор(ы) статьи
Дальше программа все сделвет сама!''')

# открывает сохраненный пдф, пытается вытащить из него текст,
# закрывает и удаляет пдф с компа
# это максимум того что у меня получилось 
def get_text_from_pdf(file):
    output_text = ''
    pdf = open(file,'rb')
    pdfread = PyPDF2.PdfFileReader(pdf,strict=True)
    num = pdfread.getNumPages()
    for i in range(num):
        page = pdfread.getPage(i)
        text = page.extractText()
        output_text = output_text + str(text)
    pdf.close()
    os.remove(file)
    return output_text

# достает весь текст статьи
def get_text_from_html(soup):
    content = soup.findAll(attrs={"class" : "cell-inner"})
    text = content[2].get_text()
    return text

# открывает ссылку и возращает текст статьи (если получается)
# если это пдф - скачивает его и передает на извлечение текста
# если не пдф - открывает эту страницу и передает на извлечение текста
def get_text(link):
    full_link = 'http://www.dialog-21.ru' + link
    if full_link.endswith('.pdf'):
        destination = 'article.pdf'
        urllib.request.urlretrieve(full_link, destination)
        # МОЖЕТ КОНВЕРТАНУТЬ ПДФ В ДОК(Х)?!
        text = get_text_from_pdf(destination)
        print('Это пдф')
    else:
        print('Это не пдф')
        soup = open_link(full_link)
        text = get_text_from_html(soup)
    #print(text)
    return text

# ДОРАБОТАТЬ
# это самый просто набросок регулярки для цитат
# находит все, что внутри квадратных скобок
def get_citations(text):
    all_skobochki = re.findall('\[(.*?)\]',text)
    return all_skobochki

# ДОРАБОТАТЬ
# как-то обрабатывает авторов
# def get_authors():

# ДОРАБОТАТЬ
# собирает связку автор+цитаты+(вес) и пишет её в файл
#def create_data():

# достает ссылку из файла и передает её в обработку
# возвращает (в идеале) файл который можноскормить Gephi и кол-во обработанных статей
# пока что просто возвращает все что найдено в скобках
def get_output_data():
    n = 0
    with open('all_articles.txt','r',encoding='utf-8') as f: # delete "test"
        lines = f.readlines()
        #print(len(lines))
        for line in lines[353:373]: # ВНИМАНИЕ тут ограничение на 20 статей из списка, чтобы обработать все иcпользуйте [1:]
            link,authors = line.split('\t')
            text = get_text(link)
            #get_authors()
            all_citations = get_citations(text)
            print(all_citations)
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
    print('Done. Вы обработали %s статей конференции Диалог.' % num) 


if __name__ == '__main__':
    main()
