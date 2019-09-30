d={
    ('a','aa'): (1,2),
    ('a','ab'): (3,4),
    ('a','ac'): (3,5),
    ('a','ad'): (3,5),
    ('b', 'aa'): (1, 2),
    ('b', 'ab'): (1, 1),
    ('b', 'bc'): (3, 5),
    ('b', 'ad'): (3, 5),
}
if not ('c', 'ad') in d :
    d[('c', 'ad')]=(11,12)

for entry in sorted(d.items(), key=lambda x: (x[0][0],x[1][0],x[1][1],x[0][1]) ):
    print(entry)

import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost    .
#conn.close()

#conn = sqlite3.connect(':memory:')
#c = conn.cursor()

c.execute('select * from stocks order by price ')
for row in c:
    print(row)
conn.close()
