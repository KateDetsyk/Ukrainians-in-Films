from imdb import IMDb
ia = IMDb()


actors_list = []
with open('actors.txt') as f:
    for line in f:
        actors_list.append(f.readline().replace('\n', ''))
        
file = {}
for actor in actors_list:
    for person in ia.search_person(actor):
        if person['name'] == actor:
            person_found = person
            ia.update(person_found)
            person_found.get_titlesRefs()
            
        movies_lst = person_found.titlesRefs.keys()
        file[person] = movies_lst
print(file)
