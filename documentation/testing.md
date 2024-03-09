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
### Comments Linter Testing 
<details>
<summary>Comments Model </summary>

![Comments1](/documentation/image_tests/CommentModelLinter.png)
</details>
<details>
<summary>Comments Serializer </summary>

![Comments2](/documentation/image_tests/CommentSerializer.png)
</details>
<details>
<summary>Comments Url </summary>

![Comments3](/documentation/image_tests/CommentUrlLinter.png)
</details>
<details>
<summary>Comments Views </summary>

![Comments4](/documentation/image_tests/CommentViewsLinter.png)
</details>

### Posts Linter Testing 
<details>
<summary>Posts Model </summary>

![Post1](/documentation/image_tests/POstModelLinter.png)
</details>
<details>
<summary>Post Serializer </summary>

![Post2](/documentation/image_tests/PostSerializerLinter.png)
</details>
<details>
<summary>Post Url </summary>

![Post3](/documentation/image_tests/PostUrlsLinter.png)
</details>
<details>
<summary>Post Views </summary>

![Post4](/documentation/image_tests/POstViewsLinter.png)
</details>

### Dnd Events Linter Testing 
<details>
<summary>Dnd Events Model </summary>

![DNDEVENT1](/documentation/image_tests/DNDModelLinter.png)
</details>
<details>
<summary>DND Serializer </summary>

![DnDEVENT2](/documentation/image_tests/DNDSerlializerLinter.png)
</details>
<details>

<summary>DND Url </summary>

![DnDEVENT3](/documentation/image_tests/DNDUrlsLinter.png)
</details>
<details>
<summary>DND Views </summary>

![DnDEVENT4](/documentation/image_tests/DNDViewsLinter.png)
</details>
<details>
<summary>DND Test</summary>

![DnDEVENT5](/documentation/image_tests/DNDtestsLinter.png)
</details>

### Replies Linter Testing 

<details>
<summary>Replies Model </summary>

![Replies1](/documentation/image_tests/RepliesModelLinter.png)
</details>
<details>
<summary> Replies Serializer </summary>

![Replies2](/documentation/image_tests/RepliesSerializerLinter.png)
</details>
<details>

<summary>Replies Url </summary>

![Replies2](/documentation/image_tests/RepliesUrlLinter.png)
</details>
<details>
<summary>Replies Views </summary>

![Replies3](/documentation/image_tests/RepliesViewsLimter.png)
</details>

### Initiative Linter Testing 

<details>
<summary>Initiative Model </summary>

![Initiative1](/documentation/image_tests/InitiativeModelLinter.png)
</details>
<details>
<summary> Initiative Serializer </summary>

![Initiative2](/documentation/image_tests/InitiativeSerlizaeLinter.png)
</details>
<details>

<summary>Initiative Url </summary>

![Initiative3](/documentation/image_tests/IniativeUrlLinter.png)
</details>
<details>
<summary>Initiative Views </summary>

![Initiative4](/documentation/image_tests/IniativeViewsLinter.png)
</details>
<details>
<summary>Initiative Test</summary>

![Initiative5](/documentation/image_tests/InitiativesTestLinter.png)
</details>


### Likes Linter Testing 

<details>
<summary>Likes Model </summary>

![Likes1](/documentation/image_tests/LikesModelLinter.png)
</details>
<details>
<summary> Likes Serializer </summary>

![Likes2](/documentation/image_tests/LikesSerializerlinter.png)
</details>
<details>

<summary>Likes Url </summary>

![Likes2](/documentation/image_tests/LikesUrlsLinter.png)
</details>
<details>
<summary>Likes Views </summary>

![Likes3](/documentation/image_tests/LikesViewsLinter.png)
</details>

### Followers Linter Testing 

<details>
<summary>Followers Model </summary>

![Followers1](/documentation/image_tests/FollowerModelLinter.png)
</details>
<details>
<summary> Followers Serializer </summary>

![Followers2](/documentation/image_tests/FollowerSerializerLinter.png)
</details>
<details>

<summary>Followers Url </summary>

![Followers3](/documentation/image_tests/FollowersUrlsLinter.png)
</details>
<details>
<summary>Followers Views </summary>

![Followers4](/documentation/image_tests/FollowersViewsLinter.png)
</details>

### Profiles Linter Testing 

<details>
<summary>Profile Model </summary>

![Profiles1](/documentation/image_tests/ProfileLintermodel.png)
</details>
<details>
<summary> Profile Serializer </summary>

![Profiles2](/documentation/image_tests/ProfileSerialzersLinter.png)
</details>
<details>

<summary>Profile Url </summary>

![Profiles3](/documentation/image_tests/ProfielsUrlsLinter.png)
</details>
<details>
<summary>Profile Views </summary>

![Profiles4](/documentation/image_tests/ProfielsViewsLinter.png)
</details>

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
| ----------- | ----------- | ----- |
| Can create new instance of Name and Value  | Shows on Initiavies List  | Pass
| /initiatives/id can be found|  shows relevant Counter for ID | Pass
| Can be deleted| Removes from list| Pass

| Test Description (DND Events)   | Expected Outcome | Actual Outcome |
| ----------- | ----------- | ----- |
| Can create new dnd event  | Shows on DND Event List  | Pass
| /dnd_event/id can be found|  shows relevant fields filled in with recent values for ID | Pass
| Can be deleted| Removes from list| Pass

| Test Description (Replies)   | Expected Outcome | Actual Outcome |
| ----------- | ----------- | ----- |
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

[Back to README](/README.md)