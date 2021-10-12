# sedr-localdatastore-parser

This is a small parser script that read the results (CSV file) obtained from parsing Symantec EDR "localdatastore" folder / ".ldb" files.

## Blog

You can read about the Symantec EDR "localdatastore" artifact here:

* [**Forensic Artifacts — Symantec EDR “localdatastore” Folder**](https://nasbench.medium.com/forensics-artifacts-symantec-edr-localdatastore-folder-9bff91d2876d)
* [**Forensic Artifacts — Parsing Symantec EDR “localdatastore” LevelDB Files**](https://nasbench.medium.com/forensics-artifacts-parsing-symantec-edr-localdatastore-leveldb-files-86f5c75736d5)

## How To Use

To use this script you need to follow these steps:

* Clone the following repo to your machine :

```git
   git clone https://github.com/obsidianforensics/ccl_chrome_indexeddb
```

* Copy the "localdatastore" to a location you can work with.
* Execute the "dump_leveldb.py" script to generate the CSV containing the unformatted data.
* Finally, execute the script provided here on the CSV file.

```bash
python sedr_localdatastore_parser.py /path/to/generated/csv/file
```

## Caveats

So far, the script provided in this repo doesn't cover/parse all of the type id provided by Symantec EDR. Only the following *Type IDs* are parsed:

* **Type ID 8001**: Process Event
* **Type ID 8003**: File Event
* **Type ID 8006**: Registry Value Event
* **Type ID 8007**: Network Event

For a complete list of all the available type id's provided by Symantec, visit this [**LINK**](https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/endpoint-detection-and-response/4-6/search-fields-and-descriptions-v126755396-d38e59231/event-summary-type-ids-v121987556-d38e58861.html)

## Extend Functionality and Contribute

In case of the exact **Type ID** you're searching for isn't covered/parsed yet by this script. You can easily extend it by following these steps:

1. Identify the fields you want to extract from the original CSV. Just copy a single line from the CSV and analyze it manually.
2. Once you've identified the fields. Create a variable and assign to it the field you want to add. (You need to be at least familiar with python dictionaries).
3. Because not all fields are present on all logs, we need to wrap the variable assignment by a "try"/"except" statement to avoid "key errors"
4. Finally, add your variable(s) to both the "f.writerow" statements.
