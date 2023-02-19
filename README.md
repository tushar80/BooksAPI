# API Documentation

* * *

## User Registration

`POST /api/users/register`

This API allows users to register for an account.

Request Parameters:

* `username` (required): The username of the user.
* `email` (required): The email of the user.
* `password` (required): The password of the user.

Response:

* If registration is successful, returns 201 Created and the newly created username and authentication token.
* If registration fails, returns a 400 Bad Request error with an error message.

* * *

## User Login

`POST /api/users/login`

This API allows users to login to their account.

Request Parameters:

* `username` (required): The username of the user.
* `password` (required): The password of the user.

Response:

* If login is successful, returns 200 OK and a access token and a refresh token that can be used to authenticate future requests.
* If login fails, returns a 401 Unauthorized error with an error message.

* * *

## Refresh Token

`POST /api/users/login/refresh`

This API allows users to get a new access token with refresh token.

Request Parameters:

* `refresh` (required): The refresh token.

Response:

* If successful, returns 200 OK and a access token that can be used to authenticate future requests.
* If failed, returns a 401 Unauthorized error with an error message.

* * *

## Get Books

`GET /api/books`

This API allows authenticated users to get a list of all books.

Authentication:

* Users must include a valid authentication token in the `Authorization` header of the request.

Response:

* If the user is authenticated, returns 200 OK and list of all Books.
* If the user is not authenticated, returns a 401 Unauthorized error with an error message.

* * *

## Add Book

`POST /api/books`

This API allows authenticated users to add a book.

Request Parameters:

* `title` (required): The title of the book.
* `author` (required): The author of the book.
* `description` (optional): The description of the book.

Authentication:

* Users must include a valid authentication token in the `Authorization` header of the request.

Response:

* If the book is added successfully, returns 201 Created and the newly created book object.
* If the user is not authenticated, returns a 401 Unauthorized error with an error message.

* * *

## Get Reviews of a Book

`GET /api/books/:book_id/reviews`

This API allows authenticated users to get a list of reviews of a books.

Authentication:

* Users must include a valid authentication token in the `Authorization` header of the request.

Response:

* If the user is authenticated, returns 200 OK and list of all Books.
* If the user is not authenticated, returns a 401 Unauthorized error with an error message.

* * *

## Add Review

`POST /api/books/:book_id/reviews`

This API allows authenticated users to add a review for a book.

Request Parameters:

* `rating` (required): The rating given by the user (an integer between 1 and 5).
* `review_text` (optional): The review text provided by the user.

Authentication:

* Users must include a valid authentication token in the `Authorization` header of the request.

Response:

* If the review is added successfully, returns 201 Created and the newly created review object.
* If the user is not authenticated or the book ID is invalid, returns a 401 Unauthorized error with an error message.

* * *

## Delete Review

`DELETE /api/books/reviews/:review_id`

This API allows authenticated users to delete a review.

Authentication:

* Users must include a valid authentication token in the `Authorization` header of the request.

Response:

* If the review is deleted successfully, returns 200 OK.
* If the user is not authenticated or the review ID is invalid, returns a 401 Unauthorized error with an error message.
