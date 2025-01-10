from flask import Flask, render_template, request, redirect, url_for, flash, session
from DSA import UserManager,MovieBookingSystem, MovieManager
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize user and movie managers
user_manager = UserManager()
movie_manager = MovieManager()
booking_system=MovieBookingSystem()

booking_system.add_movie("Yeh Jawaani Hai Deewani", 100)
booking_system.add_movie("Romeo and Juliet", 100)
booking_system.add_movie("Sita Raman", 100)

# Allowed domains for email
ALLOWED_DOMAINS = ['paruluniversity.ac.in']

# Email domain validation function
def is_valid_email(email):
    domain = email.split('@')[-1]
    return domain in ALLOWED_DOMAINS

# Sign In Route
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Get form data
        email = request.form['email']
        password = request.form['password']

        # Validate email domain
        if not is_valid_email(email):
            flash('Please use an email address from an allowed domain (e.g., @paruluniversity.ac.in)')
            return redirect(url_for('signin'))

        # Check if user exists and password matches
        if not user_manager.authenticate_user(email, password):
            flash('Invalid email or password. Please try again.')
            return redirect(url_for('signin'))
        
        session['user']={'name': user_manager.get_user_name(email), 'email': email}
        flash('Login successful!')
        return redirect(url_for('home'))

    return render_template('signin.html')

# Sign Up Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match. Please try again.')
            return redirect(url_for('signup'))

        # Check if email is valid
        if not is_valid_email(email):
            flash('Please use an email address from an allowed domain (e.g., @paruluniversity.ac.in)')
            return redirect(url_for('signup'))

        # Add user to the data structure
        if not user_manager.add_user(name, email, password):
            flash('User with this email already exists. Please try signing in.')
            return redirect(url_for('signup'))

        flash('Sign up successful! Please sign in.')
        return redirect(url_for('signin'))

    return render_template('signup.html')

# Home Route (After Sign In)
@app.route('/home')
def home():
    if 'user' not in session:
        flash('Please sign in to access this page.')
        return redirect(url_for('signin'))
    user = session['user']
    movies = movie_manager.get_all_movies()
    return render_template('home.html', movies=movies,user=user)

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out successfully.')
    return redirect(url_for('signin'))

# Book Movie Route
@app.route('/book/<movie_id>', methods=['POST'])
def book_movie(movie_id):
    # Simulate booking logic
    print(f"Attempting to book movie with ID: {movie_id}")
    if movie_manager.book_movie(movie_id):
        print("Booking successful")
        flash('Movie booked successfully!')
    else:
        print("Booking failed")
        flash('Failed to book the movie. Please try again.')
    return redirect(url_for('BookingStatus', movie_id=movie_id))

@app.route('/Booknow')
def Booknow():
    movies = movie_manager.get_all_movies()
    return render_template('Booknow.html', movies=movies)

@app.route('/about')
def about():
    return render_template('about.html', current_year=2025)

@app.route('/BookingStatus/<movie_id>')
def BookingStatus(movie_id):
    movie_details = movie_manager.get_movie_by_id(movie_id)
    if movie_details:
        seat_layout=movie_details.get('seat_layout',[])
        available_seats=movie_details.get('available_seats')
        return render_template(
            'BookingStatus.html',
            movie_id=movie_id,
            available_seats=movie_details.get('available_seats'),  # If available_seats exists, show it, otherwise 'N/A'
            seat_layout=movie_details.get('seat_layout')  # Same for seat_layout
        )
    else:
        return "Movie not found", 404

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')  # Get the search query from the URL
    search_results = movie_manager.search_movies(query) if query else []  # Call search function
    return render_template('search.html', movies=search_results, query=query)


if __name__ == '__main__':
    app.run(debug=True)
