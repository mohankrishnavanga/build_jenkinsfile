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
              script {
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
        }
        stage('Testing Json Variable') {
            steps {
              script {
                sh 'ls -ltr'
                def getChannels = new JsonSlurper().parseText(new File("$workspace/testchannels.json").text)
                sh 'python scripts/getJson.py $getChannels'
                /*print getChannels
                print getChannels['parentname']
                print getChannels['childchannels']['childchannel1'] */
            }
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
