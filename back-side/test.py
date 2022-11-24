import requests
import json

TMDB_API_KEY = '81d72b8b58e4b26b26aae316e0bbad5c'

def get_movie_datas():
    total_data = []

    genres = [
        {
            "id": 28,
            "name": "액션"
        },
        {
            "id": 12,
            "name": "모험"
        },
        {
            "id": 16,
            "name": "애니메이션"
        },
        {
            "id": 35,
            "name": "코미디"
        },
        {
            "id": 80,
            "name": "범죄"
        },
        {
            "id": 99,
            "name": "다큐멘터리"
        },
        {
            "id": 18,
            "name": "드라마"
        },
        {
            "id": 10751,
            "name": "가족"
        },
        {
            "id": 14,
            "name": "판타지"
        },
        {
            "id": 36,
            "name": "역사"
        },
        {
            "id": 27,
            "name": "공포"
        },
        {
            "id": 10402,
            "name": "음악"
        },
        {
            "id": 9648,
            "name": "미스터리"
        },
        {
            "id": 10749,
            "name": "로맨스"
        },
        {
            "id": 878,
            "name": "SF"
        },
        {
            "id": 10770,
            "name": "TV 영화"
        },
        {
            "id": 53,
            "name": "스릴러"
        },
        {
            "id": 10752,
            "name": "전쟁"
        },
        {
            "id": 37,
            "name": "서부"
        }
    ]

    count = 1
    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 200):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            actor_request_url = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
            actors = requests.get(actor_request_url).json()

            if movie.get('vote_count') < 20:
                pass
            
            else:
                if movie.get('release_date'):
                    if int(movie.get('release_date')[0:4]) > 2023:
                        pass
                    else:
                        genre_list = []
                        for i in movie.get('genre_ids'):
                            for j in genres:
                                if j['id'] == i:
                                    genre_list.append(j['name'])

                        for crew in actors['crew']:
                            if crew.get("department")=="Directing" and crew.get("job")== "Director":
                                director = crew

                        movie_dict = {
                            "model" : "servers.movie",
                            "pk": count,
                            'fields' : {
                            'title': movie.get('title'),
                            'overview': movie['overview'],
                            'id' : movie.get('id'),
                            'genre_ids': genre_list,
                            'adult' : movie.get('adult'),
                            'backdrop_path' : movie.get('backdrop_path'),
                            'original_language': movie.get('original_language'),
                            'popularity' :  movie.get('popularity'),
                            'poster_path' : movie.get('poster_path'),
                            'release_date' : movie.get('release_date'),
                            'vote_average' : movie.get('vote_average'),
                            'actors' : actors['cast'],
                            'director' : director
                            },
                            
                        }

                        count+=1
                            
                        total_data.append(movie_dict)            

    with open("back-side/servers/fixtures/movie_data.json", "w", encoding="utf-8") as make_file:
        json.dump(total_data, make_file, indent="\t", ensure_ascii=False)

get_movie_datas()
