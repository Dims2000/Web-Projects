"""
Web Page Requester that takes an input (URL) from the user
and outputs of the page exists or does not (404 Error)

Author: Dmitry Selin
Date Created: September 11, 2019
Last Modified: September 11, 2019
"""

import requests

try:
    # Asks for a url and creates a page request
    page = requests.get(input("Enter the URL of the page: "))

    # Prints the status of the page
    if page.status_code == 404:
        print("Incorrect: " + page.url)
    else:
        print("Correct: " + page.url)

# Prints an error
except requests.exceptions.MissingSchema:
    print("Invalid URL")
