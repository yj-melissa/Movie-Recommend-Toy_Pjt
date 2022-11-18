import requests
import json

TMDB_API_KEY = '81d72b8b58e4b26b26aae316e0bbad5c'

def get_movie_datas():
    total_data = []

    count = 1
    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 10):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                movie_dict = {
                    "model" : "servers.movie",
                    "pk": count,
                    'fields' : {
                    'title': movie.get('title'),
                    'overview': movie['overview'],
                    'id' : movie.get('id'),
                    'genre_ids': movie.get('genre_ids'),
                    'adult' : movie.get('adult'),
                    'backdrop_path' : movie.get('backdrop_path'),
                    'original_language': movie.get('original_language'),
                    'popularity' :  movie.get('popularity'),
                    'poster_path' : movie.get('poster_path'),
                    'release_date' : movie.get('release_date'),
                    'vote_average' : movie.get('vote_average') 
                    }
                }

                count+=1
                
                total_data.append(movie_dict)

    with open("back-side/servers/fixtures/movie_data.json", "w", encoding="utf-8") as make_file:
        json.dump(total_data, make_file, indent="\t", ensure_ascii=False)

get_movie_datas()