API
===
/api/interface/&lt;interface&gt;/&lt;metric&gt;/&lt;discriminant&gt;/
---------------------------------------------------------------------
Returns json of the form:
```
{
    "name": name, // name of interface
    "status": 0|1, // 1 if there is an error
    "keys": ["disc1", "disc2", . . . ],
    "data": {"disc1": "pos_data": [ mag1, lat1, lon1, . . .], // format read by globe
             "disc2": "pos_data": [ mag1, lat1, lon1, . . .],                         
    },
    "metadata": {"disc1": "description1", "disc2": "description2", . . .} // string descriptors for each discriminant
}
```
Interfaces
----------
All interfaces in the system must also conform to a standard.
```
<interface>.json
{
    "name": <interface>, // name of interface
    "status": 0, // 1 is only written if there is an error
    "keys": ["disc1", "disc2", . . . ],
    "data": {"disc1": [ mag1, lat1, lon1, . . .], // format read by globe
             "disc2": [ mag1, lat1, lon1, . . .],                         
    },
    "metadata": {"disc1": "description1", "disc2": "description2", . . .} // string descriptors for each discriminant
}
```
Interface describes a broad topic, be it weather, finance, or another descriptor.
This is analogous to a top-level database.

The keys array contains "discriminants".  A valid interface cannot have an empty keylist.
If there are no logical divisions of a topic (time intervals, etc), the discriminant is 'default'.  
'default' is also a reserved keyword, and cannot be used if other discriminants in the keylist.

Every discriminant must have a description in the metadata dictionary, even if it's just the empty string. 
(Note, it's probably good practice to write something.)  However, try to keep the descriptions short, as
they are sent out with the data.  
