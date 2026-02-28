import mysql.connector
class ProductDAO:
    
    def __init__(self, id, name, category, price,quantity_in_stock):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.quant=quantity_in_stock
    
    
    def save(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("INSERT INTO Products (product_id,last_name,category,price,quantity_in_stock) VALUES (%s, %s, %s, %s, %s) ",(self.id,self.name,self.category,self.price,self.quant))
            conn.commit()
            print("Product saved")
        except Exception as e:
            conn.rollback() 
            print("Erreur:", e) 
    
    
    def delete(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("DELETE FROM Products WHERE product_id=%s",(self.id,))
            conn.commit()
            print("Product deleted")
        except Exception as e:
            conn.rollback() 
            print("Erreur:", e)               
    

    def update(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("UPDATE Products SET last_name=%s, category=%s, price=%s, quantity_in_stock=%s WHERE product_id=%s",(self.name,self.category,self.price,self.quant,self.id))
            conn.commit()
            print("Product updated")
        except Exception as e:
            conn.rollback() 
            print("Erreur:", e) 

    
    def find_by_id(self,conn,id):
        cursor=conn.cursor
        try:
            cursor.execute("SELECT * FROM Products WHERE product_id=%s ",(id,))
            row=cursor.fetchall()
            print(row)
        except Exception as e:
            conn.rollback() 
            print("Erreur:", e)

class CustomerDAO:
    
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
    
    
    def save(self,conn): 
        cursor=conn.cursor()
        try:
            cursor.execute("INSERT INTO Customer (customer_id,last_name,email) VALUES (%s, %s, %s) ",(self.id,self.name,self.email))
            conn.commit()
            print("Customer saved ")
        except Exception as e:
            conn.rollback()
            print("Erreur:", e)
    
    
    def delete(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("DELETE FROM Customer WHERE customer_id=%s",(self.id,))
            conn.commit()
            print("Customer deleted")
        except Exception as e:
            conn.rollback() 
            print("Erreur:", e)        


    def update(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("UPDATE Customer SET last_name=%s, email=%s WHERE customer_id=%s",(self.name,self.email,self.id))
            conn.commit()
            print("Customer updated")
        except Exception as e:
            conn.rollback() 
            print("Erreur:", e)


    def find_by_id(self,conn,id):
        cursor=conn.cursor()
        try:
            cursor.execute("SELECT * FROM Customer WHERE customer_id=%s ",(id,))
            row=cursor.fetchall()
            print(row)
        except Exception as e:
            conn.rollback() 
            print("Erreur:", e)

class OrderDAO:
    def __init__(self, id, customer_id, order_date):
        self.id = id
        self.customer_id = customer_id
        self.order_date = order_date
    def save(self,conn): 
        cursor=conn.cursor()
        try:
            cursor.execute("INSERT INTO Orders (order_id,customer_id,order_date) VALUES (%s, %s, %s) ",(self.id,self.customer_id,self.order_date))
            conn.commit()
            print("Order saved")
        except Exception as e:
            conn.rollback() 
            print("Erreur:", e) 
    

    def delete(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("DELETE FROM Orders WHERE order_id=%s",(self.id,))
            conn.commit()
            print("Order deleted")
        except Exception as e:
            conn.rollback() 
            print("Erreur:", e)


    def update(self,conn):
        cursor=conn.cursor()
        try:
            cursor.execute("UPDATE Orders SET customer_id=%s, order_date=%s WHERE order_id=%s",(self.customer_id,self.order_date,self.id))    
            conn.commit()
            print("Order updated")
        except Exception as e:
            conn.rollback() 
            print("Erreur:", e) 

    def find_by_id(self,conn,id):
        cursor=conn.cursor()
        try:
            cursor.execute("SELECT * FROM Orders WHERE order_id=%s ",(id,))
            row=cursor.fetchall()
            print(row)
        except Exception as e:
            conn.rollback() 
            print("Erreur:", e)

                    
