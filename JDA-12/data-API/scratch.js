class Job
{
	title = 'Software engineer';
	openings = 
	{
		'ytd': Math.round( Math.randon() * 60000 ),
		'last_six_months': {

		}
	};
	seniority = 'junior'; 	// varchar
	skills = ['agile'];		// varchar
	avg_yrs_exp = 3;		// int
	number_applicants = 39055;
	country = 'USA';
	remote = true;
	companies = 43;
	salary_range = '40,000 - 50,000';
	shift = 8;
	qualifications = { 'REST':1, 'Java':1 }
}

// later on to find out what two jobs have in common
// compare two software-related jobs
input_field [ 'software engineer' ] vs input_field [ 'dev-ops engineer' ]
/*
	output:
		intersection
			skills
			seniority
			remote
*/



