import sqlite3

conn = sqlite3.connect('homework1.sqlite3')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(24) NOT NULL UNIQUE
        ); 
''')
conn.commit()
cur.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(36) NOT NULL,
        description VARCHAR(140),
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id)
        );
''')
conn.commit()
cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(24),
        email VARCHAR(24) UNIQUE
        );
''')
conn.commit()
cur.execute('''
    CREATE TABLE IF NOT EXISTS statuses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(10) UNIQUE
        );
''')
conn.commit()
cur.execute('''
    CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    status_id INTEGER,   
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (status_id) REFERENCES statuses (id)
    );
''')
conn.commit()
cur.execute('''
    CREATE TABLE IF NOT EXISTS order_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders (id),
    FOREIGN KEY (product_id) REFERENCES products (id)
    );
''')
conn.commit()

cur.executemany('''
    INSERT INTO categories(name)
    VALUES(?);    
''', (('airdrone',), ('drone',)))
conn.commit()

cur.execute('''
    UPDATE categories SET name = 'aiRdronE' WHERE id = 9
''')
conn.commit()

cur.execute('''
    DELETE FROM categories WHERE id = 10
''')
conn.commit()