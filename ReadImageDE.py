from typing import Text
import pytesseract
from datetime import datetime
from PIL import Image
import re
import ner
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
import imdb


pytesseract.pytesseract.tessract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract-ocr-w64-setup-v5.0.0-rc1.20211030.exe"
Text = pytesseract.image_to_string = ('Email.png')

print(Text)


# Find the date 

def get_date_taken(path):
    return Image.open(path)._getexif()[Text]

import pandas as pd
from datetime import datetime

datelist = pd.date_range(datetime.date, periods=100).tolist()
datetime.date.strftime('%Y-%m-%d')

# Find the email addresses

match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', Text)
match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', Text)
match.group(0) 



# Find the Rooms Rates
regex = re.compile('$')
      
# Pass the string in search 
# method of regex object
  
if(regex.search(Text) == Text.split("$", 4)):
   print(regex)



# Find the Rooms Names

Rnames = re.search(r'Room: [^A-z]').group()

print(Rnames)


# Find Individual Names.. format "Firstname Lastname" 

ne_chunk(pos_tag(word_tokenize(Text)))  
ia = imdb.IMDb() # creating instance of IMDb
search = ia.search_person(Text)  # search the name throughout the text
print(search)
 
for i in range(len(search)):
    print(search[i][Text])