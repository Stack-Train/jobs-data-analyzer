# Servers

Servers in the `pm2` `ecosystem.config.js` file

<!-- express frontend server -->
express-frontend  

<!-- express api server  -->
express-api       

<!--  script does not exist -->
python-server     

# Launching

```sh
    pm2 start ecosystem.config.js --only "jda-api,jda-frontend"
```
