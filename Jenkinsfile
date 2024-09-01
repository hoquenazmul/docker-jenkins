pipeline {
    agent {
        node { label 'PYTHON_DOCKER_AGENT' }
    }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Installing app dependencies..."
                sh '''
                cd demo-app
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Running app..."
                sh '''
                cd demo-app
                python3 app.py
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying app...'
                sh '''
                echo "deployment completed..."
                '''
            }
        }
    }
}