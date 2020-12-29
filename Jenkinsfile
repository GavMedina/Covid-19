
pipeline {
    // available agent
    agent any
    parameters {
        string(name: 'country', description: 'Highest peak of new Covid19 in the last 30 days')
        string(name: 'recoveredPeak', description: 'Highest peak of recovered Covid19 in the last 30 days')
        string(name: 'deathsPeak', description: 'Highest peak of deaths Covid19 in the last 30 days')
    }
    stages {
        stage("Build") {
            steps {
                echo "Building.."
		        sh "apt -y install python3-pip"
	            sh "pip3 install -r requirements.txt"
	            sh "python3.6 main.py &"
		        
            }
        }
        stage("deathPeak") {
            steps {
                sh "curl localhost:5555/deathsPeak?country=${params.deathsPeak}"
            }
        }
        stage("newCasesPeak") {
            steps {
                sh "curl localhost:5555/newCasesPeak?country=${params.country}"
            }
        }
        stage("recoveredPeak") {
            steps {
                sh "curl localhost:5555/recoveredPeak?country=${params.recoveredPeak}"
            }
        }
        stage("Status") {
            steps {
                sh "curl localhost:5555/status"
            }
        }
    }
}
