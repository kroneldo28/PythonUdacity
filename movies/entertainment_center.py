import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", "http://www.youtube.com/watch?v=-9ceBgWV8io")

#print(avatar.storyline)
#avatar.show_trailer()

the_pursuit_of_happyness = media.Movie("The Pursuit Of Happyness", "A man struggling to find success", "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/Poster-pursuithappyness.jpg/220px-Poster-pursuithappyness.jpg", "https://www.youtube.com/watch?v=00uTFVnWJMw")

#the_pursuit_of_happyness.show_trailer()

hunger_games = media.Movie("Hunger Games", "Storyline", "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", "https://www.youtube.com/watch?v=PbA63a7H0bo")

midnight_in_paris = media.Movie("Midnight in Paris", "Storyline", "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", "https://www.youtube.com/watch?v=atLg2wQQxvU")

ratatouille = media.Movie("Ratatouille", "Storyline", "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", "https://youtube.com/watch?v=c3sBBRxDAqk")

movies = [toy_story, avatar, the_pursuit_of_happyness, hunger_games, midnight_in_paris, ratatouille]
fresh_tomatoes.open_movies_page(movies)
