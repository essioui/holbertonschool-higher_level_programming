#!/usr/bin/python3
"""Define module convert csv to json"""
import csv
import json


def convert_csv_to_json(csv_file):
    """
    """
    try:
        data = []
        with open(csv_file, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                data.append(row)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)

        return (True)
    
    except FileNotFoundError:
        return (False)
