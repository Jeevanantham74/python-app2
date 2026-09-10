pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Jeevanantham74/python-app2.git'
            }
        }

        stage('Build') {
            steps {
                bat 'py --version'
                bat 'py app.py 10 20'
            }
        }

    }
}