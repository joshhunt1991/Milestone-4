![Titan Strength Logo Text](readmelinks/logo.png)

# Titan Strength Testing

## Manual Testing

Manual testing for this project was performed continually throughout the development process as new features were implemeneted to ensure that features worked and that they didn't have unintended consequences for other previously implemented features. For the purposes of this testing document I am going to perform my manual testing using Heroku, working through the app in a logical order from the landing page.

### Landing page

[- first I tested the navigation links returning to the landing all products page] <br/>

### Products page

[- First I tested out all of the filtering options and ensured that the filter box updates the text to reflect this.] (/readmelinks/filtering.png)<br/>
[- Next I clicked on a couple of the products to make sure that the user is redirected to the product information page.] (/readmelinks/info.png) <br/>
[- Then I scrolled to the bottom of the page and made sure that the return to top button functions correctly .] (/readmelinks/rtt.png) <br/>
[- Finally I navigated to the 3 different categories and checked that the product information links work on all those pages .] <br/>

### Product information page

[- First I adjusted the quantity up and down with the buttons to make sure that was working.] (/readmelinks/redirect-2.png)<br/>
[- Next I added a quantity of items to the bag to make sure this was functioning correctly.] (/readmelinks/addtobag.png) <br/>
[- Finally I checked that the keep shopping link works.] <br/>

### Shopping bag page

[- First I changed the quantity of the bag item and clicked the green update button to ensure that this was passing through.] (/readmelinks/update.png)<br/>
[- Next I tested the delete functionality ] (/readmelinks/delete.png) <br/>
[- Finally I confirmed that the secure checkout link works ] (/readmelinks/delete.png) <br/>

### Checkout page

[- The first thing I did before checking the validity of my form was to insert the correct information into the form and submitted it with a test card number to confirm that it works.] (/readmelinks/success.png) <br/>
[- I decided that I would test the key required fields. First for the name I entered a single character name to ensure that the minimum length validation works. Validation works as expected.] (/readmelinks/error.png) <br/>
[- I then decided that I would test the email field by not putting an @ to ensure validation works. Again validation works as expected.] (/readmelinks/error.png) <br/>
[- I then decided that I would test the address line 1 field by putting a 1 character address. Again validation works as expected.] <br/>
[- I went through all the required fields leaving them blank to ensure that the form could not be submitted. Again validation works as expected.] <br/>
[- Typing in invalid credit card numbers works as expected.] (/readmelinks/invalid.png) <br/>



### login and registration functionality

[- First I repeated the checks that I had just done on the checkout form to ensure that Django was taking care of the validation concerns] <br/>
[- Next I tried to register as an already existing user and that was stopped as expected.] (/readmelinks/error.png) <br/>


### Product management

[- Reviews are displaying correctly and are paginated] <br/>
[- Again, I cross checked the displayed reviews with the mongoDB entries to ensure that they are all their and are in the correct order (newest first)] <br/>
[- I checked that the add review button redirects the user to the add review form <br/>

### profile page

[- First I tried to submit a blank form to ensure that the validation is working for that] (/readmelinks/add-blank.png) <br/>
[- As before I realised when testing my validation that I wasn't allowing numbers to be used in the game name which would obviously cause issues, I fixed this and tested it and was correctly redirected to the game images page] <br/>
[- I then posted multiple reviews testing all the ratings radio buttons to ensure that the stars display correctly on the reviews] <br/>
[- Next I tested the review text area, I exceeded the character limit and also put less than the necessary amount to test validation] (/readmelinks/too-short.png) <br/>
[- I filled the form out with gibberish and when no games were found the redirect to the review page and the flash message displayed as expected] (/readmelinks/nogames.png)<br/>
[- Finally I filled the form out correctly with a game that I know exists and returned the game images page] <br/>

### Automated email functionality

[- In the previous section I filled out a review, this review was for call of duty and returned images] (/readmelinks/image-page.png) <br/>
[- I then selected the correct image and it posted as required] (/readmelinks/posted.png) <br/>

### Responsive design

Below are some images demonstrating the responsiveness of the webpage on different viewport sizes.

- Desktop sizes: <br/>
[- image of the homepage](/readmelinks/dhome.png) <br/>
[- image of the about page](/readmelinks/dabout.png) <br/>
[- image of how the forms look](/readmelinks/dforms.png) <br/>
[- image of logged in home page](/readmelinks/dlogged.png) <br/>
[- image of review slider](/readmelinks/dslider.png) <br/>
[- image of review page](/readmelinks/dreviews.png) <br/>

- Tablet sizes: <br/>
[- image of the homepage](/readmelinks/thome.png) <br/>
[- image of the about page](/readmelinks/tabout.png) <br/>
[- image of how the forms look](/readmelinks/tforms.png) <br/>
[- image of logged in home page](/readmelinks/tlogged.png) <br/>
[- image of review slider](/readmelinks/tslider.png) <br/>
[- image of review page](/readmelinks/treviews.png) <br/>

- Mobile sizes: <br/>
[- image of the homepage](/readmelinks/mhome.png) <br/>
[- image of the about page](/readmelinks/mabout.png) <br/>
[- image of how the forms look](/readmelinks/mforms.png) <br/>
[- image of logged in home page](/readmelinks/mlogged.png) <br/>
[- image of review slider](/readmelinks/mslider.png) <br/>
[- image of review page](/readmelinks/mreviews.png) <br/>


This wraps up the manual testing section.





