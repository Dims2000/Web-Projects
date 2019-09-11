"""
Web Page Requester that takes an input (URL) from the user
and outputs of the page exists or does not (404 Error)

Author: Dmitry Selin
Date Created: September 11, 2019
Last Modified: September 11, 2019
"""

import requests

# Asks for a user input
url = input("Type in the URL of the website: ")

# Checks if the URL entered is valid
try:
    # Creates a page request for url
    page = requests.get(url)

    # Prints if the
    if page.status_code == 404:
        print("Incorrect: " + page.url)
    else:
        print("Correct: " + page.url)

# Prints an error
except requests.exceptions.MissingSchema:
    print("Invalid URL")
