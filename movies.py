class Movies: # This "movies" class is the parent
    duration = '120 min'
    genre = 'horror'
    film_year = '2015'


class studios(): # The "studios" class is one that inherits the parent one
    number_of_films = 600
    budgets = '20 million'
    earnings = '2.3 million'
    company = 'Lions Gate'



class director(): # 2nd child class
    name = 'UCLA'
    movies_directed = '36'
    coDirected = '4 films'
    school = 'Duke'
    highest_nominated_award = 'Grammy'



class actor(): # And this is the third class that inherits the parent
    name = 'Jim Carey'
    starred_in = 0
    coStarred_in = 0
    awards = 12
    years_acting = 30

# All classes each have one or more attributes to them

x = Movies()


if __name__ == "__main__":
    x = director()
    a = Movies()
    b = studios()
    print("Mel went to " + x.name + " college and directed over " + x.movies_directed + " films. Also he co-directed " + x.coDirected + " with " + b.company + ".")
    
    z = actor()
    print("The actor {} has been acting for {} years, and has won over {} awards".format(z.name,z.years_acting,z.awards))
