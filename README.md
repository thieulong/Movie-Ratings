# Movie-Ratings
A script to crawl movie ratings online (IMDB &amp; Rotten Tomatoes) along with movie genres.
### 1. Install Github & clone the script
Firstly, to clone this script, you'll need to install Github to your device. Follow [this link](https://github.com/git-guides/install-git) for more!  
  
Note: Remember to check your OS (Operating system)  
  
Next, you'll need to config your Github account in your device, seek for further assist [here](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).  
  
Once you've done that, let's move to the next step where you'll have to open your Command Prompt or Terminal to clone the script. Once you've open the Command Prompt / Terminal, type `git clone https://github.com/thieulong/Movie-Ratings.git` and wait for the script to be cloned successfully.  
  
### 2. Install Python
After having Github installed, you must have [Python](https://www.python.org/doc/essays/blurb/) installed on your device because this is all written in Python.  
  
To download Python, check out this [link](https://www.python.org/downloads/), this script is written in Python 3.9.2.  
  
### 3. Install Requirements
Open your Command Prompt or Terminal to this directory (Movie-Ratings) using `cd`  
  
Afterthat, type `pip3 install requirements.txt` into the Command Prompt / Terminal  
  
Then, you'll need to install Chromedriver to run the script, you can figure out the proper Chromedriver version which is also your current Chrome version [here](https://help.zenplanner.com/hc/en-us/articles/204253654-How-to-Find-Your-Internet-Browser-Version-Number-Google-Chrome)  
  
Having done that, you can then download the Chromedriver in [here](https://chromedriver.chromium.org/downloads) (Remember to choose the version closest with the version you've found out above  
  
### 4. Pick your movies
After you have picked a list of movies. Open the movies.txt text file and write the movie title, each by each, line by line.  
  
Note: In order to let the script able to search for your movies better, append release year in parentheses after each of the movie title as the examples below:  
  
```
Avengers: Endgame (2019)
The Book of Life (2014)
La La Land (2016)
```
  <img width="699" alt="Screen Shot 2021-05-09 at 22 42 27" src="https://user-images.githubusercontent.com/59945736/117578531-01f40480-b119-11eb-9822-0751605f0d07.png">

### 5. Run the script
Open the script file (movie_ratings.py) and adjust the line 16 based on your current OS (If you're using Window, replace line 16 with `chromedriver = chromedriver_window` and so on with Linux and MacOS)  
    
Finally, open the Command Prompt / Terminal you have opened in step 3. (Redo the step again in case you have closed it, but don't need to type `pip3 install requirements.txt`)  
  
Type `python3 movie_ratings.py` and wait for the results. Expected will be a table displayed IMDB and Rotten Tomatoes score, along with each movie's genre.  
  
<img width="1440" alt="Screen Shot 2021-05-09 at 22 45 45" src="https://user-images.githubusercontent.com/59945736/117578537-0b7d6c80-b119-11eb-8074-6996933c883e.png">
