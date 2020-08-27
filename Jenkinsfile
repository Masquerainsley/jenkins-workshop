pipeline {
    agent any

    stages {
        stage('Debug Info') {
            steps {
                echo "Building branch '${params.BRANCH}'"
                sh 'pwd'
                sh 'whoami'
                sh 'docker info'
            }
        }

        stage('Build') {
            steps {
                echo 'ToDo: Build the app'
            }
        }

        stage('Test') {
            steps {
                echo 'ToDo: Run the tests'
            }
        }

        // If the branch is master...
        stage('Deploy') {
            steps {
                echo 'ToDo: Deploy the app somnewhere'
            }
        }

        stage('Smoke Tests') {
            steps {
                echo 'ToDo: Run some smoke tests on the deployed app'
                echo 'ToDo: Post smoke test failure alert (e.g. in Slack)'
            }
        }

        stage('Rollback on Smoke Test Failure') {
            steps {
                echo 'ToDo: Run some smoke tests on the deployed app'
                echo 'ToDo: Post rollback alert (e.g. in Slack)'
            }
        }
    }
}
