# Toast POS Scraper
#### Python web scraper of POS system Toast for restaurant inventory


This script scrapes Toast to generate a text file listing menu items marked out of stock.

At the restaurant where I work, there's no easy way to quickly determine what has been marked out of stock on the [Toast](https://pos.toasttab.com/) POS system. You can either go through each category and subcategory on the tablet or on the website. Either way it's a long, tedious process.

Ever since I started at Nashville Software School in 2019, I knew I wanted to use programming to solve real world problems, and this seemed like a manageable one to tackle. I hadn't used Python since my first computer science class at MTSU, and I'd never done any web scraping, but I was really eager to try my hand at both. I'm really happy with how ti turned out, and I learned a lot about automation and XPath in the process.



This script uses the [Selenium](https://selenium-python.readthedocs.io/) automation package.

## Process
1. Logs in to Toast with manager credentials
2. Clicks through dropdown to select correct restaurant instance
3. Navigates to full menu listing page
4. Uses combination of XPath and CSS selectors to expand menu categories one by one and extract titles of items listed as out of stock
5. Writes names of out of stock items to text file
