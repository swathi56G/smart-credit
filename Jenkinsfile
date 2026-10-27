
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t okcredit-recommender:v1 ."
            }
        }

        stage('Docker login') {
            steps {
                bat "docker login -u swathi1276 -p Docker@123"
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Push Docker Image to Docker Hub"
                bat "docker tag okcredit-recommender:v1 swathi1276/okcredit-recommender:latest"
                bat "docker push swathi1276/okcredit-recommender:latest"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/deployment.yaml --validate=false'
                bat 'kubectl apply -f k8s/service.yaml --validate=false'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }

        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}
