import os
import sys
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from ..models import Appetizer, Entree, Drink


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    settings['sqlalchemy.url'] = os.environ.get('DATABASE_URL', '')

    engine = get_engine(settings)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

        appetizers = [
            Appetizer(name='Spring Rolls', cost=4.99, description="They are spring rolls. Figure it out.", spiciness=1),
            Appetizer(name='Haggis', cost=19.99, description="Ew.", spiciness=5, special=True),
            Appetizer(name='Chicken Satay', cost=5.99, description="Chicken on a stick", spiciness=1),
            Appetizer(name='Nachos', cost=5.99, description="Why are these even here?", spiciness=1),
            Appetizer(name='Chicken Wings', cost=5.99, description="These aren't even cooked", spiciness=1)
        ]

        drinks = [
            Drink(name='Water', cost=0.99, description="", proof=50),
            Drink(name='Sprite', cost=0.99, description="", proof=50),
            Drink(name='Dr. Pepper', cost=0.99, description="", proof=50),
            Drink(name='Coke', cost=0.99, description="", proof=50),
            Drink(name='Old Fashioned', cost=0.99, description="", proof=50),
            Drink(name='Martini', cost=0.99, description="", proof=50),
            Drink(name='Old Beer', cost=0.99, description="", proof=50),
        ]

        dbsession.add_all(appetizers)
        dbsession.add_all(drinks)

