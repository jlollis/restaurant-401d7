"""Route configuration."""


def includeme(config):
    config.add_static_view('static', 'restaurant_menu_app', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('appetizers', '/appetizers')
    config.add_route('entrees', '/entrees')
    config.add_route('drinks', '/drinks')
    config.add_route('appetizer_detail', '/appetizers/{id:\d+}')
    config.add_route('entree_detail', '/entrees/{id:\d+}')
    config.add_route('drink_detail', '/drinks/{id:\d+}')
    config.add_route('edit_appetizer', '/appetizers/{id:\d+}/edit')
    config.add_route('edit_entree', '/entrees/{id:\d+}/edit')
    config.add_route('edit_drink', '/drinks/{id:\d+}/edit')
    config.add_route('add_appetizer', '/appetizers/add')
    config.add_route('add_entree', '/entrees/add')
    config.add_route('add_drink', '/drinks/add')
