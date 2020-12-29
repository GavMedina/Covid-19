
pipeline {
    // available agent
    agent any
    parameters {
        string(name: 'country', description: 'Highest peak of new Covid19 in the last 30 days')
        string(name: 'recoveredPeak', description: 'Highest peak of recovered Covid19 in the last 30 days')
        string(name: 'deathsPeak', description: 'Highest peak of deaths Covid19 in the last 30 days')
        string(name: 'status', description: 'Check if we can contact with backend API')
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
                sh "curl localhost:5555/deathsPeak?country=${params.deathsPeak}"
		sh "sleep 1"
                sh "curl localhost:5555/newCasesPeak?country=${params.country}"
		sh "sleep 1"
		sh "curl localhost:5555/recoveredPeak?country=${params.recoveredPeak}"
		sh "sleep 1"
		sh "curl localhost:5555/${params.status}"
                
            }
        }
    }
}
