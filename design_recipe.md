1. Design and create the Table
If the table is already created in the database, you can skip this step.

Otherwise, follow this recipe to design and create the SQL schema for your table.

In this template, we'll use an example table students

# EXAMPLE

Table: Books

Columns:
id | title | author_name

2. Create Test SQL seeds
Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

-- EXAMPLE
-- (file: spec/seeds_book_store.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE students RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO students (title, author_name) VALUES (Nineteen Eighty-Four', 'George Orwell');
INSERT INTO students (title, author_name) VALUES ('Mrs Dalloway', 'Virginia Woolf');

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

psql -h 127.0.0.1 book_store < seeds_book_store.sql

3. Define the class names
Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by Repository for the Repository class name.

# EXAMPLE
# Table name: books

# Model class
# (in lib/book_store.py)

# class BookStore:
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.author_name = author_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author_name})"


# Repository class
# (in lib/book_store_repository.py)
# class BookRepository

# We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

# Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = BookStore(row['id'], row['title'], row['author_name'])
            books.append(item)
        return books

4. Implement the Model class
Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

# EXAMPLE
# Table name: books

# Model class
# (in lib/book_store.py)

class Book_Store:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.author_name = ""

        # Replace the attributes by your own columns.


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> books = Book()
# >>> books.name = 'Nineteen Eighty-Four'
# >>> books.author_name = 'George Orwell'
# >>> books.title
# 'Nineteen Eighty-Four'
# >>> books.author_name
# ''George Orwell'

You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.

5. Define the Repository Class interface
Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

# EXAMPLE
# Table name: students

# Repository class
# (in lib/student_repository.py)

class BookRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM students;

        # Returns an array of Student objects.

        # Gets a single record by its ID
        # One argument: the id (number)




    def find(id):
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM students WHERE id = $1;

        # Returns a single Student object.

        # Add more methods below for each operation you'd like to implement.

    # def create(student)
    # 

    # def update(student)
    # 

    # def delete(student)
    # 


6. Write Test Examples
Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

# EXAMPLES

# 1.
# Get all books

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/book_store.sql") # Seed our database with some test data
    repository = BookRepository(db_connection) # Create a new ArtistRepository

repo = BookRepository()

books = repository.all() # Get all books

books == [
        BookStore(1, 'Nineteen Eighty-Four', 'George Orwell'),
        BookStore(2, 'Mrs Dalloway', 'Virginia Woolf'),
        BookStore(3, 'Emma', 'Jane Austen'),
        BookStore(4, 'Dracula', 'Bram Stoker'),
        BookStore(5, 'The Age of Innocence', 'Edith Wharton')
    ]





# EXAMPLES

# 2.
# Test for book construction

def test_book_constructs():
    book = BookStore(1, "Test Book Title", "Test Author Name")
    book.id == 1
    book.title == "Test Book Title"
    book.author_name == "Test Author Name"


books[0].id # =>  1
books[0].name # => 'Nineteen Eighty-Four'
books[0].author_name # => 'George Orwell'


books[1].id # =>  1
books[1].name # => 'Mrs Dalloway'
books[1].author_name # => 'Virginia Woolf'

# 3
# Get a single book

repo = StudentRepository()

books = repo.find(1)

books.id # =>  5
books.title # =>  'The Age of Innocence'
books.author_name # =>  'Edith Wharton'

# Add more examples for each method
Encode this example as a test.

7. Test-drive and implement the Repository class behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.