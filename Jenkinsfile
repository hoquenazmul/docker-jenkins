pipeline {
    agent {
        node { label 'TEST_AGENT_DOCKER' }
    }

    // triggers {
    //     pollSCM '* * * * *'
    // }

    environment {
        APP_VERSION = '3.2.5'
    }

    parameters {
        string(name: 'NODE', description: 'Node Agent', defaultValue: 'TEST_AGENT_DOCKER')
        choice(name: 'ENVIRONMENT', description: 'Application Enviroment', choices: ['dev', 'qa', 'uat', 'prod'])
        booleanParam(name: 'TEST_EXECUTION', description: 'Execute Tests', defaultValue: true)
    }

    stages {
        stage('Build') {
            steps {
                echo "bulding app with build id ${BUILD_ID}"
                script {
                    cd demo-app
                    pip install -r requirements.txt
                }
            }
        }

        stage('Test') {
            when {
                expression {
                    params.TEST_EXECUTION
                }
            }
            steps {
                echo "testing app version# ${APP_VERSION}"
                sh '''
                cd demo-app
                python3 app.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'deploying app in ${params.ENVIRONMENT}'
                sh '''
                echo "deployment completed..."
                '''
            }
        }
    }
}