# The-Data-Incubator-Capstone-Project

## Introduction
The project I propose to work on while at The Data Incubator aims to quantify the variation of cinematic gender representation in the past decade, especially after the 2008 Great Recession.

Cultural studies scholars have accused the early Hollywood movies of fortifying traditional images of women and men. However, there have been tremendous gains for gender equality in many spheres of American life including in the entertainment industry and cinematic representation. Inspired by recent editorials about emasculated female roles in some films, I want to systematically search for quantitative evidence about the gender representation in the American films, and to better understand how women and men are portrayed in contemporary films.

This project will help us to understand the general trend of gender representation in American mainstream entertainment. It will also serve as a benchmark for gender construction studies using empirical data and computational content analysis methods.

## Methods
To conduct this research, I used natural language processing techniques, specifically, Word2Vec and Doc2Vec models, to analyze the female and male roles in films through time.

There are three aspects of analysis I’m focusing on: 
⋅⋅1. Study the semantic similarities of chick flicks and non chick flicks over time, to analyze the development of content for chick flicks; 
⋅⋅2. Study the yearly semantic change of words “woman, ” ‘’man,” “wife,” “husband,” “mother” and “father” in chick flicks and non chick flicks, to compare the difference of development for male and female roles between chick flicks and non chick flicks;
⋅⋅3. Define two lists of words indicating traditional masculine traits and feminine traits, and analyze the semantic distance of these traits to female and male roles over time, to study the variation of female and male images in films.

## Data
The film data for this project was retrieved from Internet Movie Database (IMDb), including a historical data dump at ftp://ftp.funet.fi/pub/mirrors/ftp.imdb.com/pub/frozendata, a daily refreshed data dump maintained by [Amazon S3](https://datasets.imdbws.com/), and data collected using unofficial IMDb Python API [IMDbPY](https://imdbpy.sourceforge.io/). 

Among 31,344 U.S. narrative feature films released between 2007 and 2017, I obtained in total 15,719 films with available plot summaries or synopses, and information including film title, country, runtime, released year, the gender of top-billing role, and genre.

## Scripts
**I have written several scripts to collect, clean, transform, and analyze the data.**

### 1_extract_valid_movies (SQL & Python)
After downloading the raw datasets from ftp://ftp.funet.fi/pub/mirrors/ftp.imdb.com/pub/frozendata, I parsed them into a SQLite database using a [script](https://github.com/alberanid/imdbpy/blob/master/bin/imdbpy2sql.py) supported by IMDbPY. The database is 9.15 GB.

Then I filtered the U.S. feature narrative movies released between 2007 and 2017. Since this data dump does not contain IMDbID, a unique movie id identifying each movie on imdb.com, I matched the filtered movies with those in the Amazon S3 data dump and obtained the IMDbID for each movie.

### 2_fetch_synopsis.py (Python)
Because neither of the data dumps contains film synopsis data, I used IMDbPY to collect synopsis for each movie based on the IMDbID obtained from the previous step.

### 3_extract_info (SQL & Python)
I collected genre, gender of the top-billing role and longest plot for each movie from the SQLite database. The 3 cleaned data files ready for analysis are `films.csv`, `genre.csv`, and `top_billing.csv`.

### 4_analysis.ipynb (Python)
In this Jupyter Notebook, I did some preliminary analysis including generating the two plots required in the SemiFinal Challenge.
