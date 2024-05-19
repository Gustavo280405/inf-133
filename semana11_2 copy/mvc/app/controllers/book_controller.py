from flask import Blueprint, request, jsonify
from views.book_view import render_book_detail, render_book_list
from models.book_model import Book

book_bp = Blueprint("book", __name__)

@book_bp.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    book=Book.get_by_id(id)
    if book:
        return jsonify(render_book_detail(book))
    return jsonify({"error": "Libro no encontrado"}), 404

@book_bp.route("/books", methods=["POST"])
def create_animal():
    data = request.json
    Title = data.get("Title")
    Author = data.get("Author")
    Edition = data.get("Edition")
    Availability = data.get("Availability")
    
    if not Title or not Author or not Edition or Availability is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    book = Book(Title=Title, Author=Author, Edition=Edition, Availability=Availability)
    book.save()
    
    return jsonify(render_book_detail(book)),201

@book_bp. route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    book=Book.get_by_id(id)
    if not book:
        return jsonify({"error": "Libro no encontrado"}), 404
    
    data=request.json
    Title=data.get("Title")
    Author=data.get("Author")
    Edition=data.get("Edition")
    Availability=data.get("Availability")
    
    book.update(Title=Title, Author=Author, Edition=Edition, Availability=Availability)
    return jsonify(render_book_detail(book))

@book_bp.route("/book/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = Book.get_by_id(id)
    if not book:
        return jsonify({"error": "Libro no encontrado"}), 404
    book.delete()
    
    return "", 204