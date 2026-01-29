import sqlite3

with sqlite3.connect('Lesson-11/Homework-11/roster.db') as connection:
    cursor = connection.cursor()
    create_table = """
        drop table if exists Roster;
        create table Roster (
        name text,
        species text,
        age int
        );
    """
    insert_data = """
        insert into roster values
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys', 'Bajoran', 29)    
    """
    update_data = """
        update Roster
        set name = 'Ezri Dax'
        where name = 'Jadzia Dax'
    """
    query_data = """
        select name, age
        from Roster
        where species = 'Bajoran'
    """
    delete_data = """
        delete from Roster
        where age > 100
    """
    add_column = """
        alter table Roster
        add column Rank;
        
        update roster
        set rank = 'Captain'
        where name = 'Benjamin Sisko';

        update roster
        set rank = 'Lieutenant'
        where name = 'Ezri Dax';

        update roster
        set rank = 'Major'
        where name = 'Kira Nerys';
    """
    sort_query = """
        select * from roster
        order by age desc;
    """

    # cursor.executescript(create_table)
    # cursor.execute(insert_data)
    # cursor.execute(update_data)
    data = cursor.execute(query_data)
    print(data.fetchall())
    cursor.execute(delete_data)
    # cursor.executescript(add_column)
    print(cursor.execute(sort_query).fetchall())




