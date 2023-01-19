class Movies: # This "movies" class is the parent
    duration = "120 min"
    genre = 'horror'
    film_year = '2015'


class studios(Movies): # The "studios" class is one that inherits the parent one
    number_of_films = 600
    budgets = '20 million'
    earnings = '2.3 million'
    company = 'Lions Gate'



class director(Movies): # 2nd child class
    movies_directed = '26'
    coDirected = '4 films'
    school = 'Duke'
    highest_nominated_award = 'Grammy'



class actor(Movies): # And this is the third class that inherits the parent
    starred_in = 0
    coStarred_in = 0
    awards = 0
    years_acting = 0

# All classes each have one or more attributes to them


x = director()

if __name__ == "__main__":
    Movies()
    print("Mel went to " + x.school + " college.")
    print("Mel directed " x.movies_directed " films for " + x.company + " personally.")
    
    
