pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Build') {
            steps {
                echo 'Building.....'
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
