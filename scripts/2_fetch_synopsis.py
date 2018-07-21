from imdb import IMDb
import numpy as np
import pandas as pd

valid_movies = pd.read_csv('valid_movies.csv')
movie_synopsis = pd.DataFrame(columns=['tconst', 'id', 'primaryTitle', 'originalTitle', 'year', 'runtimeMinutes', 'synopsis'])

i = 0
ia = IMDb()
for index, row in valid_movies.iterrows():
    imdb_id = row['tconst'][2:]
    movie = ia.get_movie(imdb_id)
    country = movie.get('country')
    if country != None and country[0] == 'United States':
        synopsis = movie.get('synopsis')
        if synopsis != None:
            append_row = valid_movies.loc[index, :].tolist()
            append_row.append(synopsis[0])
        else:
            append_row = valid_movies.loc[index, :].tolist()
            append_row.append(np.nan)
        movie_synopsis.loc[i] = append_row
        print(i)
        i += 1

movie_synopsis.to_csv('movie_synopsis.csv', index=False)