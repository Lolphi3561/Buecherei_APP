from sqlalchemy import Column, DateTime, Integer, String, Float, Boolean

class BOOKS():

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    isbn = Column(Integer, index=True)
    title = Column(String)
    author = Column(String)
    publisher = Column(String)
    publishedYear = Column(DateTime)
    isAvailable = Column(Boolean, index=True)


class LOANS():

    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True)
    bookId = Column(Integer)
    userId = Column(Integer)
    borrowedAt = Column(DateTime)
    dueDate = Column(DateTime)
    returnedAt = Column(DateTime)
    status = Column(String, index=True)