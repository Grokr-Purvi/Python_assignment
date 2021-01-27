import psycopg2 as pg2


class Customer:
    def get_customer_details(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        conn = pg2.connect(database="Northwind", user="postgres",password="postgres", host="localhost")
        cur = conn.cursor()


        
        query2 = '''
                SELECT COUNT(*) FROM
                customers
                ;
                '''
        cur.execute(query2)

        print('No of records :', cur.fetchall())

        query1 = '''
                SELECT * FROM
                customers
                ;
                '''

        cur.execute(query1)
        #cur.commit()
        while True:

            data = cur.fetchone() # fetchinh only one row at a time for memory effeciency
            if data == None:
                break
            yield data



if __name__ == "__main__":
    customer = Customer()
    for tuple in customer.get_customer_details() :
        print(tuple)



# No of records : [(91,)]
# ('ALFKI', 'Alfreds Futterkiste', 'Maria Anders', 'Sales Representative', 'Obere Str. 57', 'Berlin', 'NULL', '12209', 'Germany', '030-0074321', '030-0076545')
# ('ANATR', 'Ana Trujillo Emparedados y helados', 'Ana Trujillo', 'Owner', 'Avda. de la Constitución 2222', 'México D.F.', 'NULL', '05021', 'Mexico', '(5) 555-4729', '(5) 555-3745')
# ('ANTON', 'Antonio Moreno Taquería', 'Antonio Moreno', 'Owner', 'Mataderos  2312', 'México D.F.', 'NULL', '05023', 'Mexico', '(5) 555-3932', 'NULL')
# ('AROUT', 'Around the Horn', 'Thomas Hardy', 'Sales Representative', '120 Hanover Sq.', 'London', 'NULL', 'WA1 1DP', 'UK', '(171) 555-7788', '(171) 555-6750')
# ('BERGS', 'Berglunds snabbköp', 'Christina Berglund', 'Order Administrator', 'Berguvsvägen  8', 'Luleå', 'NULL', 'S-958 22', 'Sweden', '0921-12 34 65', '0921-12 34 67')
# ('BLAUS', 'Blauer See Delikatessen', 'Hanna Moos', 'Sales Representative', 'Forsterstr. 57', 'Mannheim', 'NULL', '68306', 'Germany', '0621-08460', '0621-08924')
# ('BLONP', 'Blondesddsl père et fils', 'Frédérique Citeaux', 'Marketing Manager', '24 place Kléber', 'Strasbourg', 'NULL', '67000', 'France', '88.60.15.31', '88.60.15.32')
# ('BOLID', 'Bólido Comidas preparadas', 'Martín Sommer', 'Owner', 'C/ Araquil 67', 'Madrid', 'NULL', '28023', 'Spain', '(91) 555 22 82', '(91) 555 91 99')
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
