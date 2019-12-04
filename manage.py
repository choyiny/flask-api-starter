""" Interface similar to manage.py """
import argparse
import sys

from app import create_app
from extensions import db


def seed(a):
    __import__(f"db.seeds.{a.seedfile}")


def reset_db(_):
    # create app using factory
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()


def get_arg_parse():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # resetting db
    reset_db_parser = subparsers.add_parser('reset', description="Reset the db")
    reset_db_parser.set_defaults(func=reset_db)

    # importing seeds
    seed_parser = subparsers.add_parser('seed', description="Seed the db")
    seed_parser.set_defaults(func=seed)
    seed_parser.add_argument('seedfile', help="name of the seedfile located in db/seeds/<seedfile>.py")

    return parser


if __name__ == '__main__':
    if len(sys.argv) > 1:
        args = get_arg_parse().parse_args()
        args.func(args)
