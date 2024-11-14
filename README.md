# COASTAL GARDENS

![Main Mockup](README-files/main-mockup.png)

[View Live Website here.](https://coastal-gardens-e950c82335fb.herokuapp.com/)

[GitHub Repo](https://github.com/LemmenAid/coastal-gardens)

*** 

## Project Description  

_Coastal Gardens is a interactive website for my fourth portfolio project with [Code Institute](https://codeinstitute.net/ie/)._

Coastal Gardens is a web platform designed to connect and support coastal gardeners in Ireland and the UK. Focused on the unique challenges and rewards of gardening by the sea, the site provides accessible resources, insights, and a collaborative space for gardeners. Users can browse a curated selection of feature posts, explore their plant zone, and, by becoming members, unlock a personalized dashboard. Members have the opportunity to save favorite posts, keep track of their comments, and publish their own garden stories to inspire other coastal enthusiasts.

## Project Purpose

The purpose of Coastal Gardens is to foster a vibrant online community dedicated to coastal gardening. Recognizing the specific needs of the coastal region, the platform aims to be a comprehensive resource for both beginners and seasoned gardeners facing the unique conditions of seaside environments. By providing a space for knowledge exchange, storytelling, and advice, Coastal Gardens empowers gardeners to create thriving, resilient gardens and build connections with others who share similar experiences.

***

## Index – Table of Contents

* [User Experience (UX)](#user-experience)
* [Creating Process](#creating-process)
* [Design](#design)
* [Features](#features)
* [Libraries and Technologies Used](#libraries-and-technologies-used)
* [Testing](#testing)
* [Solved Bugs](#solved-bugs)
* [Deployment](#deployment)
* [Credits](#credits)

***

## User Experience (UX)

### User Stories

1. As a Visitor, I want to browse feature articles on coastal gardening, so that I can learn more about gardening by the sea.
2. As a Visitor, I want to understand the plant zone map, so I can determine in which zone I live.
3. As a Visitor, I want to read an About page to understand the purpose and mission of the site.
4. As a Visitor, I want to easily navigate to different sections of the site, so I can find relevant information quickly.

5. As a Potential Member, I want to view a sign-up page that explains the benefits of joining, so I know why I should become a member.
6. As a Potential Member, I want a simple registration process, so I can quickly join the community.

7. As a Member, I want a personalized dashboard where I can save and view my favorite articles, so I can easily revisit them.
8. As a Member, I want to see a list of all my comments in one place, so I can keep track of my participation.
9. As a Member, I want the ability to write and publish my own gardening stories, so I can share my experiences with other members.
10. As a Member, I want access to member-only stories, so I can learn from the experiences of other coastal gardeners.

11. As an Admin, I want to manage feature posts and member stories, so that the content is relevant, accurate, and engaging for users.
12. As an Admin, I want to moderate comments, so I can ensure a respectful and constructive environment.
13. As an Admin, I want to manage user accounts, so I can assist with membership issues and maintain site quality.

***

## Creating Process

When I started developing Coastal Gardens, it was my first time working on a project that combined both backend and frontend development, and my second time using Python. This project presented a steep learning curve, especially as I tackled the challenges of Django, CSS, and user interactivity. I wanted to create something with real-world application, so the idea of a resource for coastal gardeners felt both meaningful and practical.

At the beginning, I felt unsure about how to approach the project, but as I started coding, things began to click. Working through each part of the website—from creating personalized dashboards to designing the user experience—helped me better understand the concepts from my lessons. The process not only taught me more about Python logic and web frameworks, but also boosted my confidence as I realized I could solve problems and make the website functional.

The creative process became really enjoyable as I saw the website take shape, and I'm proud that it’s a tool gardeners in Ireland and the UK can use to share stories, access local gardening advice, and find inspiration for their coastal spaces.

### Project SetUp

For setting up Coastal Gardens, I followed the CodeStar follow-along project structure, customizing it to create a unique platform for coastal gardening enthusiasts.

I began by building a Django framework, developing the foundational pages (Home, About, Features, and Zone Map) that offer general information to anyone interested in coastal gardening. Once this structure was stable, I added unique member features, including personalized dashboards and the option for members to write and share blog posts exclusively within the community.

This was my first experience handling both backend and frontend tasks together, which was challenging but rewarding. Developing these elements involved custom logic for saving, displaying, and managing user-generated content in a way that’s engaging and intuitive. Testing each step along the way helped me ensure smooth functionality and an accessible user experience.

Overall, this process taught me a lot about web development and reinforced concepts from my coursework in a real-world setting, helping me build confidence in my coding abilities.

Jump to Credits: [Credits](#credits)

***

## Design

### Colour Scheme

![alt text](README-files/colour-palette.png)

The Coastal Gardens colour scheme draws inspiration from coastal landscapes, incorporating natural tones that aligns with the garden-focused theme.

* The palette centers on a calming green to echo the lushness of coastal plant life, balanced by subtle, neutral tones to maintain clarity and focus. 
* Light neutrals and deep charcoal are used for contrast, ensuring readability and accessible text elements without overwhelming the page.

This palette creates a welcoming environment that mirrors nature while being easy to navigate and visually pleasant.

### Typography

* The typography on Coastal Gardens combines Cormorant Garamond with Roboto, a clean sans-serif font, to create a modern magazine-like feel. Cormorant Garamond adds an elegant, editorial touch, while the Roboto font keeps the content easy to read and approachable. 

The following code has been imported into the top of the base.html file

    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&display=swap" rel="stylesheet">

    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">

![alt text](README-files/roboto.png)<br>
![alt text](README-files/cormorant.png)<br>

### Call to Action

* The call to action button on the homepage leads to the Sign Up page, unless you are signed in as a member, then it leads to your personalised Dashboard.

![alt text](README-files/action-button.png)<br>

### Imagery

Several image sources were used for the images throughout the website.<br>
The links to these sources are listed here:

* [Hero Image, Bells of Ireland](https://floralife.com/article/bells-of-ireland-troubleshooting/)
* Photo by Image Hunter: https://www.pexels.com/photo/hand-holding-note-on-green-bush-background-13092789/
* Photo by Lukas Medvedevas: https://www.pexels.com/photo/a-man-standing-on-the-mountain-6013664/
* Photo by Vicky Sim: https://unsplash.com/photos/brown-and-white-1-storey-house-surrounded-by-trees-VYRc_uIafIg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash/
* Photo by Dmitrij Paskevic: https://unsplash.com/photos/white-concrete-house-beside-road-SGuK8EIUx_Y?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash/
* Photo by Johny Goerend: https://unsplash.com/photos/aerial-view-of-green-grass-field-near-body-of-water-during-daytime-cGMTvIzhmAA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash/
* https://www.lummi.ai/photo/a-close-up-view-of-a-lake-and-grass-near-a-cabin-in-t-e8db6be2-994a-4f68-b3f3-54493d2929d8-GuY3A
* https://www.lummi.ai/photo/underwater-serenity-hx6rp
* Photo by Steve W: https://www.pexels.com/photo/close-up-photo-of-labrador-on-flower-field-4200202/
* Photo by Wynand van Poortvliet: https://unsplash.com/photos/two-black-and-white-birds-4AmyOdXZAQc?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash/
* Photo by Kristina Paukshtite: https://www.pexels.com/photo/blue-white-and-red-poppy-flower-field-712876/
* Photo by Joerg Hartmann from Pexels: https://www.pexels.com/photo/poppy-on-meadow-17832251/
* Photo by Photo By: Kaboompics.com: https://www.pexels.com/photo/person-in-brown-shorts-watering-the-plants-4750270/
* Photo by Roy Manuhutu: https://www.pexels.com/photo/close-up-photo-of-flower-with-spiderweb-4099836/
* Photo by Helena Jankovičová Kováčová from Pexels: https://www.pexels.com/photo/red-poppies-on-meadow-25578696/
* Photo by Helena Jankovičová Kováčová: https://www.pexels.com/photo/close-up-of-red-berries-on-a-branch-outdoors-29238660/
* https://www.gardensillustrated.com/features/wildlife-sand-habitats-gardens
* Photo by Brendan Rühli: https://www.pexels.com/photo/close-up-of-blue-flowers-7268049/
* Photo by Amie Roussel: https://www.pexels.com/photo/gardener-in-autumn-sunflower-garden-28965902/
* Photo by Everson Marcos de Carvalho: https://www.pexels.com/photo/latin-american-fleabane-in-close-up-shot-12711555/
* Photo by Tommes Frites: https://www.pexels.com/photo/a-single-cornflower-in-a-field-with-wheat-27797805/
* Photo by Werner Redlich: https://www.pexels.com/photo/purple-foxglove-flowers-24287691/
* Photo by Drew Anderson: https://www.pexels.com/photo/branch-of-blooming-tree-with-blossoms-5549936/
* Photo by Daniil Komov: https://www.pexels.com/photo/black-and-gray-bird-flying-in-the-sky-10662583/
* https://www.lummi.ai/photo/a-close-up-view-of-a-lake-and-grass-near-a-cabin-in-t-e8db6be2-994a-4f68-b3f3-54493d2929d8-GuY3A/
* https://www.goodeggs.com/repettonursery/bells-of-ireland/5c82e8ba2a974d000e7099fe/


***


## Layout / Wireframes

* The basic design layout of the website has been made using wireframes with Balsamiq. 
* Responsive design has been used for creating this website. For instance, when a page goes from mobile to larger screens some of the content goes from stacked to lined up.

#### Home Page
![alt text](README-files/wireframe-main.png)<br>

#### Text Pages
![alt text](README-files/wireframe-text-page.png)<br>

#### Feature Page
![alt text](README-files/wireframe-features.png)<br>

#### Mobile View
![alt text](README-files/mb-all-wireframe.png)<br>


***


## Features 

### General Features on each page

#### Navigation Bar

* Featured on all pages, the full responsive navigation bar includes links to the Home page, About, Features, Sign Up, Login, and Contact Us page and is identical in each page to allow for easy navigation. This will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button. 

* If a member is logged in the Dashboard page and Member Stories page will also be visible in the navigation bar. 

Navigation bar:<br>
![Nav Bar](README-files/navbar.png)

Navigation bar for members:<br>
![Nav Bar](README-files/navbar-member.png)

Dropdown navigation menu:<br>
![Nav Bar dropdown menu](README-files/navbar-drop.png)

#### The Footer

* Featured on all three pages, the footer section includes the contact information of the club.
* The footer section includes links to the relevant social media sites for Atlantic Dippers. The links will open to a new tab to allow easy navigation for the user. 


![Footer](README-files/footer.png)

#### Square Links

* The Square Links make it easy for users to navigate between pages while also adding visual appeal that encourages exploration across the site.

![Nav Bar](README-files/square-links.png)

### Features by page

#### Home Page
The Home Page serves as an inviting introduction to Coastal Gardens with a captivating hero image and a clear call-to-action button leading to the sign-up page. The "What's New?" section highlights the three latest posts, keeping content fresh and engaging for returning visitors. Below, visually appealing square links guide users to key pages, offering easy navigation across the site.

![Home Page](README-files/home-page.png)

#### About Us Page
The About Us page introduces Coastal Gardens’ mission, explaining the importance of community and knowledge-sharing for coastal gardening enthusiasts in the UK and Ireland. It helps new users understand the site's goals and encourages them to join.

![About Us](README-files/about.png)

#### Features Page
The Features page showcases Coastal Gardens' most recent articles and resources, displayed from newest to oldest. This page offers a broad view of content, covering expert tips, gardening insights, and coastal plant recommendations.

![Features](README-files/features.png)

#### Dashboard
The personalized Dashboard page provides logged-in members with an overview of their saved features, their own written stories, and all comments they’ve made. A “Create Story” button is available, allowing members to publish their own coastal gardening experiences directly to the Member Stories page.

![Dashboard](README-files/dashboard.png)

#### Create Story
This page allows members to create and publish their own stories by inputting a title, uploading an image, and writing a blog post and excerpt. The user-friendly layout encourages members to share their knowledge and unique gardening experiences.

![Create Story](README-files/create-story.png)

#### Member Stories
The Member Stories page is a member-exclusive section where users can read stories and insights shared by other community members. This feature encourages a sense of community and gives members access to firsthand experiences in coastal gardening.

![Member Stories](README-files/member-stories.png)

#### Sign Up Page
The Sign-Up page includes standard registration fields with added questions about gardening experience level and the user’s garden zone. This customization helps Coastal Gardens offer a more tailored experience for each member.

![Sign Up](README-files/signup.png)

#### Contact Us Page
The Contact Us page provides a direct way for users to reach out with inquiries or feedback. It ensures members feel supported and have access to help if needed.

![Sign Up](README-files/contact.png)


### Future Implementations

* One future feature planned for Coastal Gardens is a Reddit-style Q&A advice page. This page would allow members to post gardening questions and receive answers from the community, promoting knowledge-sharing among users with various experience levels. Members could upvote helpful responses, making it easy to identify valuable advice and reliable contributors. This addition would create an interactive support space, further enhancing the community feel of Coastal Gardens.

* Another future enhancement could be a “Garden Planner” feature. This planner could provide personalized monthly to-do lists where gardeners can focus on timely tasks like planting, pruning, and seasonal maintenance.

*** 

## Libraries and Technologies Used

* [Github](https://github.com/) - Used for hosting the repository.
* [Heroku](https://heroku.com/) - Used for deploying the live project.
* [Gitpod](https://www.gitpod.io/#get-started) - Used for developing the application.
* [Python](https://www.python.org/) - Used for adding functionality to the application.
* [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used for validation python code.

### Python Libraries


***

## Testing


### Python Validation

The [CI Python Linter](https://pep8ci.herokuapp.com/#) is used for validation python code. The run.py file was checked and a few errors were reported:

![pep8](README-files/pep8.png)

<br>
After fixing the errors, no errors were reported:

![pep-8-after](README-files/pep8-after.png) 


### Input Testing

During developments User input has been tested frequently to check if various inputs were valid, namely if the validation functions were catching all errors as expected. It was important that the User could easily navigate back to different Counties and surfspot options, as well as exiting the app. When testing User input I have repeatedly used the same set of input values: "Enter button only", "test" and "123".

All tests were completed in the local terminal as well as in the Heroku terminal.

| Feature                    | Tested?    | User Feedback Provided      |
|----------------------------|------------|-----------------------------|
| Choose County              | Yes        | Sorry, {user_county} is not a valid county. |
| Choose surfspot            | Yes        | {selected_spot} is not a valid surfspot. Please enter one of the available options.|
| Program continue options   | Yes        | {restart} is not a valid input! Please enter Y, N or C. |
| Exit                       | Yes        | Goodbye message is displayed. |


### Browser Testing  
Surf Spot Finder was tested through the Heroku app website on the following browsers without issues:  
- Google Chrome (Version 126.0.6478.182)
- Mozilla Firefox (Version 127.0.2)  
- Microsoft Edge (Version Version 126.0.2592.102) 

***

## Solved Bugs

* One bug that came up during testing was quite interesting and was only discovered by accident. The correct name for a County was entered, but accidentally had a blank space in front of it, the input was returned as not valid. After looking into this, I found that this could be solved by calling the .strip() function before calling the .capitalize() function on the User input:

 ![blank space bug](README-files/blank-bug.png)

***

## Deployment to Heroku

### Project Deployment

_I have used several different READMEs to write the deployment section of this README.<br> 
All listed in the credit section below._<br>

The application was deployed to Heroku. In order to deploy, the following steps were taken:

1. If you have an account, login to Heroku. Otherwise create a new account.
2. Once signed in, click the "New" button in the top right corner, below the header and choose "Create new app".
3. Choose a unique name for the application and select your region. When done, click "Create app".
4. This brings you to the "Deploy" tab. From here, click the "Settings" tab and scroll down to the "Config Vars" section and click on "Reveal Config Vars". 

- In the KEY input field, enter "PORT" and in the VALUE input field, enter "8000". After that, click the "Add" button on the right.

- In KEY enter "CREDS", in VALUE, paste in the text content of your CREDS.json file. 

5. In the Settings tab, in the Buildpack section, click the button "Add Buildpack".
6. First add "Python" package and then "node.js". 
7. If you exchanged the order of the packages: the Python buildpack must be above the NodeJS buildpack. You can drag the Python buildback to the top.
8. Scroll back to the top of the page and go to the "Deploy" tab. Choose "GitHub" as your Deployment method.
9. Go to "Connect to GiHub" section, search for the repository name and click "Connect".
10. In the "Automatic Deploys" section, choose your preferred method for deployment. I chose the 'automatic' option. Click "Deploy Branch".
11. Once the building of the app is finished you can click the "view" button to be redirected to the newly deployed site.

### Forking repo on GitHub

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

***

## Credits

* I would like to thank Brian Macharia for his great mentor support and guidance - helping me through the process of building my first ever CLI application.
* My facilitator Amy from Code Institute for supporting us through our third project and giving us great tips and resources for learning tools, and her feedback during the weekly stand-ups.
* At last I would like to give thanks to my friends and family for taking the time to test the application and giving me great feedback.

### Content

I have taken information from the following websites for the Surf Spot Google Sheet:
* [Surf Forecast](https://www.surf-forecast.com/)
* [Discovering Cork](http://www.discoveringcork.ie/surfing/)
* [Surfer Today](https://www.surfertoday.com/surfing/the-best-surf-spots-in-ireland)
* [Surfline](https://www.surfline.com/travel/ireland-surfing-and-beaches/2963597)


### Code

The walkthrough project "Love Sandwiches" was a great way of understanding how to get started on an CLI application and it was therefor a good source of inspiration. 
I decided to make an app that can help users to find information on surfspots per County in Ireland. 
I have used various resources to help me with figuring out how to create the Surf Spot Finder app:

* [Stack overflow](https://stackoverflow.com/)
* [Pep Style Guide](https://peps.python.org/pep-0008/)
* [W3Schools](https://www.w3schools.com/)
* [The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/style/)
* [Real Python - for quick tutorials on several subjects](https://realpython.com/)
* [Real Python - Name-Main](https://realpython.com/if-name-main-python/)
* [Real Python - While loops](https://realpython.com/python-while-loop/)
* [Pypi - ASCII title banner](https://pypi.org/project/pyfiglet/)
* [Stack Overflow - Slow Printing](https://stackoverflow.com/questions/15375368/slow-word-by-word-terminal-printing-in-python)
* [Stack Overflow - clear terminal](https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python)
* [W3Schools - strip()](https://www.w3schools.com/python/ref_string_strip.asp)
* [Tripleten - best practices](https://tripleten.com/blog/posts/python-best-practices)

* Code Institute Slack Channel


### Templates I have used for inspiration and creating my readme-file:

I have used several readme file as inspiration to write this readme:

* [Sample README Code Institute](https://github.com/Code-Institute-Solutions/SampleREADME/blob/master/README.md?plain=1) - Copied the Deployment section and used for general guideline.
* [Towers of Hanoi - Lucia2007](https://github.com/lucia2007/towers-of-hanoi/) - For general inspiration and the Heroku Deployment section for this readme.
* [Weather Checker - mdurmus](https://github.com/mdurmus/weather-checker/) - Used for general guideline.
* [Read Me Template Code Institute](https://github.com/Code-Institute-Solutions/readme-template/blob/master/README.md)
Used for general guideline.
* [Plant Factory - crypticCaroline](https://github.com/crypticCaroline/ms1-plantfactory/blob/master/README.md?plain=1) - Especially for the Technologies Used, Testing sections and design sections.
* [Visit Järbo - ClaudiaInSweden](https://github.com/ClaudiaInSweden/visit-jarbo/blob/main/README.md?plain=1) - General inspiration / guideline.
* [GitHub Docs](https://docs.github.com/en)