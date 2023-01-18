class movies: # This "movies" class is the parent
    duration = ''
    genre = ''
    year = ''


class studios(movies): # The "studios" class is one that inherits the parent one
    number_of_films = ''
    budgets = ''
    earnings = ''
    company = ''



class director(movies): # 2nd child class
    movies_directed = ''
    coDirected = ''
    school = ''
    highest_nominated = ''



class actor(movies): # And this is the third class that inherits the parent
    starred_in = ''
    coStarre_in = ''
    awards = ''
    years_acting = ''

# All classes each have one or more attributes to them



print(actor)
    
    
