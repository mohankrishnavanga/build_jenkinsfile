Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any
    environment {
         TEST_ENV = 'jenkins_test'
         TEST_SCRIPT = 'linux'
    }
    stages {
        stage('build') {
            steps {
                sh '''
                python --version
                echo $TEST_ENV
                echo $TEST_SCRIPT
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
    }

    post {
      always {
        echo 'One way or other, I have finished'
        deleteDir()
      }
      success {
        echo 'I succeeded!'
      }
      failure {
        echo 'I failed :('
      }
      changed {
        echo 'Things were different before'
      }
    }
}
