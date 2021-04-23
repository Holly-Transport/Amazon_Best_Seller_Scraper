# Amazon Best Seller Scraper

This is a Python script that uses Beautiful Soup to scrape Amazon weekly non-fiction best seller lists and save as a .csv file.

![app_screenshot](https://github.com/Holly-Transport/Amazon_Best_Seller_Scraper/blob/master/screenshots/scr_app1.png)

The user can adjust the starting date and number of weeks to query. The database begins the week of May 14, 2017. Note that anything more than 50 weeks can take a super long time to process.

![app_screenshot](https://github.com/Holly-Transport/Amazon_Best_Seller_Scraper/blob/master/screenshots/scr_app2.png)

The output .csv includes week, raking, title, author, publisher, and agent (hey, authors -- maybe this is a good way to find your next agent!). 

![app_screenshot](https://github.com/Holly-Transport/Amazon_Best_Seller_Scraper/blob/master/screenshots/scr_app3.png)

The script would also work for fiction best sellers, as well as the Amazon most-read book lists -- just adjust the base url (keeping the url data as a variable):

Non-Fiction Most Read: https://www.amazon.com/charts/2021-04-18/mostread/nonfiction?ref=chrt_bk_dx_intra_rd_nf<br>
Fiction Most Sold: https://www.amazon.com/charts/2021-04-18/mostsold/fiction?ref=chrt_bk_dx_intra_sd_fc<br>
Fiction Most Read: https://www.amazon.com/charts/2021-04-18/mostread/fiction?ref=chrt_bk_dx_intra_rd_fc<br>


