"""
- Search Questions by title
- Member can post questions
- Memebers can add answers to open questions
- Members can add comment to answers
- Members can upvote question / answer / comment
- Members will earn points by answering on questions
- Members add tags to questions




Actors - 
 - Admin
 - Moderators
 - Members


Classes -
 - StackOverflow
     - Add Question
     - Delete Question
     - Search Question
 - SearchCatalogue
     - Search by Title
     - Search by Tags
 - Questions
     - Question Title
     - Answers
     - Upvotes / Downvotes
    Functionalities
     - Answer the Question  => Earn Points on each answers
     - Upvote the Question
     - Get all Answers
 - Answers
     - Content
     - Upvotes
     - Comments
    Functionalities
     - Add Comment 
     - Upvote Answer
     - Get all Comments
 - Comments
     - Content 
     - Upvote
     - Downvote
    Functionalities
     - Upvote Comment

"""
import threading
from enum import Enum
import datetime

class QuestionStatus(Enum):
    OPEN, CLOSED = 1, 2

"""
Person class is the Parent Class to handle 
the Basic Functionalities of the Users 
"""
class Person:
    def __init__(self, name, email, phone, password):
        self.__email = email
        self.__name = name
        self.__phone = phone
        self.__password = password

class Moderator(Person):
    def __init__(self, name, email, phone, password):
        super().__init__(name, email, phone, password)
        self.__lock = threading.Lock()

    def add_question(self, question_title, question_content):
        self.__lock.acquire()
        new_question = Question(question_title, question_content, self)
        SearchCatalogue.add_question(new_question)
        self.__lock.release()

    def delete_question(self, question_id):
        pass

class Admin(Person):
    def __init__(self, name, email, phone, password):
        super().__init__(name, email, phone, password)

    def delete_question(self, question_id):
        pass


"""
 - StackOverflow
     - Search Question
"""
class SearchCatalogue:
    __title_to_qustion = {}
    __tag_to_question = {}

    @classmethod
    def search_by_title(cls, question_title):
        print(cls.__title_to_qustion.get(question_title, "Sorry Question Not Found!"))

    @classmethod
    def add_question(cls, question):
        cls.__title_to_qustion[question.get_question_title()] = question


class Question:
    def __init__(self, question_title, question_content, member):
        self.__question_title = question_title
        self.__question_content = question_content
        self.__member = member

        self.__answers = []
        self.__upvote_count = 0
        self.__upvotes = []
        self.__comments = []
        self.__lock = threading.Lock()

    def add_answer(self, member, answer_title, answer_content):
        self.__lock.acquire()
        new_answer = Answer(answer_title, answer_content, member)
        self.__answers.append(new_answer)
        print("Answer Added!")
        self.__lock.release()

    def upvote_question(self, member):
        self.__lock.acquire()
        self.__upvote_count += 1
        self.__upvotes.append(member)
        print("Question Upvoted")
        self.__lock.release()

    def add_comment(self, member, comment_title, comment_content):
        self.__lock.acquire()
        new_comment = Comment(comment_title, comment_content, member)
        self.__comments.append(new_comment)
        print("Comment Added!")
        self.__lock.release()
        
    def get_all_comments(self):
        for comment in self.__comments:
            comment.get_comment()

    def get_all_answers(self):
        for answer in self.__answers:
            answer.get_answer()

    def get_question(self):
        print(self.__question_title)
        print(self.__question_content)

    def add_tag(self, tag_name):
        self.__lock.acquire()
        SearchCatalogue.__tag_to_question[tag_name] = self
        self.__lock.release()
    
    def get_question_title(self):
        return self.__question_title
    

    def __str__(self):
        return self.__question_title


class Answer:
    def __init__(self, answer_title, answer_content, member):
        self.__answer_title = answer_title
        self.__answer_content = answer_content
        self.__member = member
        self.__upvote_count = 0
        self.__upvotes = []
        self.__creation_time = datetime.datetime.now()
        self.__lock = threading.Lock()

    def add_comment(self, comment_title, comment_content, member):
        pass

    def upvote_answer(self, member):
        self.__lock.acquire()
        self.__upvote_count += 1
        self.__upvotes.append(member)
        self.__lock.release()


    def get_all_comments(self):
        pass


    def get_answer(self):
        print(self.__answer_title)
        print(self.__answer_content)
        print("\n\n\n\n")

class Comment:
    def __init__(self, comment_title, comment_content, member):
        self.__comment_tilte = comment_title
        self.__comment_content = comment_content
        self.__member = member
        self.__upvote_count = 0
        self.__upvotes = []
        self.__creation_time = datetime.datetime.now()

    def upvote_comment(self, member):
        pass

    def downvote_comment(self, member):
        pass


    def get_comment(self):
        print(self.__comment_tilte)
        print(self.__comment_content)
        print(self.__creation_time)
        print("\n\n\n")


moderator = Moderator("Archit", "f@gmail.com", 123, 123)
moderator.add_question("Here", "Too good")
SearchCatalogue.search_by_title("Here")