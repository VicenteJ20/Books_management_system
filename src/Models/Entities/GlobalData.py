class Librarians():
    def __init__(self, id, password, username, fullname, email, creatorId):
        self.id = id
        self.password = password
        self.username = username
        self.fullname = fullname
        self.email = email
        self.creatorId = creatorId

class StandardClient():
    def __init__(self, id, username, fullname, email):
        self.id = id
        self.username = username
        self.fullname = fullname
        self.email = email

class Teacher(StandardClient):
    def __init__(self, id, username, fullname, email):
        super().__init__(id, username, fullname, email)

class Students(StandardClient):
    def __init__(self, id, username, fullname, email):
        super().__init__(id, username, fullname, email)

class Book():
    def __init__(self, isbn, title, state, returnDate, loanDate):
        self.isbn = isbn
        self.title = title
        self.state = state
        self.returnDate = returnDate
        self.loanDate = loanDate

class Loan():
    def __init__(self, loanId, teacherId, studentId, librarianId, debtId):
        self.id = loanId
        self.teacherId = teacherId
        self.student = studentId
        self.librarianId = librarianId
        self.debtId = debtId