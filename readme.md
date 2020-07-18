### Introduction

In this repo, i'm going to make a quick and simple webpage using Python Flask, jQuery and Bootstrap.  This is a simple back-end for freont-end style microservice, except that I're also hosting a single-page app with the same API.  

This simple Python based microservice using Flask will returns stock quote and historical data. I'll also make a quick website using Flask's template system, called Jinja to make an easy Bootstrap 4 site.  The site will feature a graph of the stock's performance over the period of 12 months. 

I'e going to use the yFinance module for Python.  This module uses the Yahoo Finance API to provide it's data. This API is publicly accessible, but not guaranteed to perform for long-term production use. 

Just some history here.  Yahoo Finance used to provide a comma-separated, and later a JSON api in their YUI library that provided reliable stock quote data.  Unfortunately, the times changed and the classic Yahoo Finance API was taken out of prod.



### Sample Code for this Project

Thank you for checking out my code!  This is a public repository .  If you want to clone or fork the code to your local machine, by all means please do!  Thank you for looking at the code, and you're always welcoe to send a pull request if you want to make a change.

from command line...
```bash
git clone https://github.com/rajshahdev/stockwatch
```


### Pulling the API Content with AJAX

Now everything else will be done directly from JavaScript. We will query the stock API using jQuery's AJAX method, and get the quote and historical information. Since here are two calls, first we will get the quote, and then we will pull the history. This could also be done a little differently by pulling the quote and history simultaneously, but that's not how I set it up this time.


### Conclusion

In this article we used Python and Flask to make a simple stock market API that can pull data form Yahoo Finance and then apply it to create a simple website that shows a stock market chart.

Yet the stockwatch app is not built fully i am continue to update this repo.
