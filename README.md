# Firebase Realtime Database with MicroPython

This projects provides a MicroPython library for using Google Firebase Realtime Database. At the moment we omit the authentication part so make sure access to your Realtime database is set up properly. This library is free of use and may contain additional features in the future.

## Structure of this repo

If you want to use the library, you need to upload the [firebasertdb.py](firebasertdb.py) file to your microcontroller.

```python
import firebasertdb
```

See [example.py](example.py) for an example on how to use the library.

## Usage of the library

Two things are very important before you can start interacting with the code:

* Make sure to connect to the WIFI network first (if you already do so in your project, there is no need to do it again)
* Create a FirebaseRTDB object where you pass on the FIREBASE_URL (Make sure to assign that variable)

```python
connect_wifi() 
fbrtdb = FirebaseRTDB(FIREBASE_URL)
```

### Write to Firebase Realtime Database

The write function takes 2 arguments:

* path: which is a URI-based path
* data: which takes a dictionary (and can be nested as shown in the example below)

```
fbrtdb.write(path="path/to/object", data={"sensors" : {"temperature": 25, "humidity": 60}})
```

Note that if your want to write to the root of your database, path should be set to "".

### Read from Firebase Realtime Database

The read function takes a single argument and returns the dictionary with the data.

```python
data = fbrtdb.read(path="path/to/object")
```

If a path is specified that does not exist, the return value is None.

### Update in Firebase Realtime Database

The update function takes 2 arguments:

* path: which is a URI-based path
* data: which takes a dictionary

```python
fbrtdb.update(path="path/to/object", data={"temperature" : 30})
```

Note that the difference with write is that update will only replace the specified object whereas write will replace the complete object and hence remove all values that are not specified in the new object.


### Delete from Firebase Realtime Database

The delete function deletes the object on the specified path.

```python
fbrtdb.delete(path="path/to/object")
```

## Troubleshooting

Please create an issue using the built-in issue tracker.
