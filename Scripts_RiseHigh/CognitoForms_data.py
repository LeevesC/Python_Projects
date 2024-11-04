import requests

API_KEK ="eyJhbGciOiJIUzI1NiIsImtpZCI6Ijg4YmYzNWNmLWM3ODEtNDQ3ZC1hYzc5LWMyODczMjNkNzg3ZCIsInR5cCI6IkpXVCJ9.eyJvcmdhbml6YXRpb25JZCI6ImNiYzVmOTMwLTQ3MTQtNDM2MC1iMWE2LWU3ZWVhM2I4MDdhZiIsImludGVncmF0aW9uSWQiOiI4Y2I5ZGE0MS1mNWJjLTQxNWItYmU4Zi05MzA0ZWU4MzYzYTQiLCJjbGllbnRJZCI6IjNkZTNmODMwLWNiYzctNDZlNi1iOTZlLTVmMDE2NzcyMTgzMCIsImp0aSI6ImM3MTU2OWNkLTRmZDctNDViYy04Mzk3LTNiN2JlMzRkMDQ0NyIsImlhdCI6MTcyMzAwODMwNCwiaXNzIjoiaHR0cHM6Ly93d3cuY29nbml0b2Zvcm1zLmNvbS8iLCJhdWQiOiJhcGkifQ.8JSS5_IhfKmPaIsKNuWM-pYt1Ufo8we4alYiOG9o5No"

# Base URL for the Cognito Forms API
url = 'https://www.cognitoforms.com/api/forms/3/entries/809'

# Set up the headers with your API key
headers = {
    'Authorization': f'Bearer {API_KEK}'
}

# Make the GET request to the API endpoint
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print('application numbers:', len(data['LoanApplicationDetails'])) # how many loan applications 
    print('loan split:', len(data['LoanApplicationDetails'][0]['LoanDetails'])) # how many loan split for the first application
else:
    print(f"Failed to retrieve data: {response.status_code}")
    print(response.text)

# print(data['LoanApplicationDetails'][0]['LoanDetails'][0]['LoanAmount'])
