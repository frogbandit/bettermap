import os 
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")

##url = urlparse.urlparse("postgres://gqlskkqipzmtai:1tuYJio5GMTI7-iWpZ6YlzgHH_@ec2-54-228-195-37.eu-west-1.compute.amazonaws.com:5432/d4ej7n7dsh1s1n")
## url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='cloudminer',
    host='localhost',
    port=5432
 )

cur = conn.cursor()

cur.execute("SELECT company FROM map_user_projects WHERE id = 5")

print "Connect Successfully. Some records from test site\n", cur.fetchall()
