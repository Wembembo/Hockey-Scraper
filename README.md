# NIHL National Schedule Scraper

A Python-based web scraper designed to extract hockey game schedules, scores, and team information from the **NIHL National** website. It processes the hierarchical HTML structure of the schedule page and converts it into a structured, machine-readable JSON format.

Running the code found in heatmap.py, this will output a headmap showing how a team is performing while playing away based on goal differential 

## Features

* **Date Tracking**: Automatically associates games with their respective date headers using a state-tracking logic.
* **Asset Extraction**: Pulls team names directly from image metadata (`alt` tags) for high accuracy.
* **Clean Data**: Strips unnecessary whitespace and handles "N/A" values for missing times or scores.
* **Robust Selectors**: Uses lambda functions to match dynamic CSS grid classes, making the script resistant to minor layout changes.

## Prerequisites

Before running the script, ensure you have the following installed:

* Python 3.x
* `requests` library
* `beautifulsoup4` library
* `pandas` library
* `seaborn` library
* `matplotlib` library

You can install the dependencies via pip:

```bash
pip install requests beautifulsoup4 pandas seaborn matplotlib
```` 

