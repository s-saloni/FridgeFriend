from django.shortcuts import render
from django.http import HttpResponse
import os
import psycopg2

#create database cursor, url subject to change
conn = psycopg2.connect('postgres://imzwfyxhbfszxx:a71f9a74dc23b416478ed018b02531f13645431b5b5f7f17017f96c6aebd107c@ec2-54-157-78-113.compute-1.amazonaws.com:5432/d8gqutif0fs20a', sslmode='require')
cur = conn.cursor()

#pull all fruit names from database
fruit = []
cur.execute("SELECT name, classifier1 FROM fruits ORDER BY name;")
fetched = cur.fetchall()
for i in range(len(fetched)):
    fruit.append(str(fetched[i][0])+': '+str(fetched[i][1]))
conn.close()

#context for index page
data = {'key1':fruit}

def index(request):
    return render(request, "pantry/index.html", context=data)

def test(request):
    return HttpResponse('test pantry:' + data['key1'][14])
