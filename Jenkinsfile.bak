pipeline{
  agent any
  stages{
    stage('checkout'){
	steps{
	checkout([$class: 'GitSCM', branches: [[name: '*/docker-sample']], extensions: [], userRemoteConfigs: [[credentialsId: 'd1a8d5f6-ee90-4f0c-af7d-8e01131fb41f', url: 'https://github.com/aravindp98/trigent-test.git']]])
	}
	}
	stage('test'){
	   steps{
	      sh " pip install nose coverage nosexcover pylint "
			   }
			   }
    //stage('coverage'){
	   // steps{
		//  script{ 
		//  sh " nosetests --with-xunit --xunit-file=nosetests.xml --with-coverage --cover-package=. --cover-branches --cover-xml "
     stage('SonarQube analysis') {
		  environment{
		    sonarHome = tool 'SonarQubeScanner'
			}
            steps {
                withSonarQubeEnv('sonar') {
                        sh '''$sonarHome/bin/sonar-scanner \
                             -Dsonar.projectKey=mycode \
                             -Dsonar.projectName=sample-test \
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
}