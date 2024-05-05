import requests
import os

url = "https://api.openai.com/v1/fine_tuning/jobs/ftjob-TnPKw18OSI5T1o8c4ZY2THS8"
key = os.environ.get('PYTHON_API_KEY')
file_id = "file-SrYC1bUKEhUQPs271hK2ScXD"
url_2 = "https://api.openai.com/v1/files/file-SrYC1bUKEhUQPs271hK2ScXD/content"

headers = {
    "Authorization": f"Bearer {key}"
}

response = requests.get(url_2, headers=headers)

if response.status_code == 200:
    print("Request successful!")
    data = response.json()
    print(response)
    # Do something with the response data
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)  # Print error message if available
