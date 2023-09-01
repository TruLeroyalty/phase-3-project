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

    user = User(name=f"{first_name} {last_name}", username=user_name,password=password, budget=budget)
    session.add(user)
    session.commit()
    click.echo(green(f"User {first_name} {last_name} registered with a budget of ${budget:.2f}"))

    calculate_expenses = click.confirm("Do you have any expenses to calculate?")
    if calculate_expenses:
        user = session.query(User).filter_by(name=f"{first_name} {last_name}").first()
        manage_budget(session.user)

    if calculate_expenses != "y":
        click.echo(green(f"Your remaining budget is ${user.budget}"))
        click.echo(yellow("Thank you for using our services."))

def login_user(session):
    click.echo("Login")
    name = click.prompt("First and Lastname")
    username = click.prompt("Username")
    password = click.prompt("Password")

    user = session.query(User).filter_by(username=username, password=password).first()
    return user

def manage_budget(session,user):
    while True:
        click.echo(green(f"Your current budget is: {user.budget}"))
        expense_amount = float(input("Enter the expense amount: "))

        if expense_amount <= 0 or expense_amount > user.budget:
            click.echo(red("Invalid expense amount. Please enter a valid amount."))
            continue

        user.budget -= expense_amount
        session.commit()
        click.echo(f"Expense of {red(str(expense_amount))} deducted from your budget.")

        more_expenses = input(yellow("Do you want to enter another expense? (y/n): "))
        if more_expenses.lower() !="y":
            click.echo(green(f"Your remaining budget is: {user.budget}"))
            click.echo(yellow("Thank you for using our services."))
            break

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