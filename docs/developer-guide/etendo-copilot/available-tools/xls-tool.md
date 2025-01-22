---
title: XLS Tool
tags:
    - Copilot
    - XLS Processing
    - Data Extraction
    - Excel
    - Google Sheets
    - CSV
---

# XLS Tool

:octicons-package-16: Javapackage: `com.etendoerp.copilot.toolpack`

## Overview

The XLS Tool processes `XLS` or `CSV` files to extract data. It is designed to facilitate tasks such as parsing spreadsheet content, processing tabular data, and extracting specific information from XLS files. The tool accepts the file path of an data file and returns processed data based on defined parameters.

!!!info
    To include this functionality, the Copilot Extensions Bundle must be installed. Follow the instructions from the marketplace: [Copilot Extensions Bundle](https://marketplace.etendo.cloud/?#/product-details?module=82C5DA1B57884611ABA8F025619D4C05){target="\_blank"}. For more information about available versions, core compatibility, and new features, visit [Copilot Extensions - Release notes](../../../whats-new/release-notes/etendo-copilot/bundles/release-notes.md).

## Functionality

This tool automates the process of **data extraction from XLS files**. It is particularly useful for tasks such as reading financial data, extracting customer details, or parsing inventory records. The tool supports customizable processing logic to handle diverse data structures.

Using this tool consists of the following actions:

- **Receiving Parameters**:

    - The tool receives an input object containing the file path of the XLS file to be processed and optional parameters for data extraction.
    - **path**: The path of the XLS file to be processed.
    - **parameters**: Optional extraction parameters such as sheet name, specific rows, or columns.

- **Processing the File**:

    - The tool reads the XLS file from the specified path, verifies its existence, and ensures the file format is supported.
    - It processes the file based on the input parameters to extract the required data.

- **Returning the Result**:

    - The tool returns a JSON object containing the extracted data.
    - **data**: The processed data extracted from the XLS file.

## Usage Example

### Extracting data from an XLS file

Suppose you have an Excel file at `/home/user/data.xls` and you want to extract customer information from the file:

**XLS Content**
``` txt
| Customer ID | Name       | Purchase Amount |
|-------------|------------|-----------------|
| 1001        | John Doe   | 500             |
| 1002        | Jane Smith | 300             |
```

- Use the tool as follows:

    - **Input**:

        ```
        {
            "path": "/home/user/data.xls",
            "parameters": {
                "sheet": "Customers",
                "columns": ["Customer ID", "Name", "Purchase Amount"]
            }
        }
        ```

    - **Output**:

        ```Json title="Output Json"
        {
            "data": [
                {"Customer ID": "1001", "Name": "John Doe", "Purchase Amount": 500},
                {"Customer ID": "1002", "Name": "Jane Smith", "Purchase Amount": 300}
            ]
        }
        ```

!!!note
    The result of the tool can be used as input for other processes. For instance, the extracted customer data can be utilized to generate personalized marketing campaigns or invoices.

