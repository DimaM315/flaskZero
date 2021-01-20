from app import app
import controllers


@app.route('/', methods=['GET', 'POST'])
def index():
	return controllers.PageController().call(page='index')


@app.errorhandler(404)
def page_not_found(e):
    return controllers.PageController().call(page='404error', error=404)