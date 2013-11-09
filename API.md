API
===
Frontend api:

/api/query/&lt;query&gt;/
-------------------------
Returns json of the form:
```
{
    "query": query,  //query string
    "error": 0|1,  // 1 if there is an error
}
```
