pipeline {
   agent any
   stages {
       stage('Deploy') {
           steps {
               timeout(time: 1, unit: 'MINUTES') {
                   sh 'jenkins/fib 5'
               }
               timeout(time: 1, unit: 'MINUTES') {
                   sh 'jenkins/fib 32'
               }
           }
       }
   }
}
