pipeline{
  agent any
  stages{
    stage('checkout'){
	steps{
	 git branch: 'release', credentialsId: 'd1a8d5f6-ee90-4f0c-af7d-8e01131fb41f', url: 'https://github.com/aravindp98/trigent-test.git'
	}
	}
     stage('SonarQube analysis') {
		  environment{
		    sonarHome = tool 'SonarQubeScanner'
			}
            steps {
                withSonarQubeEnv('sonar') {
                        sh '''$sonarHome/bin/sonar-scanner \
                             -Dsonar.projectKey=qualitymetric \
                             -Dsonar.projectName=Python-project \
							 -Dsonar.projectVersion=1.0 \
                             -Dsonar.sources=.\
                             -Dsonar.language=py \
                             -Dsonar.sourceEncoding=UTF-8 \
							 -Dsonar.python.xunit.reportPath=nosetests.xml \
							 -Dsonar.python.coverage.reportPaths=coverage.xml \
							 -Dsonar.coverage.exclusions=coverage.xml'''
	   }
	}
	}
}
	post{
		always {
			cleanWs()
		}
	}
}
