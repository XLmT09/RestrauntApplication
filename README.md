# **Restaurant Management System**
![Version](https://img.shields.io/badge/Version-v3.0.0-blue)
![Not Supported](https://img.shields.io/badge/Support-Not%20Supported-red)
![No Longer Maintained](https://img.shields.io/badge/Maintenance-No%20Longer%20Maintained-red)


_**Important:** The online database used has been taken down. When running the application, you will need to create your own menu items._

A web interface that helps in managing crucial daily tasks of a restaurant.


![restaurant image](restaurant.png)

## **1 Setup**
### **1.1 Configuration**
Make sure to install required modules before running the application, you can simply type this command to achive this:
```console
pip install -r requirements.txt
```
<br />

### **1.2 How to Run the Application**
After installing the required modules, go onto the command prompt and under the "project" folder type the following command:
```console
python manage.py runserver
```
You will now see a link to the webpage on the terminal, copy the link on the terminal and paste in the browser.
Or use the link below instead:
> http://127.0.0.1:8000/

<br />

## **2 Account Types**

There are different account types in the system:

- **Chefs**
- **Customers**
- **Waiters**
- **Admin**

---

### **2.1 Creating an Admin**

To create an admin account, use the following command:

```bash
py manage.py createsuperuser
```

Now you can log in with this account and use its privileges.
### **2.2 Account Information**
**Admin**
- Can manage all live orders.
- Can manage the menu.
- Handles customer help requests.

**Chefs**
- Can manage the menu.
- Can only manage confirmed orders.

**Waiters**
- Can manage the menu.
- Handles help requests.
- Can manage all other orders (placed, prepared, and delivered).

**Customer**
- Customers can register on the website.
- Alternatively, an admin can create a customer account.


## **3 Database**
This application is compatiable with the **SQLlite** and **bit.io** database.
SQLite will setup a database on your local machine whereas bit.io will setup an online database server (3GB MAX).

### *3.1 *Bit.io** 
If you would like to use ***your own*** **bit.io** database then under **project/project/settings.py**, find the dictionary called **DATABASES** then replace with this code:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<DATABASE_NAME>',
        'USER': '<USERNAME>',
        'PASSWORD': '<v2_YOUR_PASSWORD_HERE>',
        'HOST': 'db.bit.io',
        'PORT': '5432',
    }
}
```
You will also need to: setup a bit.io account, create a database and fill in the information for the above code.

### **3.2 SQLite**
If you would like to use a ***local SQLite*** database then under **project/project/settings.py**, find the dictionary called **DATABASES** then replace with this code: 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
A database called **db.sqlite3** should be created on your local machine.

### **Migrations**
If you had decided to change the databse you will have to do a migration so the website is connected with your new database.
To achive this go on the command prompt under **project/** directory and type the following command:
```bash
python manage.py makemigrations
```
<br />

## **4 Testing**
### **4.1 How to Run Test**
To run the test write the command below:
```console
python manage.py test
```

### **4.2 Notes on Testing**
Testing has been done on a dummy database which only stays alive during runtime of tests and destroyed when tests are complete.
The tests will run on a local sqlite database and the implemention can be found under settings.py with the following code:
```python
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase'
    }
```
You may modify the test database by altering these lines of code.


<br />

## **5 Software and Tools**
Software and tools to be used in devlopment:
1. Python 3.9.16
2. Django 4.1.5
3. Visual Studio Code
4. Remote PostgreSQL (bit.io)
5. PostgreSQL Database Adapter for Python (psycopg2)
6. Prettier - Code Formatter (Visual Studio Code Extension)
7. Requests Toolbelt 0.10.1

<br />

## **6 Operating Systems**
Works with *Windows* and *OS*