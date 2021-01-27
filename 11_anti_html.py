import urllib.request
from bs4 import BeautifulSoup


url = "https://www.google.com/"
my_html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(my_html)
print(soup.get_text())

# Output
# GoogleSearch Images Maps Play YouTube News Gmail Drive More »Web History 
# | Settings | Sign in Advanced searchGoogle offered in:  
# हिन्दी বাংলা తెలుగు मराठी தமிழ் ગુજરાતી ಕನ್ನಡ മലയാളം ਪੰਜਾਬੀ Advertising 
# ProgramsBusiness SolutionsAbout GoogleGoogle.co.in© 2021 - Privacy - Terms 