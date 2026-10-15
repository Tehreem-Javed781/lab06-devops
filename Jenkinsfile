pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Repo is already checked out by "Pipeline script from SCM"
                sh 'docker compose down'
                sh 'docker compose pull'
                sh 'docker compose up -d'
            }
        }
    }
}
