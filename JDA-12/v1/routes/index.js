var express = require('express');
var router = express.Router();
var site = require("../config/site");

/* GET home page. */
router.get(['/','/index','/home'], function(req, res, next)
{
    title = req.app.locals.title;
    res.render('index', { title: title });
});

module.exports = router;
