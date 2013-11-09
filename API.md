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
    "status": 0|1, // 1 if there is an error
    "data": {
        "name": name, //string
        "data": [ mag1, long1, lat1, . . .] // format read by globe
    }
}
```
