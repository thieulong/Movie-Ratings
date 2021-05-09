# Movie-Ratings
A script to crawl movie ratings online (IMDB &amp; Rotten Tomatoes) along with movie genres.
### 1. Install Github & clone the script
Firstly, to clone this script, you'll need to install Github to your device. Follow [this link](https://github.com/git-guides/install-git) for more!  
Note: Remember to check your OS (Operating system)  
Next, you'll need to config your Github account in your device, seek for further assist [here](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration).  
Once you've done that, let's move to the next step where you'll have to open your Command Prompt or Terminal to clone the script. Once you've open the Command Prompt / Terminal, type `git clone https://github.com/thieulong/Movie-Ratings.git` and wait for the script to be cloned successfully.
### 2. Install Python
After having Github installed, you must have [Python](https://en.wikipedia.org/wiki/Python_(programming_language) installed on your device because this is all written in Python.  
To download Python, check out this [link](https://www.python.org/downloads/), this script is written in Python 3.9.2.  
### 3. Install Requirements
Open your Command Prompt or Terminal to this directory (Movie-Ratings) using `cd`  
Afterthat, type `pip3 install requirements.txt` into the Command Prompt / Terminal  
### 4. Pick your movies
After you have picked a list of movies. Open the movies.txt text file and write the movie title, each by each, line by line.  
Note: In order to let the script able to search for your movies better, append release year in parentheses after each of the movie title as the examples below:  
```
Avengers: Endgame (2019)
The Book of Life (2014)
```
### 5. Run the script
Open the Command Prompt / Terminal you have opened in step 3. (Redo the step again in case you have closed it, but don't need to type `pip3 install requirements.txt`)  
Type `python3 movie_ratings.py` and wait for the results. Expected will be a table displayed IMDB and Rotten Tomatoes score, along with each movie's genre.  
