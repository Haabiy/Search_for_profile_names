# Search for profile names

Have you ever thought about searching for profiles on LinkedIn and extract information out of it? Well, this repository is made for you !

If you think about it, when you look for profiles manually, you follow the steps below.

`Step 1 : Log into your LinkedIn account`

`step 2 : Type the name of the person on the search bar`

`step 3 : Write down the information you would like to extract`

Now, I want you to imagine you doing the same process for thousands of people, it's ofcourse tiresome and quite tedious work to do. Right?

Here in this repository, I have written the script to automate the exact same process to retrieve data frpm LinkedIn.

***Prerequistes***

`1. In the Authentication.txt file, make sure you put your email and password you use to log into your LinkedIn account`

`2. In the profiles.txt file, list out the names of the people you would like to search on LinkedIn`

E.g : The start looks like this;

![image](https://user-images.githubusercontent.com/76060198/167104904-e0af0a6b-ee6b-47d7-aa5c-56f9e5cd142e.png)

*Enter the number of pages you'd like to scrape per search result :*

![image](https://user-images.githubusercontent.com/76060198/167131193-39aee699-751c-4acb-b82c-1774b39f2743.png)

*Enter the number of key-words you'd like to search on LinkedIn :* this is the number of people you have on your list

`Of course not all search results have exactly the same number of pages but just type upto which page you'd like to go on and if there are search results that are
less or more than the number of pages you specified, the error will be ignored`

***`NB : You may be wondering why not go up to the end of the page for each search result? Well, technically, yes it's possible.`***

![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) How ? 

``` 
While True:
 
    # Unless the next button on LinkedIn is disabled, it will keep going
    
    if 'disabled' in next_button.get_attribute('class'):
        break
    else:
        next_button.click()
```

![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) However you have to also keep in mind that, LinkedIn search results are sorted by based on ***RELEVANCE.*** The people that are displayed on your primary pages are the ones
closer to you and your connections. So, that's why, I didn't need to search for the names through all the pages. 

`Finally, you will have the final extracted file in the same directory as your python script named as LinkedIn_xx. And you can of course change the *path* whenever you want`

`What the code does :`


