api list

GET

1 . url = api/movie_list/1/ method = get request=(
headers = {
'Authorization': 'Basic am1laHU6YWJjQDEyMzQ1' }, url=url,
)
response = { data= {
"id": 1,
"people": [
{
"id": 1,
"movie": 1,
"name": "jmehu",
"rating": 6,
"date_created": "2021-06-06T20:36:58.770965Z",
"date_modified": "2021-06-06T21:00:40.067136Z"
} ,],
"movie_name": "Mumbai saga",
"owner": "root",
"date_created": "2021-06-04T18:34:44.393854Z",
"date_modified": "2021-06-04T18:34:44.393854Z"
}, status=200, }

2 . url = api/rating/1/ method = get request=(
headers = {
'Authorization': 'Basic am1laHU6YWJjQDEyMzQ1' }, url=url,
)
response = { data= {"id":3,"movie":2,"name":"root","rating":5,"date_created":"2021-06-06T12:49:36.932517Z","
date_modified":"2021-06-06T17:29:19.404108Z"}, status=200, }

POST

1 . url = api/movies_list/ method = post request=(
headers = {
'Authorization': 'Basic am1laHU6YWJjQDEyMzQ1' }, url=url, data={'movie_name': 'Dhol'}
)

response = { data= {
"id": 1,  
"people": [],
"movie_name": "Dhol",
"owner": "root",
"date_created": "2021-06-07T07:31:43.609331Z",
"date_modified": "2021-06-07T07:31:43.609331Z"
}, status=200, }

2 . url = api/rating/ method = post request=(
headers = {
'Authorization': 'Basic am1laHU6YWJjQDEyMzQ1' }, url=url, data={'movie': '1',"rating":7}
)

response = { data= {
"id": 1,
"movie": 1,
"name": "jmehu",
"rating": 7,
"date_created": "2021-06-07T07:36:25.095233Z",
"date_modified": "2021-06-07T07:36:25.095233Z"
}, status=200, }
