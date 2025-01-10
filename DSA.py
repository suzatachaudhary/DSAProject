class User:
    def __init__(self,name, email, password):
        self.email = email
        self.password = password
        self.name= name

class UserManager:
    def __init__(self):
        self.users = {}  # Dictionary to store users as email-password pairs

    def add_user(self, name, email, password):
        if email in self.users:
            print(f"User with email {email} already exists.")
            return False  # User already exists
        self.users[email] = User(name, email, password)
        print(f"User {name} with email {email} added successfully.")
        return True

    def authenticate_user(self, email, password):
      if email in self.users:
        return email in self.users and self.users[email].password == password
      return False
    
    def get_user_name(self, email):
        user = self.users.get(email)
        if user:
            return user.name
        return None

class Movie:
    def __init__(self, title, total_seats):
        self.title = title
        self.total_seats = total_seats
        self.available_seats = [[True] * 10 for _ in range(total_seats // 10)]  # 2D seat grid

    def book_seat(self, row, col):
      if 0 <= row < len(self.available_seats) and 0 <= col < len(self.available_seats[0]):
        if self.available_seats[row][col]:
            self.available_seats[row][col] = False
            return True  # Booking successful
        return False  # Seat already booked

    def get_available_seats(self):
        return sum(row.count(True) for row in self.available_seats)

    def display_seats(self):
        return [
            ["0" if seat else "X" for seat in row] for row in self.available_seats
        ]


class MovieBookingSystem:
    def __init__(self):
        self.users = UserManager() # Initialize UserManager to manage users
        self.movies = {}  # Dictionary to store movie objects

    # User management
    def add_user(self, name, email, password):
        return self.users.add_user(name,email,password)

    def authenticate_user(self, email, password):
        return self.users.authenticate_user(email, password)

    # Movie management
    def add_movie(self, title, total_seats):
        self.movies[title] = Movie(title, total_seats)

    def book_seat(self, title, row, col):
        if title in self.movies:
            return self.movies[title].book_seat(row, col)
        return False  # Movie not found

    def get_movie_details(self, title):
        if title in self.movies:
            movie = self.movies[title]
            print("Seat layout:", movie.display_seats())  # Debugging line
            print("Available seats:", movie.get_available_seats())  # Debugging line
            return {
                "title": movie.title,
                "available_seats": movie.get_available_seats(),
                "seat_layout": movie.display_seats(),
            }
        return None


class MovieManager:
    def __init__(self):
        self.movies = [
            {
                'id': '1',
                'title': 'Yeh Jawaani Hai Deewani',
                'description': 'Explores different friendship dynamics through Bunny-Aditi and Avi-Bunny & Naina.',
                'genre': 'Romantic Comedy',
                'rating': '9.8',
                'image_url': 'static/images/YJHD.jpeg',
                'available_seats':50,
                'seat_layout':[['0'] * 10 for _ in range(5)]
            },
            {
                'id': '2',
                'title': 'Romeo and Juliet',
                'description': 'a tragic love story where the two main characters, Romeo and Juliet, are supposed to be sworn enemies but fall in love',
                'genre': 'Romance',
                'rating': '9.5',
                'image_url': 'static/images/RomeoAndJuliet.jpeg',
                'available_seats':50,
                'seat_layout':[['0'] * 10 for _ in range(5)]
                
            },
            {
                'id': '3',
                'title': 'Sita Raman',
                'description': 'The story of love between an Indian Army officer and a woman, set against the backdrop of Indo-Pak tensions in the 1960s.',
                'genre': 'Action, Mystery & Romance',
                'rating': '9.0',
                'image_url': 'static/images/SitaRaman2.jpg',
                'available_seats':50,
                'seat_layout':[['0'] * 10 for _ in range(5)]
            },
            {
                'id': '4',
                'title': 'Rockstar',
                'description': 'Rockstar is a 2011 movie about a college student who becomes an international rock star',
                'genre': 'Drama , music & Romance',
                'rating': '8.0',
                'image_url': 'static/images/Rockstar.jpg',
                'available_seats':50,
                'seat_layout':[['0'] * 10 for _ in range(5)]
            },
            {
                'id': '5',
                'title': 'Moana',
                'description': ' Disney animated action-adventure musical film about a Polynesian teenager who sets sail to save her peopl',
                'genre': ' Animation, adventure, comedy, family, fantasy, musical',
                'rating': '9.5',
                'image_url': 'static/images/Moana.jpg',
                'available_seats':50,
                'seat_layout':[['0'] * 10 for _ in range(5)]
            },
            {
                'id': '6',
                'title': 'Harry potter',
                'description': 'a series of fantasy films that also include elements of adventure, family, drama, mystery, and coming-of-age fiction: ',
                'genre': 'Fantasy, adventure, family, drama, mystery',
                'rating': '9.3',
                'image_url': 'static/images/Harryporter.jpg',
                'available_seats':50,
                'seat_layout':[['0'] * 10 for _ in range(5)]
            },
            {
                'id': '7',
                'title': 'Bhool bhulaiya',
                'description': ' Indian Hindi-language psychological comedy horror ',
                'genre': 'Comedy and horror',
                'rating': '8.7',
                'image_url': 'static/images/Bhool.jpg',
                'available_seats':50,
                'seat_layout':[['0'] * 10 for _ in range(5)]
            },
            {
                'id': '8',
                'title': 'The notebook',
                'description': 'romantic drama film about a young couple love story in the 1940s',
                'genre': 'love and Romance',
                'rating': '9.0',
                'image_url': 'static/images/TheNotebook.jpg',
                'available_seats':50,
                'seat_layout':[['0'] * 10 for _ in range(5)]
            }
        ]

    def get_all_movies(self):
        return self.movies
    def get_movie_by_id(self, movie_id):
        # Logic to find and return the movie details by movie_id
        # Assuming movies is a list of dictionaries
        for movie in self.movies:
            if movie['id'] == movie_id:
              return movie
        return None  # If the movie is not found"""

    def book_movie(self, movie_id):
      movie = self.get_movie_by_id(movie_id)
      if movie:
        for row_idx, row in enumerate(movie['seat_layout']):
            for col_idx, seat in enumerate(row):
                if seat == '0':  # An available seat
                    movie['seat_layout'][row_idx][col_idx] = 'X'  # Book the seat
                    movie['available_seats'] -= 1
                    return {
                        "status": "success",
                        "message": f"Seat booked at Row {row_idx + 1}, Column {col_idx + 1}"
                    }
      return {"status": "error", "message": "No seats available or invalid movie ID"}
    
    def search_movies(self, query):
        """Search movies by title or part of the title."""
        return [
            movie for movie in self.movies
            if query.lower() in movie['title'].lower()
        ]
   
             
        
    
