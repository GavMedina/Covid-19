pipeline {
    // available agent
    agent any
    parameters {string(name: 'country')}
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		        sh 'apt -y install python3-pip'
		        sh 'pip3 install -r requirements.txt'
		        
            }
        }
        stage('Test') {
            steps {
                echo 'testing'
                sh 'python3.6 main.py &'
                sh 'sleep 1'
                sh 'curl -s localhost:5555/newCasesPeak?country=${params.country}'
            }
        }
    }
}

