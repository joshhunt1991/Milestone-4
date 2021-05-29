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
[- Next I tried to register as a new user and that worked.] (/readmelinks/register.png) <br/>
[- Next I confirmed the email address that was successfully sent to my address.] (/readmelinks/confirm.png) <br/>
[- Next I signed in.] <br/>
[- After logging back out I tried to sign up again with the same information.] (/readmelinks/duplicate.png) <br/>
[- I then logged back in to ensure that the super user links (product management, profile page, and the edit and delete buttons on the all products page and the product information page") don't show up. I also tried going direct through the url to ensure that I am redirected to the sign in page.] <br/>
[- Finally I logged in as my super user account and ensured that those same buttons were available and that they all worked.] (/readmelinks/duplicate.png) <br/>

### Product management

[- First I tried to submit a blank form to ensure that the validation is working for that] (/readmelinks/empty.png) <br/>
[- Next I submitted an actual test product to confirm that the process works] (/readmelinks/testprod.png) <br/>
[- I then deleted it to test that] <br/>

### profile page

[- First I tried to submit a blank form to ensure that the validation is working for that] (/readmelinks/add-blank.png) <br/>
[- Next I submitted an actual test product to confirm that the process works] (/readmelinks/testprod.png) <br/>

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





