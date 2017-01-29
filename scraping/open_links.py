import webbrowser,requests,bs4,sys

print('Googling...')
res=requests.get('https://google.com/search?q='+' '.join(sys.argv[1:]))
elementSoup=bs4.BeautifulSoup(res.text,"lxml")
links=elementSoup.select('.r a')
toopen=min(6,len(links))
for i in range(toopen):
    webbrowser.open('https://google.com'+links[i].get('href'))
    print(links[i].getText())
