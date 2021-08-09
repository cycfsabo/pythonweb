pipeline {
    agent runner

    stages {
        stage('Pull') {
            steps {
		echo "Pulling from...${env.GIT_BRANCH}"
            }
        }
        stage('Build') {
            steps {
                echo 'Building.....Done!'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing......Done!'
            }
        }
        stage('Deploy') {
            steps {
		        echo 'Deploy successfully!'
            }
        }
    }
}