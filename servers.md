# Servers

Servers in the `pm2` `ecosystem.config.js` file

<!-- express frontend server -->
<<<<<<< HEAD
express-frontend  

<!-- express api server  -->
express-api       
=======
jda-frontend  

<!-- express api server  -->
jda-api       
>>>>>>> 93dc399 (Configure server script and add pm2 for server mgmt)

<!--  script does not exist -->
python-server     

# Launching

```sh
    pm2 start ecosystem.config.js --only "jda-api,jda-frontend"
```
