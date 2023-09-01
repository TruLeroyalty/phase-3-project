from db import Session,User,Base,Engine
import click
from prettycli import red,green,yellow

def main():
    click.echo(yellow("Seems like you need help keeping track of your budgeting!"))
    session = Session()