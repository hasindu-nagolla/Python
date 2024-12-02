import requests # Importing the requests module, it is not a built-in module so you need to install it using pip install requests. pip is a package manager for python


# in this, we are making a get request to the api and getting the data from the api. 
response = requests.get('https://covid-api.com/api/reports?date=2020-03-14&q=China%20Beijing&iso=CHN&region_name=China&region_province=Beijing')
print(response.json()) # This will print the response in json format 

