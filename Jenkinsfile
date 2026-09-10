pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Stage 1: Cloning and checking out repository source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Stage 2: Verifying Python installation and executing program...'
                sh 'python3 --version'
                sh 'python3 app.py 12.5 7.5'
            }
        }
    }
}