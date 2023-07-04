import firebase_admin
from firebase_admin import credentials
from firebase_admin import  db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://smartattendance-7b3c8-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = {
    '501':
        {
            'name':'Jeff Bezoz',
            'branch':'IT',
            'starting_year':2020,
            'total_attendance':7,
            'year':3,
            'last_attendance_time':'2021-12-11 00:54:35'
        },
    '502':
        {
            'name':'Mukesh Ambani',
            'branch':'Chemical',
            'starting_year':2019,
            'total_attendance':8,
            'year':4,
            'last_attendance_time':'2022-12-11 00:25:35'
        },
   '503':
        {
            'name':'Narendra Mode',
            'branch':'CSE DS',
            'starting_year':2022,
            'total_attendance':6,
            'year':1,
            'last_attendance_time':'2022-12-11 00:54:35'
        },
   '504':
        {
            'name':'Neeraj Chopra',
            'branch':'EIE',
            'starting_year':2021,
            'total_attendance':6,
            'year':2,
            'last_attendance_time':'2022-12-11 00:54:35'
        },

    '505':
        {
            'name':'PV Sindhu',
            'branch':'ECE',
            'starting_year':2022,
            'total_attendance':3,
            'year':1,
            'last_attendance_time':'2021-12-11 00:25:35'
        },
   '506':
        {
            'name':'Rohith',
            'branch':'CSE',
            'starting_year':2019,
            'total_attendance':5,
            'year':4,
            'last_attendance_time':'2022-12-11 00:54:35'
        },
    '507':
        {
            'name':'Rohit Sharma',
            'branch':'EEE',
            'starting_year':2022,
            'total_attendance':8,
            'year':1,
            'last_attendance_time':'2021-12-11 00:25:35'
        },
   '508':
        {
            'name':'Sai Charan',
            'branch':'CSE',
            'starting_year':2020,
            'total_attendance':9,
            'year':3,
            'last_attendance_time':'2022-12-11 00:54:35'
        },
    '509':
        {
            'name':'Saina Nehwal',
            'branch':'ECE',
            'starting_year':2019,
            'total_attendance':2,
            'year':4,
            'last_attendance_time':'2021-12-11 00:25:35'
        },
    '510':
        {
            'name':'Satya Nadella',
            'branch':'MECH',
            'starting_year':2020,
            'total_attendance':5,
            'year':3,
            'last_attendance_time':'2023-12-11 00:54:35'
        },
    '511':
        {
            'name':'Sundar Pichai',
            'branch':'ECE',
            'starting_year':2019,
            'total_attendance':4,
            'year':4,
            'last_attendance_time':'2022-12-11 00:25:35'
        },
    '512':
        {
            'name':'Virat Kohli',
            'branch':'CIVIL',
            'starting_year':2022,
            'total_attendance':8,
            'year':1,
            'last_attendance_time':'2022-12-11 00:25:35'
        }
}

for key,value in data.items():
    ref.child(key).set(value)