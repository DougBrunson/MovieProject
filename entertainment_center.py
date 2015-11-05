import media
import fresh_tomatoes

ateam = media.Movie("The A-team", 
					"Iraq War veterans look to clear their name.", 
					"http://ia.media-imdb.com/images/M/MV5BMTc4ODc4NTQ1N15BMl5BanBnXkFtZTcwNDUxODUyMw@@._V1__SX1537_SY757_.jpg",
					"https://www.youtube.com/watch?v=exyzEFrmLuM")


ironman = media.Movie("Iron Man", 
					"Tony Stark fights evil",
					"http://www.simbasible.com/wp-content/uploads/2015/09/Iron-Man1.jpg",
					"https://www.youtube.com/watch?v=8hYlB38asDY")


fast_five = media.Movie("Fast & Furious 5",
						"Street racers plan a massive heist",
						"http://resizing.flixster.com/Pk5Sb5BTZDmlonljKc47fyjr3s8=/800x1200/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/30/11173000_ori.jpg",
						"https://www.youtube.com/watch?v=vcn2GOuZCKI")

hangover = media.Movie("The Hangover",
						"Bachelor party gone right.",
						"http://resizing.flixster.com/4ZdUmCYzIx8pWqjBhOUNaSMkeCI=/800x1200/dkpu1ddg7pbsk.cloudfront.net/movie/11/16/67/11166717_ori.jpg",
						"https://www.youtube.com/watch?v=tcdUhdOlz9M")

	
gladiator = media.Movie("The Gladiator", 
						"A Roman General becomes a gladiator to exact revenge",
						"https://www.movieposter.com/posters/archive/main/22/A70-11370",
						"https://www.youtube.com/watch?v=owK1qxDselE")

limitless = media.Movie("Limitless",
						"A struggling writer becomes a financial wizard",
						"https://upload.wikimedia.org/wikipedia/en/1/17/Limitless_Poster.jpg",
						"https://www.youtube.com/watch?v=jOLqNOfzus4")


movies = [ateam, ironman, fast_five, hangover, gladiator, limitless] 

fresh_tomatoes.open_movies_page(movies)