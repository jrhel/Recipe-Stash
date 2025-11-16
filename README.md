# Recipe Stash

Recipe Stash is a service for storing and creating all of your recipies in one place. 

## Functinality to be implemented:
- User can create an account and log in;
- User can create and save recipies;
- User has a userpage where their created recipies show up;
- User can open & view a saved recipie;
- User can edit & delete their saved recipies;
- User can search for recipies by name;
- Users may add recipies, created by other users, to their own page for future reference;
- Users can tag recipies, that they have added or created;
- A users own tags show in a recipe;
- The most prominent tags by users show in a recipie;
- User can search for recipies by a tag/categpry;
- Users may add a score, (e.g. n stars out of five), to any recipie, and view these from their own page;
- The avergage of user scores show up in search results next to recipies;

## Functinality that may be implemented:
- User can search for recipies by a set of ingredients;
- Users can comment on recipies

## Installation instructions:
1) In your terminal, navigate to the directory in which you want to install the application and download it, with the command:
```
git clone https://github.com/jrhel/Recipe-Stash.git
```
2) Set up a virtual environment for the application, with the command:
```
python3 -m venv venv
```
3) Activate the virtual environment:
 - a) on Unix, with the command;
   ```
   venv/bin/activate
   ```
 - b) on Windows, with the command;
   ```
   venv\Scripts\activate
   ```
4) Install flask, with the command:
   ```
   pip install flask
   ```
5) Launch the application, with the command:
```
flask run
```
6) The user interface for the application may now be opened, in your browser, with the address specified in your terminal.

## Shutting down the application
1) In your terminal, shut down the application by pressing ctrl + c.
2) Deactivate the virtual environment, with the command:
```
deactivate
```

## Restarting the application
1) In your terminal, navigate to the directory where the virtual environment was set up and activate it:
 - a) on Unix, with the command;
   ```
   venv/bin/activate
   ```
 - b) on Windows, with the command;
   ```
   venv\Scripts\activate
   ```
2) Launch the application, with the command:
```
flask run
```
3) The user interface for the application may now be opened, in your browser, with the address specified in your terminal.
