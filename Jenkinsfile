import groovy.json.JsonSlurper

pipeline {
    agent any
    environment {
         TEST_ENV = 'jenkins_test'
         TEST_SCRIPT = 'linux'
    }
    parameters {
      string(defaultValue: 'https://172.19.34.165:9200', description: '', name: 'elasticClusterIP')
      string(defaultValue: 'admin', description: 'Elasticsearch User', name:'elasticUser')
    }
    stages {
        stage('build') {
            steps {
                sh '''
                python --version
                echo $TEST_ENV
                echo $TEST_SCRIPT
                '''
            withCredentials([usernamePassword(credentialsId: 'elastic-cluster', passwordVariable: 'PASS', usernameVariable: 'USER')]){
              sh "curl -u ${USER}:${PASS} ${params.elasticClusterIP} --insecure"
              }
            }
        }
        stage('Testing Json Variable') {
            steps {
                def getChannels = new File("D:\\Mohan\\workspace\\git\\build_jenkinsfile\\testchannels.json")
                getChannels = new JsonSlurper().parseText(getChannels.text)
                echo getChannels
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
