import media
import fresh_tomatoes

# This code creates the objects representing the movies I want to display

totoro = media.Movie("My Neighbor Totoro", 
	"A story of two girls who meet a fantastic creature",
	"https://upload.wikimedia.org/wikipedia/en/thumb/0/02/"
		"My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg/"
		"220px-My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg",
	"https://www.youtube.com/watch?v=92a7Hj0ijLs")

mononoke = media.Movie("Princess Mononoke",
	"A girl and a boy from different lands fight for what they believe in",
	"https://upload.wikimedia.org/wikipedia/en/thumb/2/24/"
		"Princess_Mononoke_Japanese_Poster_%28Movie%29.jpg/"
		"220px-Princess_Mononoke_Japanese_Poster_%28Movie%29.jpg",
	"https://www.youtube.com/watch?v=4OiMOHRDs14")

spirited_away = media.Movie("Spirited Away",
	"A girl helps gets lost in a magical land",
	"https://upload.wikimedia.org/wikipedia/en/thumb/3/30/"
		"Spirited_Away_poster.JPG/220px-Spirited_Away_poster.JPG",
	"https://www.youtube.com/watch?v=ByXuk9QqQkk")

nausicaa = media.Movie("Nausicaa of the Valley of the Wind",
	"A girl fights to protect her world from destruction",
	"https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/"
		"Nausicaaposter.jpg/220px-Nausicaaposter.jpg",
	"https://www.youtube.com/watch?v=6zhLBe319KE")

the_cat_returns = media.Movie("The Cat Returns",
	"A girl becomes mixed up with the cat kingdom",
	"https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/"
		"Cat_Returns.jpg/220px-Cat_Returns.jpg",
	"https://www.youtube.com/watch?v=Gp-H_YOcYTM")

the_wind_rises = media.Movie("The Wind Rises",
	"A boy dreams of building airplanes",
	"https://upload.wikimedia.org/wikipedia/en/thumb/a/a3/"
		"Kaze_Tachinu_poster.jpg/220px-Kaze_Tachinu_poster.jpg",
	"https://www.youtube.com/watch?v=jGr8XDxB-9I")

movies = [totoro, mononoke, spirited_away, nausicaa, 
	the_cat_returns, the_wind_rises]

fresh_tomatoes.open_movies_page(movies)