import random
import time


def main():
    film_names = [
        "The Shawshank Redemption", "The Godfather", "Pulp Fiction", "Fight Club", "Inception",
        "The Dark Knight", "Goodfellas", "The Matrix", "Forrest Gump", "The Lord of the Rings: The Fellowship of the Ring",
        "The Lion King", "The Avengers", "Interstellar", "Gladiator", "The Departed", "The Prestige",
        "The Social Network", "Blade Runner", "Casino", "The Silence of the Lambs", "The Shining",
        "Eternal Sunshine of the Spotless Mind", "The Big Lebowski", "The Green Mile", "The Truman Show",
        "The Sixth Sense", "The Grand Budapest Hotel", "The Revenant", "The Departed", "The Princess Bride",
        "The Terminator", "The Great Gatsby", "The Wolf of Wall Street", "The Big Short", "The Hangover",
        "The Dark Knight Rises", "The Conjuring", "The Exorcist", "The Godfather: Part II", "Back to the Future",
        "The Bourne Identity", "The Incredibles", "The Pianist", "The Notebook", "The Breakfast Club",
        "The Sound of Music", "The Wizard of Oz", "The Jungle Book", "The Little Mermaid", "The Lion King",
        "The Nightmare Before Christmas", "The Matrix Reloaded", "The Matrix Revolutions", "The Matrix Resurrections",
        "The Lord of the Rings: The Two Towers", "The Lord of the Rings: The Return of the King",
        "The Hobbit: An Unexpected Journey", "The Hobbit: The Desolation of Smaug", "The Hobbit: The Battle of the Five Armies",
        "The Avengers: Endgame", "The Avengers: Infinity War", "The Avengers: Age of Ultron"
    ]

    for _ in range(60):
        film_name = random.choice(film_names)
        print(film_name)
        time.sleep(1)


if __name__ == '__main__':
    main()
