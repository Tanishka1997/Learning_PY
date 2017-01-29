import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status
playfile=open("Romeo and Juliet","wb")
for dt in res.iter_content(100000):
    playfile.write(dt)
playfile.close()
