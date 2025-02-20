POSTGRES:-

# For Mac
brew services list
# If not running, start it with:
brew services start postgresql

# Log into PostgreSQL as the postgres user
psql postgres

# check if Django can connect to PostgreSQL:
python manage.py dbshell
