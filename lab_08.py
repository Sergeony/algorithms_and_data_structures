""" Lab_8
    1)Individual task: N = 19 % 20 = 1
        1. Create multi list with author surnames and their writings.
"""


def main():
    """ The main logic of program.
    """
    # Create one publisher
    some_publisher = Publisher()

    # add 2 authors
    some_publisher.add_author('Hemingway')
    some_publisher.add_author('Dostoevsky')

    # add some writings to the authors
    some_publisher.add_writing_to_author('Dostoevsky', 'Crime and Punishments')
    some_publisher.add_writing_to_author('Dostoevsky', 'The Brothers Karamazov')
    some_publisher.add_writing_to_author('Hemingway', 'The Old Man and the Sea')
    some_publisher.add_writing_to_author('Hemingway', 'A Farewell to Arms')

    # print the publisher
    print(some_publisher)

    # delete one author and one writing
    some_publisher.del_author()
    some_publisher.del_writing_from_author('Hemingway')

    # print the publisher again
    print(some_publisher)


class Writing:
    """ A some author's writing.
    """

    def __init__(self, title: str, next_writing=None):
        self.title = title
        self.next_writing = next_writing

    def __str__(self):
        return f"{self.title}"


class Author:
    """ A person with some surname and list of their writings.
    """

    def __init__(self, surname: str, next_author=None):
        self.surname = surname
        self.first_writing: [Writing, None] = None
        self.next_author = next_author

    def add_writing(self, title: str):
        """ Add a new writing.
        """
        self.first_writing = Writing(title, self.first_writing)

    def del_writing(self):
        """ Delete the last added writing.
        """
        if self.first_writing is None:
            raise IndexError("The author has no writings yet.")

        self.first_writing = self.first_writing.next_writing

    def __str__(self):
        """ A string representation of the author.
        """
        result_string = f"{self.surname}: "
        current_writing = self.first_writing

        while current_writing is not None:
            result_string += current_writing.title

            if current_writing.next_writing is not None:
                result_string += ','
            result_string += ' '

            current_writing = current_writing.next_writing

        return result_string


class Publisher:
    """ A group of authors.
    """

    def __init__(self):
        self.first_author: [Author, None] = None

    def add_author(self, surname: str):
        """ Create a new author with no writings.
        """
        self.first_author = Author(surname, self.first_author)

    def del_author(self):
        """ Delete the last added author.
        Raise an error, if there is no author.
        """
        if self.first_author is None:
            raise IndexError("There is no authors yet.")

        self.first_author = self.first_author.next_author

    def add_writing_to_author(self, surname: str, title: str):
        """ Add a new writing to the given author.
        Raise an error, if there is no author.
        """
        current_author = self.first_author

        while current_author.surname != surname:
            if current_author is None:
                raise IndexError(f"There isn't author with {surname} surname.")

            current_author = current_author.next_author

        current_author.add_writing(title)

    def del_writing_from_author(self, surname: str):
        """ Delete the last added writing from the given author.
        Raise an error, if there is no author.
        """
        current_author = self.first_author

        while current_author.surname != surname:
            if current_author is None:
                raise IndexError(f"There isn't author with {surname} surname.")

            current_author = current_author.next_author

        current_author.del_writing()

    def __str__(self):
        """ A """
        result_string = ""
        current_author = self.first_author

        while current_author is not None:
            result_string += str(current_author) + '\n'
            current_author = current_author.next_author

        return result_string


if __name__ == "__main__":
    main()
