from app import app

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/page1')
def one_page(method="POST"):
    return 'one page'