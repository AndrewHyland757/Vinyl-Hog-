# Vinyl Hog Ecommerce Website

![Image of user landing page on different size screens]()

[Live application can be found here]()

## About
Vinyl Hog operates as a fully functional e-commerce platform built using Django, Python, Javascript, HTML, and CSS. Visitors can browse the records on offer, create an account and make purchaces. 


## Business Goals

- Showcase the businesses products in a clear and organised way.
- Encourage purchaces through seamless site navigation, ability to search for products and provide a easy checkout      experience. 
- A design that appeals to the target demographic and provide them with the necessary information about the products and store. 
- Ability for users to create and azccount to encourage further purchaces and engagement. 

 
## User Experience

### Target Audience

- 12-80 year olds.
- People interested in vinyl records and music in general. 


### User Requirements and Expectations
- A user-friendly website that balances information with an aesthetic thats appealing and modern.
- A mobile-friendly website as purchaces are often made on the go. 
- Information about the store including contact detils.
- A way to book a make a purchace.
- A way to create an account.

- A way to easily access social media accounts from the website.

## User Stories

Agile  was used to keep development in line with the core requirements of the project. In Github a kanban board was created where the user stories 
were located. This made it easy to keep track of getting the essential aspects of the project covered as well as being able to see progress happening as 
the project progressed.

### General User Needs
1. As a user I can intuitively navigate through the website so that I can easily access key information and view desired content.
2. As a user I can find essential information about the company, such as: contact info, delivery info, social medial links and contact details.
3. As a user I can search for certain products.
4. As a user I can sort products.
5. As a user I can view further details on each product such as a product description.
6. As a user I can add and remove products from my shoppong basket.

### Non-Registered User Needs

6. As a non-registered user I can make a purchace without having to spend time creating an account.

### Registered User Needs

7. As a registered user I can make an order as a registered user.
8. As a registered user I can have my my delivery details saved which will auto fill the delivery fields in the checkout page.
9. As a registered user I can view any past orders in my profile page.
10. As a registered user I can save desired products to a wishlist.
11. As a registered user I can easily see if I'm logged in or not so that I can choose to log in or log out depending on what I'm doing.

### Admin User Needs

12. As an admin user I can access the product management page.
13. As an admin user I can add new products to the store and edit or delete required products. 


![Image of user stories]()

## Scope
The website has to achieve the essential user & business goals. The following features will be included in this version:

- A responsive navbar that will have links to all the sections and pages on the website.
- A visually strong landing page that entices the user to further exploration of the business.
- Visual language and styling that reflects the brands values and appeals to the target audience.

- About section with a brief suitable description of the restaurant with three images. ****************

- Products page where users can view the albums available'
- Product page where the customers can view the product in further detail and have the option to add it to their basket, or if logged in their wishlist.
- A basket page where the customer can view the products in their basket and remove and change quantity in necessary. 
- A checkout page where the customer can make a purchace.
 
- A footer section with contact information, social media links, site links and contact details. 
- Register and login pages using Django Allauth.
- A user profile page to view orders made.
- A logout page for logged in users.  


## Front-End Design

### Brief
- A clean, modern and minimal design in monochrome which communicates the brand values.
- Appeal to the target audience.
- Easily navigate and locate necessary information for optimal user expeerience.

### Images

- Each product card includes the cover of each album, or if not avvailable a default image.

### Landing Page
- A visually enticing landing page urging a potential customer to explore the website further and find out more.
- Monochrome and subduded it was important the landing page was in line with the overall design brief of the wepage. 

### Colours
#### Background Colours
- The website uses a light theme throughout. This works well in creating a clean, modern and refined feel to the content as well as enhancing readability.
- For the products grid display and the product page a light grey is used as a background colour. 

#### Styling Colours
![Image of colour palette]()****************************************




### Fonts
- Google fonts DM Sans is used on the brand logo. This sans-serif font has works well in a bold and lowercase configuration as its fullness reflects and compliments the black cirlce it is enclosed in.  

- Helvetica is used on all other text. It offers a clean, refined and legible design, which makes it easy to read on screens of different sizes and resolutions. It has a neutral appearance and doesn't have any distracting features that can make it difficult to read. It is also in line with the refined minimal aesthetic of the website.


## Back-End Design

![Image of database models]()

### User Model
- User model as part of the Django Allauth library contains basic information about the authenticated user and contains the folowing fields: username, password and email.
     
### Artist Model

- This model was created to add an artist for the products. It is connected to Album model with a ForeignKey

### Genre Model

- This custom model holds all the genres. 
- It has a ManyToMany relationship woth the Album model, allowing for more than one genre per album.

### Album Model

- This custom model holds all the albums.
- This includes the a description of the album and a featured image. 
Book This is a custom product model. It is connected to Genre as a ManyToManyField and author as ForeignField. In addition to that it has fields for handling stock. The Stock field holds the integer value of the stock levels; this is updated when a product is purchased. 

### UserWishlist Model

- This model contains the product field which is connected to the Album model as a ForeignField. 
- It also contains a user which will assign the logged-in user from the Allauth User model and assign them to the created instance.


### Flowchat

- When making a booking on the reservation section, the form fields displayed will depend on the user being logged in or not.
- It was import that logged in users were not entering account information like username and email as this would be fustrating. 
- Equally, it was important that non-registered users could make a booking without having to go through the sign-up process. Therefore, a guest user field was included in the Booking model to  handle this. The guest will haver to enter thier email when making a booking. Any  past bookings accociated  with this email will be retrivied if the user decides to create an account later. 
- Once the booking form is validated the code checks if there are any available tables.
- If so, it was important that tables were assigned according to the number of guests, not just the first table from the Table Model.
- The code then finds the best matched table to exclude or lower the number of empty seats. 
- If more that three empty seats is the only availability the booking will not proceed as there will be too many empty seats.


![Image of locic-flow chart](static/images/readme-images/logic-flow.png)



