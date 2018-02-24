from .models import Nav


def get_nav(type):
    return Nav.query.filter_by(type=type).all()