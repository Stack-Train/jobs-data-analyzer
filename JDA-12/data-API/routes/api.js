var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next)
{
    res.render('api', { title: 'Jobs Data API.' });
});

const YEAR = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept','Oct', 'Nov', 'Dec'];

var last_six_months = function()
{
    var months = [ ];
    var date = new Date();

    var curr_month = date.getMonth();
    var prev_month = curr_month;
    var curr_year = date.getFullYear();

    for( var i = 0; i < YEAR.length/2; i++ )
    {
        prev_month -= i ;
        prev_month = ( YEAR.length + prev_month ) % YEAR.length;
        months.push({
            'month': YEAR[ prev_month ],
            'year': ( prev_month < 0 ) ? (  curr_year - 1 ) : curr_year
        });
    }
    return months;
}

/* GET users listing. */
router.get(['/data','/jobs'], function(req, res, next) 
{
    var months = last_six_months();
    var  sample_months = [ 'Jan', 'Dec', 'Nov', 'Oct', 'Sept', 'Aug' ];
    sample_months.reverse();
    const MAX = 40;

    var job_queries = [ 'Software Engineer', 'Support Engineer', 'Dev-Ops'];

    var sample_data = [
        {
            series: [
            {
                name: 'Seniority',
                type: 'pie',
                data: [
                {
                    value: Math.round(Math.random()*385),
                    name: 'Entry level'
                },
                {
                    value: Math.round(Math.random()*234),
                    name: 'Senior'
                },
                {
                    value: Math.round(Math.random()*1548),
                    name: 'Junior'
                }]
            }
            ]
        },
        {
            // Global color palette
            color: [
                '#c23531', '#2f4554', '#61a0a8', '#d48265', '#91c7ae',
                '#749f83', '#ca8622', '#bda29a', '#6e7074', '#546570',
                '#c4ccd3'
              ],
            title:{ text: job_queries[0] + ' demand.' },
            tooltip: { },
            legend: { data: ['Applications'] },
            xAxis: { data: sample_months },
            yAxis: { },
            series: [
                {
                    name: 'Applications',
                    type: 'bar',
                    data: [ 
                        Math.round(Math.random()*MAX),
                        Math.round(Math.random()*MAX),
                        Math.round(Math.random()*MAX),
                        Math.round(Math.random()*MAX),
                        Math.round(Math.random()*MAX),
                        Math.round(Math.random()*MAX) 
                    ]
                }
            ]
        },
        {
            series: [
            {
                name: 'Experience',
                type: 'pie',
                data: [
                {
                    value: Math.round(Math.random()*100),
                    name: '5 years'
                },
                {
                    value: Math.round(Math.random()*200),
                    name: '4 years'
                },
                {
                    value: Math.round(Math.random()*300),
                    name: '3 years'
                },
                {
                    value: Math.round(Math.random()*400),
                    name: '2 years'
                },
                {
                    value: Math.round(Math.random()*500),
                    name: '1 year'
                }
                ],
                roseType: 'area'
            }
            ]
        },
        {

            title:{ text: job_queries[1] + ' demand.' },
            tooltip: { },
            legend: { data: ['Applications'] },
            xAxis: { data: sample_months },
            yAxis: { },
            series: [
                {
                    name: 'Applications',
                    type: 'bar',
                    data: [ 
                        Math.round(Math.random()*MAX),
                        Math.round(Math.random()*MAX),
                        Math.round(Math.random()*MAX),
                        Math.round(Math.random()*MAX),
                        Math.round(Math.random()*MAX),
                        Math.round(Math.random()*MAX) 
                    ]
                }
            ]
        }
    ];
    
    res.setHeader('Content-Type','application/json');
    res.send( sample_data );
});

module.exports = router;
