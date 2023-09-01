from db import Session,User,Base,Engine
import click
from prettycli import red,green,yellow

def register_user(session):
    click.echo("Register")
    first_name = click.prompt("First Name")
    last_name = click.prompt("Last Name")
    user_name= click.prompt("Username")
    password = click.prompt("Password")
    budget = click.prompt("Budget", type=float)



def main():
    click.echo(yellow("Seems like you need help keeping track of your budgeting!"))
    session = Session()

    choice = click.prompt(click.style("Do you want to (l)ogin or (r)egister?", fg="yellow"), type=click.Choice(["l", "r"]))
        if choice == "1":
            user = login_user(session)
            if user:
                manage_budget(session,user)
            else:
                click.echo(red("Invalid username or password. Exiting..."))
            else:
                register_user(session)
            
            session.close()

            if __name__ == "__main__":
                Base.metadata.create_all(engine)
                main()