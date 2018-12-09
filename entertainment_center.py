import json
import fresh_tomatoes
import media

movie_list = []
json_file = open('movie_list.json', 'r')
json_data = json.load(json_file)

# Read movie data from movie_list.json and populate movie_list

for data in json_data:
    movie_list.append(media.Movie(data['title'],
                                  data['overview'],
                                  data['poster_image_url'],
                                  data['trailer_youtube_url']))

json_file.close()

# Create website using movie_list as data source

fresh_tomatoes.open_movies_page(movie_list)
