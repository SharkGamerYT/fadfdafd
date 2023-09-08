
scraped_data = []
from bs4 import soup

def scrape():
  

     url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
     bright_star_table = soup.find("table", attrs={"class, wikitable"})
     table_body = bright_star_table.find('tbody')
     table_rows = table_body.find_all('tr')

     for row in table_rows:
          table_cols = row.find_all('td')
          print(table_cols)
    
