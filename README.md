# ⒸⒶⓇⒹⓈⒸⓇⒶⓅⒺⓇ
**Work in progress** program to easily manage Magic The Gathering card prices!

<sub>Currently</sub> the program has a script that uses chromedriver to scrape TCGplayer.com from a predefined list (.csv) of url's,
scraping the card name, some info, regular price and foil price and dumping it into a different .csv for use for importing (or in my case copy-pasting) into Google Sheets

## Features
Right now we have a dinky interface (its a button) that will tell you of errors and when is complete. The program runs chromedriver headless, 
it grabs your pre-registered urls in 
`cardlist.csv`
and shortens them to a much more manageable size, and outputs the new url at the end of each appropriate line
scraped data for now includes (card name) (card number) (rarity) (market price) (foil price) (url)
**important to note that if the card only has a foil version, it will be scraped as only one price- thus placing it into (market price)**
This data is then placed into:
`card_prices.csv`

## Future
I'd like to continue to evolve this project, but it is something in my free time that currently works, so not a ton of motivation to advance immediately.
future plans for this project:

- Make Pretty
- Denote if no foil price found
- Option to run headless or not in gui
- Hook into Google Sheets (upload feature?)
- Progress bar?
- Automate searching for cards from names instead of direct urls
