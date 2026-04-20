var createError = require('http-errors');
var express = require('express');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

app.get('/api/data', function(req, res) {
  res.json({
    demand: [
      { role: 'Software Engineer', openings: 48200 },
      { role: 'DevOps Engineer', openings: 21500 },
      { role: 'Data Scientist', openings: 18700 },
      { role: 'Product Manager', openings: 15300 }
    ]
  });
});

app.get('/api/jobs', function(req, res) {
  res.json({
    seniority: { junior: 42, mid: 35, senior: 23 },
    experience: { '0-2': 38, '3-5': 34, '6+': 28 },
    remote: { remote: 61, hybrid: 25, onsite: 14 }
  });
});

app.use(function(req, res, next) {
  next(createError(404));
});

app.use(function(err, req, res, next) {
  res.status(err.status || 500).json({ error: err.message });
});

module.exports = app;
