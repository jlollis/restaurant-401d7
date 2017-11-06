"""All the views."""
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config
from restaurant_menu_app.models import Appetizer, Entree, Drink


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request):
    return {}


@view_config(route_name='appetizers', renderer='../templates/list.jinja2')
def appetizers_list(request):
    # query the dbsession for appetizer objects
    appetizers = request.dbsession.query(Appetizer).all()
    return {
        'items': appetizers,
        'route': 'appetizer_detail'
    }


@view_config(route_name='entrees', renderer='../templates/list.jinja2')
def entrees_list(request):
    entrees = request.dbsession.query(Entree).all()
    return {
        'items': entrees,
        'route': 'entree_detail'
    }


@view_config(route_name='drinks', renderer='../templates/list.jinja2')
def drinks_list(request):
    """List of all the drink items."""
    drinks = request.dbsession.query(Drink).all()
    return {
        'items': drinks,
        'route': 'drink_detail'
    }


@view_config(route_name='appetizer_detail', renderer='../templates/detail.jinja2')
def appetizer_detail(request):
    """Detail for one appetizer."""
    app_id = int(request.matchdict['id'])
    appetizer = request.dbsession.query(Appetizer).get(app_id)
    if not appetizer:
        raise HTTPNotFound
    return {
        'item': appetizer
    }


@view_config(route_name='drink_detail', renderer='../templates/detail.jinja2')
def drink_detail(request):
    """Detail for one drink."""
    drink_id = int(request.matchdict['id'])
    drink = request.dbsession.query(Drink).get(drink_id)
    if not drink:
        raise HTTPNotFound
    return {
        'item': drink
    }


@view_config(route_name='entree_detail', renderer='../templates/detail.jinja2')
def entree_detail(request):
    """Detail for one entree."""
    entree_id = int(request.matchdict['id'])
    entree = request.dbsession.query(Entree).get(entree_id)
    if not entree:
        raise HTTPNotFound
    return {
        'item': entree
    }
