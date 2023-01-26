# How to work from a branch
Clone the repository you want to download the code for (in this example I've picked the LRResty project on Github):

$ git clone https://github.com/gitusername/reponame.git
$ cd reponame
--------------
Check what branch you are using at this point (it should be the master branch):

$ git branch    
* master
--------------
Check out the branch you want, in my case it is called 'your_branch_name':

 $ git checkout -b your_branch_name origin/your_branch_name
 Branch your_branch_name set up to track remote branch your_branch_name from origin.
 Switched to a new branch 'your_branch_name'
---------------
Confirm you are now using the branch you wanted:

$ git branch    
* your_branch_name
  master

-----------------------
If you want to update the code again later, run git pull:

$ git pull
Already up-to-date.
