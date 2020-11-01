import threading, time
from enum import Enum


"""
- Must List all cities with cinemas
- Each cinema can have multiple halls and each hall will run only one show at a time
- Each movie will have the multiple shows
- Search movie by title, language, generes, city
- After Selecting the movie it should show the all the cinemas running that movie
- Customer selects the show of movie and books ticket
- Customer can see the seating arrangnment and book the tickets accordingly.
- System should send notifications when there is a movie
- System will ensure same seat is not booked by same user.

Actors in the system
- Admin
- Customer
- Cinema Attendant

Classes in the System
  - Movie
    - Name
    - Desc

  - Cinema
    - Name 
    - Place
    - Add a movie at Hall, Show
    - Add a Hall in Cinema

  - City
    - Add Cinema

  - Ticket
    - Show
    - Seat
  - Halls
    - Maximum Seats
  - Show
    - City
    - Cinema
    - Hall
    - Timing
    - Seats
  - Seats
  - TicketingSystem
  - SearchCatalogue
    - Cinemas
    - Movies to Cinema
    - City to Cinema
    - 
"""
import threading
from enum import Enum


class TicketStatus(Enum):
  """
  Enumeration of the Ticket status
  """
  UNDERPROCESS, FAILED, ACCEPTED = 1, 2, 3

class Movie:
  """
  Blueprint for storing the movie objects
  """

  """
  * @param name: Movie Name
  * @param desc: Movie Description
  """
  def __init__(self, name, desc, cinema, city):
    self.__name = name
    self.__desc = desc
    self.__cinema = cinema
    self.__shows = []
    self.__city = city
    self.__lock = threading.Lock()

  """
  * @param show: Show Object
  """
  def add_show(self, show):
    self.__lock.acquire()
    self.__shows.append(show)
    self.__lock.release()

  def __str__(self):
    return str(self.__name)


class Cinema:
  """
  Blueprint for the Cinema objects
  """

  """
  * @param name: Movie Name
  * @param desc: Movie Description
  * @param city: City Object
  """
  def __init__(self, name, desc, city):
    self.__name = name
    self.__desc = desc
    self.__movies = []
    self.__city = city
    self.__lock = threading.Lock()

  def get_city(self):
    return self.__city
	

  """
  * @param movie: Movie Object
  """
  def add_movie(self, movie):
    self.__lock.acquire()
    self.__movies.append(movie)
    SearchCatalogue.add_movie(movie, self)
    self.__lock.release()

class SearchCatalogue:
  """
  Blueprint for the SearchCatalogue objects
  """
  __instance = None
  
  class __ONLY_ONE:
    def __init__(self):
      self.title_to_movie = {}
      self.movies_to_cinema = {}
      self.cinemas = set([])
      self.city_to_movies = {}
      self.lock = threading.Lock()

  def __init__(self):
    if not SearchCatalogue.__instance:
      SearchCatalogue.__instance = SearchCatalogue.__ONLY_ONE()
  
  """
  * @param movie: Movie Object
  * @param cinema: Cinema Object
  """
  @classmethod
  def add_movie(cls, movie, cinema):
    self = cls.__instance
    self.lock.acquire()
    if movie in self.movies_to_cinema:
      self.movies_to_cinema[movie].add(cinema)
    else:
      self.movies_to_cinema[movie] = set([cinema])
    self.cinemas.add(cinema)

    self.city_to_movies.get(cinema.get_city(), set()).add(movie)
    if str(movie) not in self.title_to_movie:
      self.title_to_movie[str(movie)] = [movie]
    else:
      self.title_to_movie[str(movie)].append(movie)
    self.lock.release()

  @classmethod
  def search_movie_by_title(cls, title):
    self = cls.__instance
    if title in self.title_to_movie:
      for mov in self.title_to_movie[title]:
        print(mov)


class City:
  """
  Blueprint for the City objects
  """

  """
  * @param name: name
  """
  def __init__(self, name):
    self.__name = name
    self.__cinemas = set([])
    self.__lock = threading.Lock()

  """
  * @param cinema: Cinema Object
  * @param param2: 
  """
  def add_cinema(self, cinema):
    self.__lock.acquire()
    self.__cinemas.add(cinema)
    self.__lock.release()

class Show:
  """
  Blueprint for the Show objects
  """

  """
  * @param start_time: Time Object for start time
  * @param end_time: Time Object for end time
  * @param movie: Movie Object
  * @param price: Price per seating
  """
  def __init__(self, start_time, end_time, movie, seating, price):
    self.__start_time = start_time
    self.__end_time = end_time
    self.__movie = movie
    self.__seating = seating
    self.__tickets = []
    self.__price = price
    self.__lock = threading.Lock()

  """
  * @param rows: Row number in Seating
  * @param columns: Column number in the Seating
  """
  def book_ticket(self, rows, columns):
    self.__lock.acquire()
    n = len(self.__seating); m = len(self.__seating[0])
    booked = []; f = False
    for idx in range(len(rows)):
      row = rows[idx]; column = columns[idx]
      if 0 <= row < n and 0 <= column < m and self.__seating[row][column] != -1:
        self.__seating[row][column] = -1
        booked.append([row, column])
      else:
        f = True
        break
    if f:
      print("Sorry some seats are already booked!")
      for ele in booked:
        row, column = ele[0], ele[1]
        self.__seating[row][column] = -1
      return
    self.__tickets.append(Ticket(rows, columns, self))
    self.charge_money(len(rows))
    self.__lock.release()

  """
  * @param count_tickets: Number of Tickets Booked
  * @param param2: 
  """
  def charge_money(self, count_tickets):
    print("Please pay",count_tickets*self.__price)
    return

class Ticket:
  """
  Blueprint for the Ticket objects
  """

  """
  * @param rows: Rows that are Booked
  * @param columns: Columns that are Booked
  * @param show: Show Object
  """
  def __init__(self, rows, columns, show):
    self.__rows = rows
    self.__columns = columns
    self.__show = show
    self.__lock = threading.Lock()

class Time:
  """
  Blueprint for the Time objects
  """

  """
  * @param hours: Hours for Time
  * @param minutes: minutes fot Time
  """
  def __init__(self, hours, minutes):
    self.__hours = hours
    self.__minutes = minutes
    self.__lock = threading.Lock()

class TicketBooking:
  """
  Blueprint for the TicketBooking objects
  """

  """
  * @param name: Name of the Movies Ticket booking Site
  * @param place: Place of the Movie Ticket Booking Site 
  """
  def __init__(self, name, param2):
    self.__name = name
    self.__param2 = param2
    self.__lock = threading.Lock()


mirzapur = City("Mirzapur")
tulsi = Cinema("Tulsi", "Awesome Cinema", mirzapur)
mirzapur.add_cinema(tulsi)
krish = Movie("Krish", "Awesome Movie", tulsi, mirzapur)
SearchCatalogue()
tulsi.add_movie(krish)
start_time = Time(12, 45)
end_time = Time(14, 45)
seating = [[1]]
show = Show(start_time, end_time, krish, seating, 45)
show.book_ticket([0], [0])
SearchCatalogue.search_movie_by_title("Krish")