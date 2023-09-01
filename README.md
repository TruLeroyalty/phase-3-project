

<div align="center">

# Budget CLI phase-3-project

<div align="center">
  <img src="https://img.freepik.com/free-photo/top-view-budget-written-note-notepad-with-pen-dark-surface-student-color-school-money-gray-college-copybook_179666-19729.jpg" width="600" height="300"/>
</div>

1.Create the virtual environment (Created virtual environment 3.8.13)
2.Install dependencies 
    a. SQLAlchemy Version 1.4.41 
    b. Alembic 
    c. Ipdb 
    d. faker (to generate fake data if needed) 
    e. Click
3.Create the migration environment (after shell, created migrations)
4.Conifigure the migration environment (alembic.ini and env.py) (sqlalchemy.url = sqllite///expense_tracker.db) (made updates to env.py)
5.Create the declarative base
6.Create Schema (python classes or models)
7.Populate database with seeds
8.Test the relationships (one to many)

----------------------------------------------------------------------------------------------------------------------------------------------
( Video of application if needed for visual instructions -- https://youtu.be/hWDoUqXVrQA )

INSTRUCTIONS:
    1. Go into the shell environment
    2. Run the cli.py 
    3. You will be prompted with registration or login. All you have to do is type r or l.
    4. If you register, fill out a Firstname and Lastname, Username, Password, and set the budget you wish to not go over. 
    5. You will then be successfully registered and your in the database with your information!

Do you want to start listing that amount for your expenses? Go ahead and type in "y" or "n" for when it asks you to.
You will then put in the amount that you deduct from your budget. Once you do, your budget in the database will then update!

Are you finished listing your expenses? Go ahead and tell the prompt "n" and you will be notified your remaining budget!
Remember though, if you tend to forget your password, you will NOT be able to get back into your account, and will have to register again.

Good luck on budgeting! 
</div>

<div id="badges">
  <a href="https://www.linkedin.com/in/leroysjr/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
