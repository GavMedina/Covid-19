
pipeline {
    // available agent
    agent any
    parameters {
        string(name: 'country', description: 'newCasesPeak'))
        string(name: 'recoveredPeak', description: 'recoveredPeak')
        string(name: 'deathsPeak', description: 'deathsPeak')
        string(name: 'status', description: 'status')
    }
    stages {
        stage("Build") {
            steps {
                echo "Building.."
		sh "apt -y install python3-pip"
	        sh "pip3 install -r requirements.txt"
		        
            }
        }
        stage("Test") {
            steps {
                echo "testing"
                sh "python3.6 main.py &"
                sh "sleep 1"
                sh "if [ -z ${params.deathsPeak} ]; then curl localhost:5555/deathsPeak?country=${params.deathsPeak}; fi"
                sh "curl localhost:5555/newCasesPeak?country=${params.country}"
                
            }
        }
    }
}
