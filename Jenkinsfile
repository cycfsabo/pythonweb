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
                if (env.GIT_BRANCH == 'master') {
                    sh 'echo \'a\' | sudo -S scp -i /home/ubuntu/hungcao.pem -r ./* ubuntu@18.140.64.78:/home/ubuntu/web/'
                    sh 'echo \'a\' | sudo -S ssh -i /home/ubuntu/hungcao.pem ubuntu@18.140.64.78'
                    sh 'echo \'a\' | sudo -S systemctl restart pythonweb.service'
                } else {
                    sh 'pwd'
                    sh 'cp -Rf . /home/ubuntu/web/'
                    sh 'echo \'a\' | sudo -S systemctl restart pythonweb'
                }
            }
        }
    }
}
