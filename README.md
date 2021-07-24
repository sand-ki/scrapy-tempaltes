# Scrapy templates
## Content
Some templates for your scrapy project.
Paths are set in config.py.

- pipelines.py: 
    - Custom image pipeline for downloading images automatically to certain location with expiry
    - Custom database pipeline with sql-alchemy
    - Basic data cleaning pipelines (to be finished)

- exporters.py:
    - Csv exporter that formats the csv and drops blank lines
    
-   model.py:
    - Custom database and table creation with sql-alchemy and sqlite

- settings.py:
    - Unchanged
    
 - spiders:
    - Custom basic crawler spider

## Built With
* [scrapy](https://scrapy.org/) - Open source web scraping framework.


