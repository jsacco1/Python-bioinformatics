#!/usr/bin/env python3
""" ---
CLI for a simple json query of meta-data via NCI GDC API.

author: James Sacco
date: 2020-12-09
output:
    submission request output file names
--- """ 

"See https://docs.gdc.cancer.gov/API/Users_Guide/Appendix_A_Available_Fields/ for available fields"

import requests
import json

import sys
import time


def main(primary_site, 
    exp_strategy, 
    data_format):
    """
    Args:
        primary_site: location of tissue. examples: Lung, Skin, Brain, Breast
        exp_strategy: experimental strategy. examples: RNA-Seq, WXS, Genotyping Array, miRNA-Seq
        data_format: format of file. examples: BAM, Gene Expression Quantification
    """


    fields = [
    "file_name",
    "cases.submitter_id",
    "cases.samples.sample_type",
    "cases.disease_type",
    "cases.project.project_id"
    ]

    fields = ",".join(fields)

    files_endpt = "https://api.gdc.cancer.gov/files"

    # This set of filters is nested under an 'and' operator.
    filters = {
        "op": "and",
        "content":[
            {
            "op": "in",
            "content":{
                "field": "cases.project.primary_site",
                "value": [primary_site]
                }
            },
            {
            "op": "in",
            "content":{
                "field": "files.experimental_strategy",
                "value": [exp_strategy]
                }
            },
            {
            "op": "in",
            "content":{
                "field": "files.data_format",
                "value": [data_format]
                }
            }
        ]
    }

    # A POST is used, so the filter parameters can be passed directly as a Dict object.
    params = {
        "filters": filters,
        "fields": fields,
        "format": "TSV",
        "size": "2000"
        }


    print("Querying NCI GDC API (internet connection required)")

    start = time.time()

    # The parameters are passed to 'json' rather than 'params' in this case
    response = requests.post(files_endpt, headers = {"Content-Type": "application/json"}, json = params)

    print(response.content.decode("utf-8"))

    print("Done! Queried {} {} experiment {} files in {}.".format(primary_site, exp_strategy, data_format,time.time() - start))

if __name__ == "__main__":
    if len(sys.argv) == 4:
        primary_site = sys.argv[1]
        exp_strategy = sys.argv[2]
        data_format = sys.argv[3]
        main(primary_site = primary_site, exp_strategy = exp_strategy, data_format = data_format)
    else:
        print("Input required arguments: \n (1) primary site, (2) experiment strategy, (3) data format.\nIf your argument contains whitespace, enclose it in quotes")
