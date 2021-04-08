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
                script {
                    if (env.GIT_BRANCH == 'master') {
                        sh 'echo \'a\' | sudo -S scp -i /home/ubuntu/hungcao.pem -r ./* ubuntu@18.140.64.78:/home/ubuntu/web/'
                        sh '''sudo ssh -i /home/ubuntu/hungcao.pem ubuntu@18.140.64.78 << EOF 
                                echo \'a\' | sudo -S systemctl restart pythonweb.service
                            EOF'''
                    } else {
                        sh 'pwd'
                        sh 'cp -Rf . /home/ubuntu/web/'
                        sh 'echo \'a\' | sudo -S systemctl restart pythonweb'
                    }
                }
            }
        }
    }
}
