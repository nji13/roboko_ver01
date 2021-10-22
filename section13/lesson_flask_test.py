import requests

r = requests.get('http://127.0.0.1:5000/employee/kinji')
print(r.text)

r = requests.post('http://127.0.0.1:5000/employee', data={'name': 'kinji'})
print(r.text)

r = requests.put('http://127.0.0.1:5000/employee', data={'name': 'kinji', 'new_name': 'hasegawa'})
print(r.text)

r = requests.delete('http://127.0.0.1:5000/employee', data={'name': 'kinji'})
print(r.text)