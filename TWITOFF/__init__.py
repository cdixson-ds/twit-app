"""Entry point for our twitoff flask app"""

from .app import DB, create_app

APP = create_app()


"""
from .app import create_app

APP = create_app()
"""