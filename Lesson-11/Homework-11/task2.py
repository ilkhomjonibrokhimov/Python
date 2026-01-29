import sqlite3

with sqlite3.connect('Lesson-11/Homework-11/Library.db') as connection:
    cursor = connection.cursor()
    create_table = """
        drop table if exists Books;
        create table Books (
        title text,
        author text,
        year_published int,
        genre text
        );
    """
    insert_data = """
        insert into Books values
        ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
        ('1984', 'George Orwell', 1949, 'Dystopian'),
        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')    
    """
    update_data = """
        update Books
        set year_published = 1950
        where title = '1984'
    """
    query_data = """
        select title, author
        from Books
        where genre = 'Dystopian'
    """
    delete_data = """
        delete from Books
        where year_published > 1950
    """
    add_column = """
        alter table Books
        add column Rating;
        
        update Books
        set Rating = '4.8'
        where title = 'To Kill a Mockingbird';

        update Books
        set Rating = '4.7'
        where title = '1984';

        update Books
        set Rating = '4.5'
        where title = 'The Great Gatsby';
    """
    sort_query = """
        select * from Books
        order by year_published asc;
    """

    # cursor.executescript(create_table)
    # cursor.execute(insert_data)
    cursor.execute(update_data)
    data = cursor.execute(query_data)
    print(data.fetchall())
    cursor.execute(delete_data)
    # cursor.executescript(add_column)
    print(cursor.execute(sort_query).fetchall())

    