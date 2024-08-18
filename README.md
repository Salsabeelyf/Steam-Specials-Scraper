# Steam-Specials-Scraper

![Steam Website](<Screenshot from 2024-08-13 22-52-21-1.png>)

## About 

* A python script that scrapes games info from [Steam website](https://store.steampowered.com/specials "Steam website"), then

* Extracts each game info depending on attributes in `config.json`, for example:
    * title
    * link to thumbnail
    * category tags
    * rating
    * number of reviews
    * original price
    * discounted price
    * discount percent
      
## Libraries Used
* Playwright
* Requests
* Selectolax
* Pandas

## Installing

#### Download the code from Github
#### Open CLI and Go to the project folder
#### Run the following command

```
pip install -r requirements.txt
```

## Running
#### If you want to add more attributes for the code to exctract, edit `config.json` file, for example:

```
{
   "name": "description",
   "selector": "div.StoreSaleWidgetShortDesc",
   "match": "first",
   "type": "text"
}
```

#### Run the following command:

```
py main.py
```

## Output
All games info should be extracted and exported into `games_data.csv` file

