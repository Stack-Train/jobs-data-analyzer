var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
    var data = ['shirt','cardigan','chiffon','pants','heels','socks'];
    res.send( data );
});

module.exports = router;
