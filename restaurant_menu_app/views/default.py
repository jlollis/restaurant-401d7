from pyramid.view import view_config
from restaurant_menu_app.models import Appetizer, Entree, Drink


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request):
    return {}


@view_config(route_name='appetizers', renderer='../templates/appetizers.jinja2')
def appetizers_list(request):
    # query the dbsession for appetizer objects
    appetizers = request.dbsession.query(Appetizer).all()
    return {
        'appetizers': appetizers
    }


@view_config(route_name='entrees', renderer='../templates/entrees.jinja2')
def entrees_list(request):
    entrees = request.dbsession.query(Entree).all()
    return {
        'entrees': entrees
    }


@view_config(route_name='drinks', renderer='../templates/drinks.jinja2')
def drinks_list(request):
    drinks = request.dbsession.query(Drink).all()
    return {
        'drinks': drinks
    }

