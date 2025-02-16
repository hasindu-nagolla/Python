# Example for Using Dependencies in Python

# ========================================================
# Section 1: Importing External Dependencies
# ========================================================

import requests  # Importing the requests module, it is not a built-in module so you need to install it using pip install requests. pip is a package manager for python

# ========================================================
# Section 2: Making a GET Request to an API
# ========================================================

# In this example, we are making a GET request to the API and getting the data from the API.
response = requests.get('https://covid-api.com/api/reports?date=2020-03-14&q=China%20Beijing&iso=CHN&region_name=China&region_province=Beijing')

# Printing the response in JSON format
print(response.json())  # This will print the response in JSON format

# ========================================================
# Explanation
# ========================================================

# The `requests` module is used to send HTTP requests to web servers. In this example, we are sending a GET request
# to retrieve COVID-19 data for Beijing, China, on a specific date. The response is in JSON format, which is printed.
# You need to install the `requests` module using the command: `pip install requests`.


# ========================================================
# Author: Hasindu Nagolla
# Copyright © 2024 Hasindu Nagolla
# LinkedIn: https://www.linkedin.com/in/hasindu-nagolla/
# ========================================================