var express = require('express');
var router = express.Router();
var project = require('../config/project');
var title = 'Jobs Data API';

/* GET home page. */
router.get(['/','/home'], function(req, res, next) 
{
  res.render('index', { title: project.name  || title });
});

router.get('/about', (req, res, next)=>
{
  res.render('about', { title: project.name || title });
})

module.exports = router;
