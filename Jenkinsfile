
pipeline {
    agent any

    environment {
        DOCKERHUB_REPO = 'swathi1276/okcredit-recommender'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKERHUB_REPO%:%BUILD_NUMBER% .'
                bat 'docker tag %DOCKERHUB_REPO%:%BUILD_NUMBER% %DOCKERHUB_REPO%:latest'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'swathi1276',
                    passwordVariable: 'Docker@123'
                )]) {
                    bat '''
                        echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                        if errorlevel 1 exit /b 1
                        docker push %DOCKERHUB_REPO%:%BUILD_NUMBER%
                        if errorlevel 1 exit /b 1
                        docker push %DOCKERHUB_REPO%:latest
                        if errorlevel 1 exit /b 1
                        docker logout
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/deployment.yaml'
                bat 'kubectl apply -f k8s/service.yaml'
                bat 'kubectl rollout status deployment/okcredit-deployment --timeout=120s'
                bat 'kubectl get pods'
                bat 'kubectl get services'
            }
        }
    }

    post {
        success {
            echo 'OkCredit built, pushed, and deployed to Kubernetes.'
        }
        failure {
            echo 'Pipeline failed. Check the first failed stage in Console Output.'
        }
    }
}
