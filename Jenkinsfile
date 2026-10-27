
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out OkCredit project'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image'
                bat 'docker build -t okcredit-recommender:latest .'
            }
        }

        stage('Docker Login') {
            steps {
                echo 'Logging in to Docker Hub'

                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'swathi1276',
                    passwordVariable: 'Docker@123'
                )]) {
                    bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo 'Pushing Docker Image to Docker Hub'
                bat 'docker tag okcredit-recommender:latest swathi1276/okcredit-recommender:latest'
                bat 'docker push swathi1276/okcredit-recommender:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying OkCredit to Kubernetes'

                bat 'kubectl config use-context docker-desktop'
                bat 'kubectl apply -f k8s/deployment.yaml --validate=false'
                bat 'kubectl apply -f k8s/service.yaml --validate=false'
                bat 'kubectl rollout status deployment/okcredit-deployment --timeout=120s'
                bat 'kubectl get pods'
                bat 'kubectl get services'
            }
        }
    }

    post {
        success {
            echo 'OkCredit pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the Jenkins Console Output for the error.'
        }
    }
}
