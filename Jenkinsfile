pipeline {
    // available agent
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		        sh 'apt install python3-pip'
		        sh 'pip3 install -r requirements.txt'
		        sh 'python3 main.py'
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

