from readsapi import app

@app.route("/")
def index():
   return "App Index"

@app.route("/books")
def books():
   return "Books will appear here, maybe."

@app.route("/authors")
def authors():
   return "Authors will appear here, maybe."

@app.route("/users")
def users():
   return "Users will appear here, maybe."
