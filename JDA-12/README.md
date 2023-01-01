# JDA-12: Visualization Site 📈

&nbsp;&nbsp;&nbsp;&nbsp; Everything related to visualization. <br />

&nbsp;&nbsp;&nbsp;&nbsp; [References issue JDA-12](https://solvestack.atlassian.net/browse/JDA-12?atlOrigin=eyJpIjoiZjMzZjNkNjBjMTIxNDYyNGJmZWJiZDc0MmU2YzY4OTciLCJwIjoiaiJ9)

## Tableau WebApp with Flask backend

A flask back-end and authentication, with login and a Tableau dashboard management.

## Usage

Launch the `main.py` script. It will start a `web server` on `localhost:5000`. <br />
There's need to be a `Tableau server running on 10.0.55.1` ( otherwise you'll have to change the address in the files )

```
Login example:
username:   user1
password:   yourpassword
```
### Login form example
![alt text](login_form.PNG)

### Dashboard page example
![alt text](dashboard.PNG)

### Built with

- `Flask`
- `Tableau` ( `Rest API` and `JS API` )
- `HTML / CSS / JS`
