# RESTful API

- **[0. Basics of HTTP/HTTPS](./T0_HTTP_HTTPS.md)**

Instructions:
1. Differentiating HTTP and HTTPS:
  - Read the provided resources to understand the basic differences between HTTP and HTTPS.
  - Jot down the main differences, focusing on security aspects.
  - Optional: Use a packet sniffer tool like Wireshark to observe the traffic of an HTTP and an HTTPS request (Make sure you have the appropriate permissions).
2. Understanding HTTP Structure:
  - Visit a simple website, right-click, and choose "Inspect" or "Inspect Element". Navigate to the "Network" tab. This shows all network requests made by the page.
  - Reload the page and observe the first request. Click on it. Explore the "Headers" section to understand the structure of HTTP requests and responses. You'll see methods, paths, status codes, headers, and more.
3. Exploring HTTP Methods and Status Codes:
  - Based on the resources provided, make a list of at least four common HTTP methods and explain when each would be used.
Make another list of five common HTTP status codes. For each status code, provide a brief description and a scenario where it might be encountered.

- **[1. Consume data from an API using command line tools (curl)](./T1_curl_API.md)**

Instructions:

1. Installing and Basic Interaction with curl:
  - Install curl on your system. It's usually available in standard repositories for Linux/Mac systems. For Windows, consider using Windows Subsystem for Linux (WSL) or downloading a Windows version of curl.
  - Once installed, run curl --version to confirm its availability.
  - Use curl to fetch the content of a webpage. For instance: curl http://example.com.
2. Fetching Data from an API:
  - Use curl to retrieve posts from JSONPlaceholder: curl https://jsonplaceholder.typicode.com/posts
  - Observe the output. It should be a JSON array of posts.
3. Using Headers and Other Options with curl:
  - Fetch only the headers of the same request using curl -I https://jsonplaceholder.typicode.com/posts.
  - Use curl to make a POST request to the same API: curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts

- **[2. Consuming and processing data from an API using Python](./task_02_requests.py)** 

Instructions:
1. If not installed, install the requests library using pip: pip install requests.
2. Write a basic Python script to fetch posts from JSONPlaceholder using requests.get().
  - Create a function fetch_and_print_posts() that fetches all post from JSONPlaceholder.
    - Print the status code of the response i.e. Status Code: 200
    - If the request was sucessfull, parse the fetched data into a JSON object using the .json() method of the response object.
    - Iterate through the parsed JSON data and print out the titles of all the posts.
  - Create a function fetch_and_save_posts() that fetches all post from JSONPlaceholder.
    - If the request was sucessfull, instead of printing titles, structure the data into a list of dictionaries, where each dictionary represents a post with keys and values for id, title, and body.
    - Using Python's csv module, write this data into a CSV file called posts.csv with columns corresponding to the dictionary keys.

- **[3. Develop a simple API using Python with the `http.server` module](./task_03_http_server.py)**

Instructions:
1. Setting Up a Basic HTTP Server:
  - Use the http.server module to set up a simple HTTP server. Start by creating a subclass of http.server.BaseHTTPRequestHandler.
  - Implement the do_GET method to handle GET requests. Within this method, send a simple text response back to the client: "Hello, this is a simple API!".
  - Start the server on a specific port (8000) and test it by visiting http://localhost:8000 in your browser or using curl.
2. Serving JSON Data:
  - Modify the do_GET method in your server class to serve a sample JSON data when the endpoint /data is accessed.
  - You should return a simple dataset: {"name": "John", "age": 30, "city": "New York"}.
  - Ensure that the correct content type (application/json) header is set in the response.
3. Handling Different Endpoints:
  - Add an /status endpoint to check the API status. It shoud return OK.
  - Implement error handling. If the user tries to access an undefined endpoint, return a 404 Not Found status with an appropriate message.

- **[4. Develop a Simple API using Python with Flask](./task_04_flask.py)**

Instructions:
1. Setting Up Flask:
  - Install Flask using pip: pip install Flask.
  - Create a new Python file and import Flask: from flask import Flask.
  - Instantiate a Flask web server from the Flask module: app = Flask(__name__).
2. Creating Your First Endpoint:
  - Define a route for the root URL ("/") and create a function (def home():) to handle this route. Within the function, return a string: "Welcome to the Flask API!".
  - Run the Flask development server with: if __name__ == "__main__": app.run().
  - Visit http://localhost:5000 in your browser or use curl to see the message.
3. Serving JSON Data:
  - Import the jsonify function from Flask: from flask import jsonify.
  - Create a new route /data and associate a function with it. Inside this function, return a JSON response using jsonify(). This should return a list of all the usernames stored in the API.
  - Users will be stored in memory using a dictionary with username as the key and the whole object (dictionary) as the value.
  - Example dictionary: users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
    - NOTE: To avoid problem with the checker, do not include your testing data when pushing your code.
4. Expanding Your API:
  - Add a few more endpoints to simulate different functionalities:
  - /status: It should return OK.
  - /users/<username>: Returns the full object corresponding to the provided username. (Hint: Use Flask's dynamic route feature)
  - If the user does not exist, return a 404 with {"error": "User not found"}.
5. Handling POST Requests:
  - Import the request object from Flask: from flask import request.
  - Create a new route /add_user that accepts POST requests.
  - This route should:
    - Parse the incoming JSON data. Example data: {"username": "john", "name": "John", "age": 30, "city": "New York"}
    - Add the new user to the users dictionary using username as the key.
    - Return a confirmation message with the added user's data.
    - If the request body is not valid JSON, return 400 with {"error":"Invalid JSON"}.
    - If username is missing, return 400 with {"error":"Username is required"}.
    - If username already exists, return 409 with {"error":"Username already exists"}.

- **[5. API Security and Authentication Techniques](./task_05_basic_security.py)**

Instructions:
  - Basic Authentication:
  1. Install Flask-HTTPAuth:
    - Run: pip install Flask-HTTPAuth.
  2. Set up Basic HTTP Authentication:
    - Create a list of users and their hashed passwords.
    - Use the werkzeug.security library for password hashing and verification.
  3. Protect Routes with Basic Authentication:
    - Use the @auth.login_required decorator to protect certain routes.
  - Token-based Authentication with JWT:
  4. Install Flask-JWT-Extended:
    - Run: pip install Flask-JWT-Extended.
  5. Set up JWT-based Authentication:
    - Use a secret key for token generation and validation.
    - Create a route /login where users can log in with their credentials and receive a JWT token.
  6. Protect Routes with JWT Tokens:
    - Use the @jwt_required() decorator to protect certain routes.
  7. Implement Role-based Access Control:
    - Add roles (e.g., admin, user) to your users.
    - Create routes that should only be accessible to certain roles.
    - Implement checks to ensure the user's role matches the required role for accessing specific routes.