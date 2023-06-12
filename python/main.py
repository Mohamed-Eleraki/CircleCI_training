import requests


print('Hello, From Building python app.....')

#3
try:
    response = requests.get('http://google.com')  # get the website code status result
    if response.status_code == 200:  # if Okay print the below statement
        print('Website is running successfully!')
    else:  # if not Send an email
        print('Website down, Fix it!')


except Exception as ex:  # catch the err in ex
    print(f'connection error happened {ex}')  # print out the error
    
