#Instructions to work from a branch
Clone the repository you want to download the code for (in this example I've picked the LRResty project on Github):

$ git clone https://github.com/lukeredpath/LRResty.git
$ cd LRResty
--------------
Check what branch you are using at this point (it should be the master branch):

$ git branch    
* master
--------------
Check out the branch you want, in my case it is called 'arcified':

 $ git checkout -b arcified origin/arcified
 Branch arcified set up to track remote branch arcified from origin.
 Switched to a new branch 'arcified'
---------------
Confirm you are now using the branch you wanted:

$ git branch    
* arcified
  master

-----------------------
If you want to update the code again later, run git pull:

$ git pull
Already up-to-date.
