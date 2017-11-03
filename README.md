# Restaurant Menu

## Routes

- `/` - listing of the entire menu, showing the name of the dish, the price, and a clickable something to show me detail about the food
- `/appetizers` - just lists the appetizers
- `/entrees`
- `/drinks`
- `/appetizers/<id>`
- `/entrees/<id>`
- `/drinks/<id>`
- `/appetizers/<id>/edit`
- `/entrees/<id>/edit`
- `/drinks/<id>/edit`
- `/appetizers/add`
- `/entrees/add`
- `/drinks/add`

## Model Outlines

Appetizers
    id - int
    name - str
    cost - float
    description - str
    spiciness - int
    special - bool

Entrees
    id - int
    name - str
    cost - float
    description - str
    spiciness - int
    special - bool

Drinks
    id - int
    name - str
    cost - float
    description - str
    proof - float
    special - bool
