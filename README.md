# ⒸⒶⓇⒹⓈⒸⓇⒶⓅⒺⓇ
**Work in progress** program to easily manage Magic The Gathering card prices!

<sub>Currently</sub> the program has a script that uses Chromedriver to scrape TCGplayer.com from a predefined list (.csv) of URLs,
scraping the card name, some info, regular price, and foil price and dumping it into a different .csv for use for importing (or in my case copy-pasting) into Google Sheets

## Features
Right now we have a dinky interface ***(It's coming along!)***
that will tell you of errors and when is complete.

Eventually, I would like to add a progress bar, but for now, you have a button to run the script, and a button to close the program. When you run the script it will indicate that it is working on scraping the files, when it is complete it will let you know and provide a button to open your new CSV file!


The program runs Chromedriver headless, 
it grabs your pre-registered URLs in 

`cardlist.csv`

and shortens them to a much more manageable size, and outputs the new URL at the end of each appropriate line
scraped data, for now, includes

```css
   (card name) (card number) (the rarity) (market price) (foil price) (URL)
```

This data is then placed into:

`card_prices.csv`

## Future
I'd like to continue to evolve this project, but it is something in my free time that currently works, so not having a ton of motivation to advance immediately.
future plans for this project:

- Make Pretty*
- Add button to open "cardlist.csv" to add URLs
- ~~Denote if no foil price found~~
- Option to run headless or not in GUI
- Hook into Google Sheets (upload feature?)
- Progress bar?
- Automate searching for cards from names instead of direct URLs
