# import urllib
# use urllib.request to get the data from the url
# write a function that takes a url
# returns a response

import urllib.request as urllib

print("This is a  Site Connectivity checker program")

def main(url):
    print("Checking connectivity... ")
    
    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was:", response.getcode())

input_url = input("Input the url of the site you want to check: ")

main(input_url)

