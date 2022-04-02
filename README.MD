### WINC BACK-END FINAL EXERCISE ###

### Problems I encountered ###
At the very start of this final exercise I had troubles creating an account at digital ocean because of non-code issues (no credit card / paypal account).
When I found a solution this issue the second thing I walked into was getting the flask application running on the server. It kept giving me error messages and after 
finding out I tried to execute commands in the wrong directory I passed that issue.

I also had some troubles working with Github. for example I did not really know where to add an action ( It was not toroughly explained where to put the action files) but in the end
I found out how to do this by creating some actions using Github Desktop. 

When I eventually finished this project, I had trouble starting the server again (I still don't know what caused this issue but I could not login to my VPS through the SSH). In the end I got it all to work proper.
### What did I do to get my project to run?###
I created a droplet running on Ubuntu which I connect to using my local machine through SSH. With some commands I installed GUNICORN, Python, and flask on the VPS. 
I deployed the Flask server and everytime I push new code, a github action runs pytest (test_main) to check.