# Testing

## Index

 * [Error resolution and Debugging](#error-resolution-and-debugging)
 * [Validation](#validation)
 * [Manual testing](#manual-testing)
 * [Coverage Testing](#coverage-testing)
 * [Automated Testing](#automated-tests)


 ## Error resolution and Debugging
 * I had a couple of issues with getting my urls to be set up, I had mutliple spelling errors from my end that meant I had to reset my debug settings to figure out my own errors.


## Validation



## Manual testing 


| Test Description (API)   | Expected Outcome | Actual Outcome |
| ----------- | ----------- | ----- |
| Start Load Page   | Welcome message to API  | Pass
| /posts | Should be able to see Post List | Pass
| /followers | Should see Followers List| Pass
| /likes| Should see Likes list | Pass
| /profiles| Should see Profiles list | Pass
| /comments| Should see Comments Events list | Pass
| /dnd_events| Should see DND Events list | Pass
| /initiatives| Should see Initiative list | Pass
| ----------- | ----------- | ----- |
| /initiatives/id| Should see Initiative Detail | Pass
| /profiles/id| Should see Profiles Detail | Pass
| /posts/id| Should see Posts Detail | Pass
| /likes/id| Should see Likes Detail | Pass
| /commentsid| Should see Comments Detail | Pass
| /dnd_events/id| Should see DND Event Detail | Pass

### Tests on Custom Apps
| Test Description (Initiatives)   | Expected Outcome | Actual Outcome |
| Can create new instance of Name and Value  | Shows on Initiavies List  | Pass
| /initiatives/id can be found|  shows relevant Counter for ID | Pass
| Can be deleted| Removes from list| Pass

| Test Description (DND Events)   | Expected Outcome | Actual Outcome |
| Can create new dnd event  | Shows on DND Event List  | Pass
| /dnd_event/id can be found|  shows relevant fields filled in with recent values for ID | Pass
| Can be deleted| Removes from list| Pass

| Test Description (Replies)   | Expected Outcome | Actual Outcome |
| Can create new reply instance  | Shows on Replies List  | Pass
| /replies/id can be found|  shows reply on which post | Pass
| Can be deleted| Removes from list| Pass


## Coverage Testing 

* I followed the following steps to generate a coverage report - result of 88% coverage.
1) pip install coverage
2) coverage run manage.py test
3) coverage report

![Coverage1](/documentation/image_tests/Coverage1.png)
![Coverage2](/documentation/image_tests/Coverage2.png)
![Coverage3](/documentation/image_tests/Coverage3.png)


## Automated tests
A couple of automated tests have been made for this API project, for future projects I would like to create multiple tests for every single app. the ones I made are based in DnD_events test and Initiative test.  
### Find them [here](../dnd_events/tests.py) and [here](../initiative/tests.py)

