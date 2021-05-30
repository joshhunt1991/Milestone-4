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

[- Confirmed that the form submits and that blank values can be submitted to clear the form if the user requires] <br/>


### Automated email functionality

[- Confirmed that verification emails are sent and that they work in the "login and registration functionality" section]. <br/>
[- Confirmed that confirmation email is sent when an order is made.] (/readmelinks/posted.png) <br/>

### Responsive design

Below are some images demonstrating the responsiveness of the webpage on different viewport sizes.

- Desktop sizes: <br/>
[- image of the homepage](/readmelinks/homedesktop.png) <br/>
[- image of the products page](/readmelinks/productsdesktop.png) <br/>
[- image of how the product management page looks](/readmelinks/prodmandesktop.png) <br/>
[- image of profile](/readmelinks/profiledesktop.png) <br/>
[- image of shopping bag](/readmelinks/bagdesktop.png) <br/>
[- image of review page](/readmelinks/checkoutdesktop.png) <br/>

- Tablet sizes: <br/>
[- image of the homepage](/readmelinks/hometablet.png) <br/>
[- image of the products page](/readmelinks/productstablet.png) <br/>
[- image of how the product management page looks](/readmelinks/prodmantablet.png) <br/>
[- image of profile](/readmelinks/profiletablet.png) <br/>
[- image of shopping bag](/readmelinks/bagtablet.png) <br/>
[- image of review page](/readmelinks/checkouttablet.png) <br/>

- Mobile sizes: <br/>
[- image of the homepage](/readmelinks/homemobile.png) <br/>
[- image of the products page](/readmelinks/productsmobile.png) <br/>
[- image of how the product management page looks](/readmelinks/prodmanmobile.png) <br/>
[- image of profile](/readmelinks/profilemobile.png) <br/>
[- image of shopping bag](/readmelinks/bagmobile.png) <br/>
[- image of review page](/readmelinks/checkoutmobile.png) <br/>


This wraps up the manual testing section.





