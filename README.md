# Toast POS Scraper
#### Python web scraper of POS system Toast for restaurant inventory


This script scrapes Toast to generate a text file listing menu items marked out of stock.

At the restaurant where I work, there's no easy way to quickly determine what has been marked out of stock on the [Toast](https://pos.toasttab.com/) POS system. You can either go through each category and subcategory on the tablet or on the website. Either way it's a long, tedious process.

Ever since I started at Nashville Software School in 2019, I knew I wanted to use programming to solve real world problems, and this seemed like a manageable one to tackle. I hadn't used Python since my first computer science class at MTSU, and I'd never done any web scraping, but I was really eager to try my hand at both. I'm really happy with how ti turned out, and I learned a lot about automation and XPath in the process.



This script uses the [Selenium](https://selenium-python.readthedocs.io/) automation package.

## Process
1. Logs in to Toast with manager credentials using Selenium
2. Uses combination of XPath and CSS selectors to scrape list of item IDs for later requests (weekly)
3. Logs in to Toast with manager credentials using Selenium
4. Saves cookies from session for use in requests (daily)
6. Uses saved cookies and scraped IDs to query backend for item inventory status
7. Writes names of out of stock items to text file
