pipeline {
    // available agent
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		sh 'pip install -r requirements.txt
		python main.py
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
