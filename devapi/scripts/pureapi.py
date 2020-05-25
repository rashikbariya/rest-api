import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/status/"

def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    print(r.status_code)
    data = r.json()
    print(type(json.dumps(data)))
    for obj in data:
        print(obj['id'])
        if obj['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']) )
            print(r2.json())
    return data


def create_status():
    new_data = {
        'user': 1,
        'content': 'some more new content from server side',
    }
    r = requests.post(BASE_URL + ENDPOINT, data = json.dumps(new_data))
    print(r.status_code)
    print(r.headers)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


# print(create_update())
# print(get_list())

def status_update():
    new_data = {
        'content': 'updated contend',
    }
    r = requests.put(BASE_URL + ENDPOINT + "7/", data = json.dumps(new_data))
    print(r.status_code)
    print(r.headers)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

def status_delete():
    r = requests.delete(BASE_URL + ENDPOINT + "8/")
    print(r.status_code)
    print(r.headers)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

# print(status_delete())
print(status_update())

