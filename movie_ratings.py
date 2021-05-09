from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from rotten_tomatoes_scraper.rt_scraper import MovieScraper
import re

movie_file = 'movies.txt'

option = webdriver.ChromeOptions()
option.add_argument('headless')

chromedriver_linux = '/usr/bin/chromedriver'
chromedriver_window = 'C:\\Users\\Lorca\\AppData\\Local\\Google\\Chrome\\chromedriver.exe'
chromedriver_mac = '/usr/local/bin/chromedriver'

chromedriver = chromedriver_mac

with open(movie_file) as file:
    movie_list = [movie.rstrip() for movie in file]


def format_movie_title(movie_title):

    movie_title = re.sub('[^A-Za-z0-9]+', ' ', movie_title)
    movie_title = movie_title.lower()
    movie_title = movie_title.split()
    movie_title = "_".join(movie_title)

    return movie_title


def capitalize(wordlist):

    result = list()

    for i in range(len(wordlist)):
        result.append(wordlist[i].title())

    return result


def rotten_tomatoes_score(movie, release_year):

    formatted_movie_title = format_movie_title(movie_title=movie)

    try:
        movie_scraper = MovieScraper(movie_title = movie)
        
    except Exception:
        try:
            url = "https://www.rottentomatoes.com/m/{movie}".format(movie = formatted_movie_title)
            movie_scraper = MovieScraper(movie_url = url)

        except Exception:
            url = "https://www.rottentomatoes.com/m/{movie}_{year}".format(movie = formatted_movie_title, year = release_year)
            movie_scraper = MovieScraper(movie_url = url)

    else:
        movie_scraper.extract_metadata()
        tomatometer = movie_scraper.metadata["Score_Rotten"]
        audience = movie_scraper.metadata["Score_Audience"]
        genre = movie_scraper.metadata["Genre"]

        return [tomatometer, audience, genre]


def imdb_score(movie, release_year):

    driver = webdriver.Chrome(chromedriver, options=option)

    driver.get("https://www.imdb.com/")

    searchbox = driver.find_element_by_id("suggestion-search")
    searchbox.click()

    try:
        searchbox.send_keys("{movie}\n".format(movie=movie))

    except Exception:
        searchbox.send_keys("{movie} ({year})\n".format(movie=movie, year=release_year))
    
    else:
        select = driver.find_element_by_link_text('{link}'.format(link=movie))
        select.click()

        score = driver.find_element_by_xpath("//span[@itemprop='ratingValue']")
        score = score.text 

        driver.quit()
        return score


def create_table(movie_list):

    print("|"+"-"*200+"|")
    print("|", "|".rjust(42), "|".rjust(22), "Rotten Tomatoes".center(50), "|", "|".rjust(81))
    print("|", "Movie title".center(40), "|", "IMDB".center(20), "|", "-"*50, "|", "Genres".center(80)+"|")
    print("|", "|".rjust(42), "|".rjust(22), "Tomatometer".center(25), "|", "Audience Score".center(22), "|", "|".rjust(81))
    print("|"+"-"*200+"|")

    for i in range(len(movie_list)):

        movie = movie_list[i]
        year = movie[movie.find("(")+1:movie.find(")")]
        movie_title = re.sub("[\(\[].*?[\)\]]", "", movie)
        movie_title = movie_title.strip()

        tomatometer, audience, genre = rotten_tomatoes_score(movie=movie_title, release_year=year)

        if tomatometer != "":
            tomatometer = str(tomatometer)+"%"

        else:
            tomatometer = ""

        if audience != "":    
            audience = str(audience)+"%"
        
        else:
            audience = ""

        genre = capitalize(genre)
        genre = ", ".join(genre)

        imdb = imdb_score(movie=movie_title, release_year=year)
        imdb = imdb+"/10"

        print("|"+" "*200)
        print("|",movie.ljust(40), imdb.center(23), tomatometer.center(25), audience.center(27), genre.ljust(0))
        print("|"+" "*200)
        print("|"+"-"*200+"|")


create_table(movie_list=movie_list)
