meds_json_formatter

GOAL: FORMAT JSON FILE FOR MEDS UPLOAD

TAKE IN JSON OBJECT

{
    "1002": "Magellan Behavioral Health of FL",
    ...
}

RETURN OBJECT

[
    {
        "code": "1002",
        "item": "Magellan Behavioral Health of FL"
    },
    {
    	 'code': '1002', 
    	 'item': 'Magellan Behavioral Health of FL'
    },


    ...
 ]# MEDS-JSON-Formatter

## STEPS

1. Move current JSON object to root
2. Run by calling Python3.9 meds_json_formatter {JSON file name}
3. Output prints in console and in root folder as a file '{json_path}_output.json'.
