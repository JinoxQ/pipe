pipeline {
    agent any
    stages{
        stage('SCM checkout') {
            steps {
               git branch: 'main', url: 'https://github.com/JinoxQ/pipe.git'
            }
        }
        stage ('docker image build') {
            steps {
                sh '/usr/bin/docker image build -t jinoxq/fla .'
            }
        }
        stage ('token login') {
            steps{
                sh 'echo dckr_pat_RkcQsWcChNo8rx50wBfo43XJQSo | /usr/bin/docker login -u jinoxq --password-stdin'
            }
        }
        stage ('push image') {
            steps{
                sh '/usr/bin/docker image push jinoxq/fla'
            }
        }
        stage ('remove service') {
            steps{
                sh '/usr/bin/docker service rm flask-service'
            }
        }
        stage ('create service') {
            steps{
                sh '/usr/bin/docker service create --name flask-service -p 9090:80 --replicas 2 jinoxq/fla'
            }
        }
    }
}
