'''
This file contains the library for Firebase Realtime Database
'''

import urequests

class FirebaseRTDB:
    def __init__(self, firebase_url):
        self.firebase_url = firebase_url
    
    def write(self, path, data):
        url = f"{self.firebase_url}/{path}.json"
        response = urequests.put(url, json=data)
        response.close()

    def read(self, path = ""):
        url = f"{self.firebase_url}/{path}.json"
        response = urequests.get(url)
        data = response.json()
        response.close()
        return data

    def update(self, path, data):
        url = f"{self.firebase_url}/{path}.json"
        if isinstance(data, dict):
            try:
                response = urequests.patch(url, json=data) 
                data = response.json()
                response.close()
                return data
            except:
                return None
        else:
            return None

    def delete(self, path):
        url = f"{self.firebase_url}/{path}.json"
        try:
            response = urequests.delete(url)
            response.close()
            return True
        except:
            return False
        