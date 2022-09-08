#####-- These are the commands for Git and Github --#####

git log
git config --global user.name Shivam Bhosle - UserName
git config --global user.email - Email log
git config --global user.username
git init -- creates a new Git repository
git status
git add
git add. - to add multiple files at a times
git add -A  -- to add all the files in the directory
git commit - m "msg" - commit is mandatory before pushing 
git remote add origin <link-SSH>
git remote -v = shows address of where is pushing and fetching
git push 
git push origin --delete <branch name at github>  -- deletes the branch from github
git push --set-upstream origin <branch name at local> -- to push the current branch and set the remote as upstream
git pull
git pull origin <name of main branch at hub> -- to pull the data from main branch on hub
git pull origin <name of main branch at hub> --allow-unrelated-histories -- to download all the files on remote to the local by irgnoring merging conflicts
git touch - to make new empty files
touch <filename.txt> = create new file
start <filename.txt> = open that file
git clone = 
git branch -- to check in which branch you are working
git checkout -- lets you navigate between the branches created by git branch
git merge <branch name>
git branch -d <branch name> = to delete the branch
git branch -m <old branch name> <new branch name>
git push origin --delete <branch name> = will delete branch from git hub
git rm <filename/folder name> = to delete perticular folder or file



====== Connecting Existing Local Directory to repository on github =======

# Initialize the local directory as a Git repository.
git init

# Add files
git add .

# Commit your changes
git commit -m "First commit"

# Add remote origin
git remote add origin <Remote repository URL>
# <Remote repository URL> looks like: https://github.com/user/repo.git

# Verifies the new remote URL
git remote -v

# Push your changes
git push origin master
