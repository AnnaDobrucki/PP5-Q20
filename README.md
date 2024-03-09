# 20 Sided Queer

![API Page View](/documentation/image_tests/HomePageAPI.png)

- You can find the link to the live API site [here](/https://pp5-q20-adf89388b6ef.herokuapp.com/)
- You can find the link to the Front-End GitHub Repo [here](https://github.com/AnnaDobrucki/q20-frontend-v2)
- You can find the link to the Back-End API [here](https://github.com/AnnaDobrucki/PP5-Q20-API)

## CONTENTS

* [Introduction](#20-sided-queer)

* 20 Sided Queer has been created to allow like minded queer's who enjoy ttrpg games (mostly DnD), to come together and post content, create events and share their love of all things happening within the TTRPG world right now!

* [Sections and Apps](#sections-and-apps)
    *  [Dnd_events](#dnd-events)
    *  [Replies](#replies)
    *  [Posts](#posts)
    *  [Initiative](#initiative)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)


## Sections and Apps

### Custom Sections

### **Dnd Events** 
* This app for events, was created to link up with my fornt end app, and collect, store and return to origin the data that's created about making DND Events.
* This meant I created the ability to know when a user is logged in, order posts due to there created at ID's, and included dates, times, and descriptions (text box input fields) of what was going on in this event.

### **Replies**

* Coinciding DND Events is my replies app, to allow users to state their interest in a particular game/ event. Which in turn will hopefully rally more support and people!

### **Posts**

* This based upon the Code Institute modle walkthrough, is to allow logged in users to post their every thought or comment on others posts. Here is where people can state there love or hate (or out right appathy) for anything dnd.
* Logged in users are able to connect to this API, to use CRUD functionality. Allowing our users a seemless transition of data form Front to Back end. Giving them full control over Creating/Reading/Updating/Deleting there own content.

### **Initiative**

* Building this allowed me to make a small dream of mine to have a DND initiative counter that keeps track of your players and monsters, using fields of name and iniative for only values.


[Back to top](#20-sided-queer)

## Testing

  ### All notes related to testing are found [here](documentation/testing.md).

[Back to top](#20-sided-queer)

## Deployment

* Go to the Heroku Dashboard. Create new apllication
* In the 'Settings' tab of your app select 'Reveal Config Vars'.
* Add releveant Build Packs for this project e.g. Python
* Make sure Postgres Database is attached.
* Create/ Add 'SECRET_KEY' connecting to your django environment.
* Create/ Add 'DATABASE_URL' connecting to your postgreSQL database.
* Create/ Add 'ClOUDINARY_URL' connecting to cloudinary's cloud hosting service for media.
* Remember to attach the relevant key and value pairs for linking to the new Front End. with Client Origin Dev
* *Remember to change DEBUG to False in settings.py when ready to deploy live versions.*
* Move to deployment tab above.
* Link repository from GitHub to Heroku.
* Go to deploy page, select auto deployment.
* Note: Deploy Main Branch, choosing either from "Automatic Deploys" or "Deploy Branch".
* Wait until launching is complete.
* Click Open App.


## Credits

Through-out this project I was inspired and helped by a number of sources, in order to make custom code:
1) For use of learning how to test more efficently and re understanging how to unpack dictionaries. I found this very helpful [here](https://pythonhow.com/what/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters/)
2) The tutors at Code Institute for giving me a lot of understanding with how to debug my code!And reminding me to switch my states for deployment!
3) The Code Institue Walkthrough for Moments, helped to shape and template my own code as I found this task hard to start from a blank slate.


* I'd also like to credit thanks to all the tutors that helped guide me through-out at Code Institue.

[Back to top](#20-sided-queer)