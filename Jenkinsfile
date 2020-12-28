pipeline {
    // available agent
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		        sh 'apt -y install python3-pip'
		        sh 'pip3 install -r requirements.txt'
		        sh 'python3.6 main.py'
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


