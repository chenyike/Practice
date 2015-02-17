def create_actors_DB(actor_file):
    '''Create a dictionary keyed on actors from a text file'''
    f = open(actor_file)
    movieInfo = {}
    for line in f:
        line = line.rstrip().lstrip()   # remove the space before and after the list
        actorAndMovies = line.split(',') # split the list into individual items
        actor = actorAndMovies[0] # get the actor name in the list

        '''Leo: Titanic, Leo, The Departed''' # when it sees Leo the second time, it does not touch the keys
        if actor not in movie.info.keys():
            movieIfo[actor]=set([])  # to Avoid potential repetition
            
        movies = actorAndMovies[1:] # to get the movie list behind the actor 
        cleaned_movies = []  # get individual movie out from the movie list
        for movie in movies:
            cleaned_movies.append(movie.lstrip().rstrip()) 
        movieInfo[actor] = movieInfo.get(actor).union(set(cleaned_movies))
    f.close()
    return movieInfo


