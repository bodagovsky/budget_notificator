from yoyo import read_migrations, get_backend


def apply():
    print('Migrations process start')
    with open('/app/db/password.txt') as pass_file:
        password = pass_file.readline()
    database = get_backend('mysql://root:' + password + '@db:3306/stylight')
    print("successfully connected to database")

    print('reading migrations...')
    migrations = read_migrations('/app/db/migrations')
    print('migrations have been read')

    print('applying migrations...')
    with database.lock():
        database.apply_migrations(database.to_apply(migrations))
    print('migrations successfully have been applied')
