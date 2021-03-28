from easysav import app


@app.route('/', methods=["GET"])
def get_home():
    return "Hello world !"
