# Giting it. Start here.

# [We've got Issues! 📋](https://solvestack.atlassian.net/jira/software/projects/JDA/boards/1)

There are basically three categories of `issues`;

1. `Feature`: May require the creation of a branch, especially if issue title is too broad. e.g. `Create visualization site.`
2. `Major`: An issue that affects many parts of the `project` and needs to be fixed ASAP. Could be a `bug` / tool issue.
3. `Minor`: There's no need to panic about this issue.

# Working with issue-based branches 🎋

Lets say you want to work on a `feature` issue for example; **`JDA-12`: Build working visualization site**

## 1. Create a branch of our main repo

Create a branch of`jobs-data-analyzer` via a `JIRA` issue panel see image below;

<img width="854" alt="Create a new branch via JIRA" src="https://user-images.githubusercontent.com/9142438/210124742-de51ce8a-e32c-46b2-b412-33de7cc2abb2.png">

## 2. Go to the repo on `Github`

Go to the `jobs-data-analyzer` repo on `GitHub` and make sure the `branch` you created exists on `Github`;

<img width="839" alt="Select the newly created branch" src="https://user-images.githubusercontent.com/9142438/210124855-efef1136-7ca4-4807-9176-b0067b1cfd4f.png">

## 3. Clone the branch 

Choose `HTTPS`, `SSH`, copy the link and clone the `branch`;

<img width="567" alt="clone issue branch" src="https://user-images.githubusercontent.com/9142438/210125001-f41280fd-c6c6-4fb7-9c91-5eece5f88109.png">

Clone the branch: `git clone -b JDA-12 git@github.com:StackBreakthrough/jobs-data-analyzer.git`

`cd` into the folder and work on your branch

<img width="636" alt="Work on it" src="https://user-images.githubusercontent.com/9142438/210125476-ef73526d-e7cf-4951-888a-2a49e8f75f0b.png">

# Shortcut 

You could also could've simply created the branch from `main` via your command line ( assuming you initially cloned the main branch ); 

`git checkout -b JDA-12` 

and switched to it for the following steps. ¯\_(ツ)_/¯

## Step 1

Add and commit your changes to your branch `JDA-12` in this case.

<img width="636" alt="Add and commit changes" src="https://user-images.githubusercontent.com/9142438/210125763-85073d43-38f0-4305-9c47-2ee544f321d6.png">

## Step 2

Then `checkout` the `main` `branch` and merge it with your `branch`, `JDA-12` in this case;

<img width="636" alt="Checkout and merge" src="https://user-images.githubusercontent.com/9142438/210125855-756c3245-97e4-447f-8cc9-40421724c677.png">

## Step 3 

You have a number of options;

1. `git push origin main` or `switch` back to your branch (`JDA-12`) and add more stuff, or push what you already have in that branch to its remote; 
3. `git switch JDA-12` 
4. `git push origin JDA-12`

# Another way to merge your changes with the main branch

If this seems like a long process then you might consider just pushing your changes to your remote branch and using Github's pull request to merge it with the `main` branch.

