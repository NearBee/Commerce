# CS50 Project 2: Commerce  

### *Brief description*:  https://youtu.be/4V2CcP6vZqA (Video Demo)
In this project we were assigned the objective of creating a website with a feel in similarity with that of Ebay. What came along with this task was using ***Python*** and ***Django*** hand in hand to create both the front-end as well as the back-end for the website. There is a very tiny bit of Javascript that I sought out and interpreted in my own way but I have no experience personally with it at all so there is very little.

---

## Registration Page:
Where I would suggest a user to head to first (though not required to actually view the contents of most pages) would be towards the registration page. Using the combination of models.py and forms.py with Django I was able to make a very sleek (in my opinion) and modern looking registration form. One of the things I would like to do in the future is refactor the code to return teh form back to the user with the fields lit up as an error for better recogrnition of where a problem might be occuring.
<br><br>
![Registration Page](/commerce/auctions/README_imgs/register_page.png)

---

## Index Page:
The index page is also where I house all of the current *Active Listings*, that being listings that are currently being able to be bid on. I would like to in the future possibly create a seperate view on the same page for the user's watchlisted items to be shown at the top of the screen but that is on the backlog for things to do on the website.
<br><br> 
![Index/Active Listing Page](/commerce/auctions/README_imgs/index_page.png)

---

## Create Listing Page:
The create listing page allows for any user to be able to have the ability to create a listing of their own. The only required fields being, Title, Description and Initial price. Users also have the ability to optionally add an accompanying picture that will attach to the auction as well as choose from a list of categories to allow for a other users to find the item with more specific searches.
<br><br>
![Create Listing Page](/commerce/auctions/README_imgs/create_listing_page.png)

---

## Categories Page:
The categories page will be a more specific version of the index page, only displaying items from the chosen category but in the end it looks very similar to the index page in style.
<br><br>
![Category Page](/commerce/auctions/README_imgs/categories_page.png)

---

## Listing Page:
On the listing page the item is shown with an optional picture on the left (if none is provided instead a placeholder picture of questionmarks will show up), then the title with the lister, the current amount of users watching the post (when not the lister of the post there is the ability to watch the post), and a description of the post, then a section showing the current bid on the item, next to it for users that **aren't the lister** there would be an input box for a new bid which must be higher than the currently posted bid, otherwise for the case that you **are the lister** there would be two seperate buttons which show up in different cases, it will be a *Green Accept Bid* button if there is an active bid on the auction and it will send the listing to the closed auction page, or a *Red Cancel Auction* button if there are no current bids on the auction and that will just cancel/delete the auction.
<br><br>
![Active Listing with Accept Bid button](/commerce/auctions/README_imgs/Listed_Item.png)

---

## Watchlist Page:
The watchlist page is a way for users to keep an eye on listings that they want to check back on later. Users can freely watch/unwatch items as they please on the active items listing page, but then an item is closed by any means (whether that be deleted or closed due to a winning bid being chosen) then it will subsequently be removed from the watchlist (I am currently going back and forth with this decision though I believe it's better for the closed item to not be there it might be better to just show that the item has been closed tbd).
<br><br>
![Watchlist Page](/commerce/auctions/README_imgs/watchlist_page.png)

---

## Closed Listing Page:
The closed listing page would be there users can go to see previous items that have been closed and a winning bid has been chosen, it displays similarly to the index page but instead of just a dollar amount at the end of the card there would also be the winner that submitted the said bid.
<br><br>
![Closed Listing Page](/commerce/auctions/README_imgs/closed_listings_page.png)

Thank you for taking time to read this README about my commerce page, I look forward to creating more in the future as well!
