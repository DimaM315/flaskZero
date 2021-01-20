from controllers.BaseController import *
from tools import slugify
from models import *


class PageController(BaseController):
    def _call(self, *args, **kwargs):
        page = kwargs.get('page', False)
        if page == 'index':
            return self.index_page()
        elif page == '404error':
            return self.error_page(kwargs['error'])


    def index_page(self):
        return render_template('index.html',)


    def error_page(self, error_code):
        if error_code == 404:
            return render_template('404.html'), 404
