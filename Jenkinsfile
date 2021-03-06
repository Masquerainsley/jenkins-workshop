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
                sh './build.sh'
            }
        }

        stage('Test') {
            steps {
                sh './dockertest.sh'
            }
        }

        // If the branch is master...
        stage('Deploy') {
            when {
                expression { params.BRANCH == 'master' }
            }
            steps {
                echo 'ToDo: Deploy the app somnewhere'
            }
        }

        stage('Smoke Tests') {
            when {
                expression { params.BRANCH == 'master' }
            }
            steps {
                echo 'ToDo: Run some smoke tests on the deployed app'
                echo 'ToDo: Post smoke test failure alert (e.g. in Slack)'
            }
        }

        stage('Rollback on Smoke Test Failure') {
            when {
                expression { params.BRANCH == 'master' }
            }
            steps {
                echo 'ToDo: Run some smoke tests on the deployed app'
                echo 'ToDo: Post rollback alert (e.g. in Slack)'
            }
        }
    }
}
