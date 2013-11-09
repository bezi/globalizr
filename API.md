API
===
Frontend api:

/api/query/&lt;query&gt;/
-------------------------
Returns json of the form:
```
{
    "query": query,  //query string
    "status": 0|1,  // 1 if there is an error
}
```

/api/interface/&lt;interface&gt;/&lt;metric&gt;/
------------------------------------------------
Returns json of the form:
```
{
    "name": name, // human readable string describing dataset
    "status": 0|1, // 1 if there is an error
    "data": {
        label1: {
            "name": name, //string
            "data": [ mag1, long1, lat1, . . .] // format read by globe
        },
        label2: {
            "name": name, //string
            "data": [ mag1, long1, lat1, . . .] // format read by globe
        }, . . . 
    }
}
```
