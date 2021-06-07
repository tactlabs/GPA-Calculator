from bs4 import BeautifulSoup
import requests
resp   = requests.get("http://techietet.com/gpa/reg2017.php")
soup1  = BeautifulSoup(resp.content, "html.parser")
page   = soup1.find_all("span",{'class':'subjectname'})
length = len(page)
songs  = []

for position in range(length):
    songs.append(soup1.find_all("span",{'class':'subjectname'})[position].get_text())
print(songs)
