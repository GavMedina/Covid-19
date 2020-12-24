pipeline {
    // available agent
    agent {
        docker { image 'docker run -p 5555:80 yyyaner/python:v1' }
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		        sh 'python3.7.5 main.py'
            }
        }
    }
}
