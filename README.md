# Shira API
API resources for the Shira application.

## Quick Installation
First, install all the packages needed (I recommend using Python 3 and virtualenv):

```
$ pip install -r requirements.txt
```

I assume you have created a database in postgre with the following settings:

```python
DATABASES = {
	'HOST': 'localhost',
	'NAME': 'shira_db',
	'USER': 'postgres',
	'PASSWORD': 'root',
	'PORT': '5432'
}
```

You can change this configuration as needed. the file is in `apps/settings.py`. 
Then, make 3 tables. the following is a query that can be copied and executed immediately:

```sql
CREATE TABLE product (
 id serial PRIMARY KEY,
 name VARCHAR (200) NOT NULL,
 cost INTEGER NOT NULL,
 final_price INTEGER NOT NULL,
 stock INTEGER NOT NULL,
 minimum_stock INTEGER NOT NULL
)

CREATE TABLE "order" (
 id serial PRIMARY KEY,
 order_number VARCHAR (10) UNIQUE NOT NULL,
 created DATE NOT NULL DEFAULT CURRENT_DATE,
 grand_total INTEGER NOT NULL,
 pay INTEGER NOT NULL,
 change INTEGER NOT NULL
)

CREATE TABLE item (
 id serial PRIMARY KEY,
 order_id INTEGER NOT NULL,
 product_id INTEGER NOT NULL,
 quantity INTEGER NOT NULL,
 final_price INTEGER NOT NULL,
 subtotal INTEGER NOT NULL,
 CONSTRAINT order_id_fkey FOREIGN KEY (order_id)
  REFERENCES "order" (id) MATCH SIMPLE
  ON UPDATE NO ACTION ON DELETE NO ACTION,
 CONSTRAINT product_id_fkey FOREIGN KEY (product_id)
  REFERENCES product (id) MATCH SIMPLE
  ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE "user" (
 id serial PRIMARY KEY,
 username VARCHAR (200) UNIQUE NOT NULL,
 email VARCHAR (200) UNIQUE NOT NULL,
 password VARCHAR (200) NOT NULL,
 first_name VARCHAR (100),
 last_name VARCHAR (100),
 created DATE NOT NULL DEFAULT CURRENT_DATE,
 is_active BOOLEAN NOT NULL
);
```

Run with pleasure and access URL `http://localhost:9000/`:

```
$ python manage.py
```

