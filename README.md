# Page titles sorter

These python scripts are used to sort Wikipedia pages titles per views.

## Analitics downloader

This script take in input a file containing raw Wikipedia names and use the Wikipedia API to retrieve the number of views during the last year for each page.
The script output the date in a csv file with two columns, one for the page title and the other for the page view count.
Given the fact that the each page generate one fetch request the time to process each page title is very long (about 1 full month).

## Page sorter

This script take in input the file result of the Analitics downloader script and sort the page in decreasing order based on page view.
The output is an csv file in the same format as for the Analitics downloader script.

## Requirments

To use the script you will need raw input data from Wikipedia dumps. The file needs to be placed in a folder named "data" and the file should be named "data.txt".

The script use a lib called "requests" to fetch the Wikipedia API.

```properties
pip install requests
```

## Usage

Each script can be run with:

```properties
python {{script-name}}.py
```

OR

```properties
python3 {{script-name}}.py
```

There are no parameters needed and no input will requested. This means that those script can be run in the background with the nohup command for exemple.
The ONLY requirements are the data file to be correctly placed and named.