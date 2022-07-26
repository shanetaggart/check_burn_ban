
''' Get the Burn Ban data from https://novascotia.ca/burnsafe/. '''

import requests
import constants

def check_burn_ban():

    ''' Returns the current burn_condition for TOWN. '''

    # Error message for when there is no information
    burn_condition = 'ERROR: NO BURN BAN INFORMATION.'
    
    # Get the XML (Unicode) response and sanitize it before converting it to a String.
    response = requests.get(constants.URL)
    xml = response.text.encode('utf-8').replace('\t', '').lower()
    
    # Convert the String to a List and look for TOWN to pull out the burn_condition
    lines = xml.splitlines()
    for line in lines:
        if constants.TOWN in line:
            burn_condition = lines[lines.index(line) + 1].lower()
            burn_condition = burn_condition.replace('<conditionenglish>', '').replace('</conditionenglish>', '')
    print(burn_condition)
    return burn_condition

if __name__ == '__main__' :
    check_burn_ban()
