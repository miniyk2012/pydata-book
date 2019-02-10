# MovieLens 1M data set

import pandas as pd
import os
import re


encoding = 'latin1'

upath = os.path.expanduser('ch02/movielens/users.dat')
rpath = os.path.expanduser('ch02/movielens/ratings.dat')
mpath = os.path.expanduser('ch02/movielens/movies.dat')

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

users = pd.read_csv(upath, sep='::', header=None, names=unames, encoding=encoding)
ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, encoding=encoding)
movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, encoding=encoding)

data = pd.merge(pd.merge(ratings, users), movies)

print(data.title.loc[372300])
title = data.title
# https://stackoverflow.com/questions/20078816/replace-non-ascii-characters-with-a-single-space/39059279
for i, row in enumerate(title):
    try:
        row.decode('ascii')
    except UnicodeDecodeError:
        # row = re.sub(r'[^\x00-\x7F]+',' ', row)
        row = "".join(i for i in row if ord(i) < 128)
        title.iloc[i] = row
data.title = title
print(data.title.loc[372300])

mean_ratings = data.pivot_table('rating', index='title',
                                columns='gender', aggfunc='mean')


