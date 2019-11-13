# theScore "the Rush" Interview Question
At theScore, we are always looking for intelligent, resourceful, full-stack developers to join our growing team. To help us evaluate new talent, we have created this take-home interview question. This question should take you no more than a few hours.

**All candidates must complete this before the possibility of an in-person interview. During the in-person interview, your submitted project will be used as the base for further extensions.**

### Why a take-home interview?
In-person coding interviews can be stressful and can hide some people's full potential. A take-home gives you a chance work in a less stressful environment and showcase your talent.

We want you to be at your best and most comfortable.

### A bit about our tech stack
As outlined in our job description, you will come across technologies which include a server-side web framework (either Ruby on Rails or a modern Javascript framework) and a front-end Javascript framework (like ReactJS)

### Understanding the problem
In this repo is the file [`rushing.json`](/rushing.json). It contains data about NFL players' rushing statistics. Each entry contains the following information
* `Player` (Player's name)
* `Team` (Player's team abreviation)
* `Pos` (Player's postion)
* `Att/G` (Rushing Attempts Per Game Average)
* `Att` (Rushing Attempts)
* `Yrds` (Total Rushing Yards)
* `Avg` (Rushing Average Yards Per Attempt)
* `Yds/G` (Rushing Yards Per Game)
* `TD` (Total Rushing Touchdowns)
* `Lng` (Longest Rush -- a `T` represents a touchdown occurred)
* `1st` (Rushing First Downs)
* `1st%` (Rushing First Down Percentage)
* `20+` (Rushing 20+ Yards Each)
* `40+` (Rushing 40+ Yards Each)
* `FUM` (Rushing Fumbles)

##### Requirements
1. Create a web app. This must be able to do the following steps
    1. Create a webpage which displays a table with the contents of `rushing.json`
    2. The user should be able to sort the players by _Total Rushing Yards_, _Longest Rush_ and _Total Rushing Touchdowns_
    3. The user should be able to filter by the player's name
    4. The user should be able to download the sorted/filtered data as a CSV

2. Update the section `Installation and running this solution` in the README file explaining how to run your code

### Submitting a solution
1. Download this repo
2. Complete the problem outlined in the `Requirements` section
3. In your personal public GitHub repo, create a new public repo with this implementation
4. Provide this link to your contact at theScore

We will evaluate you on your ability to solve the problem defined in the requirements section as well as your choice of frameworks, and general coding style.

### Help
If you have any questions regarding requirements, do not hesitate to email your contact at theScore for clarification.

### Installation and running this solution

#### Installing
Python 3 is required.  This comes pre installed on most modern linux distros.  Windows or Mac users may need to install it manually from https://www.python.org/downloads/.  If you have Python installed but aren't sure of the version check by running `python --version`.

This app isn't tested with Python 2.  The app should be cross platform but has only been tested on Windows.

Install Python dependencies by running this from the root project folder:
`pip install -r requirements.txt`

#### Running
From the command line simply run:
`python bin/down_set_hut.py`

then visit http://localhost:8888/rushing and test out the various features!


### ToDo List
Here's a list of ToDo items which would complete this project by making a more cohesive user experience, help productionize this app, and so forth.

* On page load set radio button according to sort settting.  This would aid UI experience under the principle visibility of system status.
* Port hardcoded variables to config file.

### Framework Selection and Design Considerations
Most of my experience writing production applications is in Python so that's the language used here.  I then selected Tornado as the web app Framework.

Since I'm a backend developer the front end is rather rudimentary.  However, bootstrap is used to keep the app easy on the eyes.  It's alsoloaded from a CDN providing some scalability out of the box.  But no frameworks or even JS is used; it's otherwise raw HTML but it's enough to get the job done.


The backend has more shiney features.

One easy trap to fall into is modifying state on each request.  Such errors may not show up when testing with a single client but can produce strange behaviour like missing data when testing with multiple users.  Still I will acknowledge this is reliant on bug-free programming and there's nothing stopping an accidental state modification from occuring with even a small code change.

### Feature Design Rationale
I decided to implement the NFL Rushings app as a single page.  This keeps things simple and cohesive, as well allows the features to work complementary to one another rather than on their own.  This is especially powerful for the CSV export, allowing users to easily export the exact data they're looking at.

All features are implemented server-side, however the CSV export and possibly filtering might better be implemented client-side.  They would certainly help the app scale by taking computational demand away from the server.
