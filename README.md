## Set a path for the global exclude file
git config --global core.excludesfile ~/.gitignore

## add patterns or files to ignore 
.gitignore
### Add file names in .gitignore file, e.g.,:
### .env

## Stage and commit the .gitignore file
git add .gitignore
git commit -m "Add .gitignore file"


## Stop tracking the file (removes from repository index, keeps on disk)
## If you starting tracking a file that was not added in .gitignore, you can remove it first before commiting other changes
git rm --cached <filename>

## Commit the untracking change
git commit -m "Untrack <filename> and ignore"


# Clean Up

## 1. Remove all files from the index (keeps them on disk)
git rm -r --cached .

## 2. Re-add all files. Git will automatically ignore files listed in .gitignore
git add .

## 3. Commit the cleanup
git commit -m "Cleaned up tracked files according to .gitignore"