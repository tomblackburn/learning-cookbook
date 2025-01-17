from flask import Flask, request, jsonify

# Create a Flask application instance
# The first argument is the name of the application’s module or package
# __name__ is a convenient shortcut for this that is appropriate for most cases
# This is needed so that Flask knows where to look for resources such as templates and static files
app = Flask(__name__)

# the route() decorator tells Flask what URL should trigger our function
@app.route("/")
def home():
    #The function returns the message we want to display in the user’s browser
    # The default content type is HTML, so HTML in the string will be rendered by the browser
    return "Home"

# -----------------------------------------------------------------
# Everything above this line is what a minimal flask application looks something like

# You can add variable sections to a URL by marking sections with <variable_name>
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200

# By default, a route only answers to GET requests unless specified
# The below above keeps all methods for the route within one function, which can be useful if each part uses some common data
@app.route("/create-user", methods=["POST"])
def create_user():
    if request.method == "POST": # This is only required if multiple methods are used
        data = request.get_json()
        return jsonify(data), 201
    
# Flask provides seperate views for different methods into different functions
# A shortcut for decorating routes with get(), post()
@app.get('/login')
def login_get():
    return "login"

@app.get('/login')
def login_post():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == "__main__":
    # The Flask run command 
    # By enabling debug mode, the server will automatically reload if code changes
    # Debug mode will also show an interactive debugger in the browser if an error occurs during a request
    app.run(debug=True)

