module.exports = {
    apps: [
        {
            name: 'jda-frontend',
            script: 'JDA-12/v1/bin/www',
            instances: '1',
            watch: false,
            env: {
                NODE_ENV: 'development',
                ID: 44
            },
            env_production: {
                NODE_ENV: 'production',
                ID: 83
            },
            max_memory_restart: "90M"
        },
        {
            name: 'jda-api',
            script: 'APIs/exp-API/bin/www',
            instances: '1',
            watch: false,
            env: {
                NODE_ENV: 'development',
                ID: 45
            },
            env_production: {
                NODE_ENV: 'production',
                ID: 84
            },
            max_memory_restart: "90M"
        },
        {
            name: 'python-server',
            script: 'APIs/py-API/run_script.sh',
            instances: '1',
            watch: false,
            env: {
                NODE_ENV: 'development',
                ID: 46
            },
            env_production: {
                NODE_ENV: 'production',
                ID: 85
            },
            max_memory_restart: "90M"
        }
    ],

    deploy : {
        production: {
            user: 'SSH_USERNAME',
            host: 'SSH_HOSTMACHINE',
            ref: 'render/dev',
            repo: 'git@github.com:Stack-Breakthrough/jobs-data-analyzer.git',
            path: 'DESTINATION_PATH',
            'pre-deploy-local' : '',
            'post-deploy' : 'npm install && pm2 reload ecosystem.config.js --env production'
        }
    }
};
