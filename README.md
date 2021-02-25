# sedr-localdatastore-parser
This is a small parser/formatter script that parses results (CSV file) obtained from parsing Symantec EDR "localdatastore" folder / ".ldb" files.

### Blog
You can read about the Symantec EDR "localdatastore" artifact here:
* https://nasbench.medium.com/forensics-artifacts-symantec-edr-localdatastore-folder-9bff91d2876d (Part I)
* https://nasbench.medium.com/forensics-artifacts-parsing-symantec-edr-localdatastore-leveldb-files-86f5c75736d5 (Part II)

### How To Use
To use this script you need to follow these steps
* First, clone the following repo to your machine : https://github.com/obsidianforensics/ccl_chrome_indexeddb
* Second, copy the "localdatastore" to a location you can work with.
* Execute the "dump_leveldb.py" script to generate the CSV containing the unformatted data.
* Finally execute the script provided here on the CSV file.

```
python sedr_localdatastore_parser.py /path/to/generated/csv/file
```

### Caveats
So far, the script provided in this repo doesn't cover/parse all of the type id provided by Symantec EDR. Only the following type id's are parsed:
* Type ID 8001: Process Event
* Type ID 8003: File Event
* Type ID 8006: Registry Value Event
* Type ID 8007: Network Event

For a complet list of all the available type id's provided by symantec, visit this link: https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/endpoint-detection-and-response/4-5/Event_Schemas_10/search-fields-and-descriptions-v126755396-d38e59231/event-summary-type-ids-v121987556-d38e58861.html

### Extend Functionality
In case the exact "Type ID" you're searching for isn't coverd/parsed yet by this script. You can easily extend it by following these steps:
* First, identify the fields you want to exract from the original CSV. Just copy a single line from the CSV and analyze it manually.
* Second, once you've identifed the fields. Simply create a variable and assign to it the field you want to add. (You need to be at least familiar with python dictionaries).
* Because not all fields are present on all logs, we need to wrap the varaible assignment by a "try"/"except" statement to avoid "key errors"
* Finally, add your variable(s) to both the "f.writerow" statements.
