import media
import fresh_tomatoes

toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys that come to life",
                        "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_.jpg",
                        "https://www.youtube.com/watch?v=v-PjgYDrg70&ab_channel=RottenTomatoesClassicTrailers")

print (toy_story.storyline)

avatar = media.Movie("Avatar",
                        "A marine on alien planet",
                        "https://m.media-amazon.com/images/I/61OUGpUfAyL._AC_SY741_.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY&ab_channel=20thCenturyStudios")

print (avatar.storyline)

hangover= media.Movie("Hangover",
                        "Drunk guys try to find out what happened on the party",
                        "https://m.media-amazon.com/images/M/MV5BNGQwZjg5YmYtY2VkNC00NzliLTljYTctNzI5NmU3MjE2ODQzXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
                        "https://www.youtube.com/watch?v=tcdUhdOlz9M&ab_channel=RottenTomatoesClassicTrailers")

print (hangover.storyline)
hangover.show_trailer();

movies = [toy_story, avatar, hangover]
fresh_tomatoes.open_movies_page(movies)
