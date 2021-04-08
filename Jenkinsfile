pipeline {
    agent any

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
                sh 'pwd'
                sh 'cp -Rf . /home/ubuntu/web/'
                sh 'echo \'a\' | sudo -S systemctl restart pythonweb'
            }
        }
    }
}
