# MyAnimeList.net Scraper

Search for all the anime listed on top of myanimelist.net and save it in json (and optionally csv).

To run the scraper, first open the directory in the terminal and do:

```python
$ scrapy
```

And then:

```python
$ scrapy crawl mal -o mal.json
```
To store the data in the `mal.json` file.

To convert the json to a csv file you can use the `json_to_csv.py` script.
