from flask import Flask, render_template, request
from sqlalchemy import *
# import simplejson as json
# import collections
# import requests

import os 
# import psycopg2
# import urlparse


app = Flask(__name__)

# @app.route('/', methods = ['POST'])
# def getPersonById():
#     personId = int(request.form['personId'])
#     return personId

@app.route("/")
# def search():
# 	return render_template("form.html")

# @app.route("/search", methods=["GET", "POST"])
def hello():

	# db = create_engine('postgresql://postgres:cloudminer@localhost:5432/postgres')
	db = create_engine('postgres://gqlskkqipzmtai:1tuYJio5GMTI7-iWpZ6YlzgHH_@ec2-54-228-195-37.eu-west-1.compute.amazonaws.com:5432/d4ej7n7dsh1s1n')
	metadata = MetaData(db)
	users = Table('map_resources_table', metadata, autoload=True)
	#users = Table('map_user_projects', metadata, autoload=True)
	#s = users.select(and_(not_(users.c.latitude == 0))).order_by("longitude DESC")
	#users.c.id != 114806, users.c.id!= 114716, users.c.id != 114859
	s = users.select(not_(users.c.latitude == 0))

	rs = s.execute()
	rows = rs.fetchmany(5)
	
	#196880
	#Moghoweyik River
	# #-171.6199

	# rowarray_list = []

	# #filename = request.form["commodity"]
	# count = 0
	# for row in rows:

	# 	# if filename in row1.commodity_name:
	# 		geometry = {'coordinates': [row.longitude, row.latitude], 'type': "Point"}
	# 		# properties = {'publicid': row.project_name, 'origintime': row.project_name, 'longitude': row.longitude, 'latitude': row.latitude, 'depth': row.id, 
	# 		# 'magnitude': row.id, 'magnitudetype': row.project_name, 'status': row.project_name, 'phases': row.id, 'type': row.project_name, 
	# 		# 'agency': row.project_name, 'updatetime': row.project_name, 'bbox': [row.longitude, row.latitude, row.longitude, row.latitude]}
	# 		properties = {}
	# 		t = {'type': "Feature", 'geometry': geometry, 'geometry_name': row.project_name, 'properties': properties, 'commodity': row.commodity_name, 'country_code': row.country_code}
	# 	# for row2 in rows:

	# 	# 	if (row1.latitude == row2.latitude) and (row1.longitude == row2.longitude):
	# 	# 		count = count + 1

	# 	# t = {'lon': row1.longitude, 'lat': row1.latitude, 'project': row1.project_name, 'number': row1.id}
	# 		rowarray_list.append(t)
	# 		count = 0


	# 		# if filename in row1.commodity_name:
	# 	# 	point = {'coordinates': [row.latitude, row.longitude]}
	# 	# 	t = {'point': point, 'project': row.project_name}
	# 	# # for row2 in rows:

	# 	# # 	if (row1.latitude == row2.latitude) and (row1.longitude == row2.longitude):
	# 	# # 		count = count + 1

	# 	# # t = {'lon': row1.longitude, 'lat': row1.latitude, 'project': row1.project_name, 'number': row1.id}
	# 	# 	rowarray_list.append(t)
	# 	# 	count = 0



 #   	j = json.dumps(rowarray_list,  use_decimal=True, sort_keys = True)

 #   	j = '{"type": "FeatureCollection", "features":' + j + ', "crs":{"type":"EPSG","properties":{"code":"4326"}},"bbox":[-1000, 1000, -1000, -1000]}'
 #   	print j[-1000:-1]
 #   	#j = '{"type": "", "features":' + j + ', "crs": {}, "bbox": []}'
 #   	#j = '{"objects":' + j + '}'
 #   	f = open('static/data/data.json', 'w+')
 #   	f.write(j)
 #   	f.close()



	return render_template("earthquake.html")


# if __name__ == "__main__":
#     app.run(debug=True)
