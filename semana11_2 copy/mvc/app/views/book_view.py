def render_book_list(books):
    return [
        {
            "id": book.id,
            "Title": book.Title,
            "Author": book.Author,
            "Edition": book.Edition,
            "Availability": book.Availability,
        }
        for book in books
    ]

def render_book_detail(book):
    return{
        "id": book.id,
        "Title": book.Title,
        "Author": book.Author,
        "Edition": book.Edition,
        "Availability": book.Availability,
    }
