def migrate(connection):
    command = """
            create table if not exists public.authors
        (
            id serial primary key,
            first_name   varchar(16) not null,
            last_name  varchar(128)
        );
    """
    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()
    cursor.execute("SELECT COUNT(*) From authors")
    row_count = cursor.fetchone()[0]
    if row_count == 0:
        cursor.execute("""
        insert into authors(first_name, last_name) values('nombre1','ape1');
        insert into authors(first_name, last_name) values('nombre2','ape2');
        insert into authors(first_name, last_name) values('nombre3','ape3');
        insert into authors(first_name, last_name) values('nombre4','ape4');
        """)
        connection.commit()
    cursor.close()
