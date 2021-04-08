pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
		echo "${env.GIT_BRANCH}"
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
                sh 'cp -Rf . /home/ubuntu/web/'
                sh 'echo \'a\' | sudo -S systemctl restart pythonweb'
            }
        }
    }
}
