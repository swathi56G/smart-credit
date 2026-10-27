# OkCredit – Smart Credit Card Recommender (DevOps Mini Project)

A simple Flask app with three pages: Home (`/`), Recommendation Form (`/recommend`), and Result (after form submission). It uses illustrative sample cashback rates for Food, Shopping, and Travel, not real financial offers.

## Run locally
```bash
python -m pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Build and run Docker
```bash
docker build -t okcredit-recommender:local .
docker run --rm -p 5000:5000 okcredit-recommender:local
```
Open http://localhost:5000

## Before Jenkins/Kubernetes
Replace `YOUR_DOCKERHUB_USERNAME` in BOTH `Jenkinsfile` and `k8s/deployment.yaml` with the same Docker Hub username/repository. In Jenkins, create a Username with password credential ID `dockerhub-creds`; use a Docker Hub access token as its password.

Ensure the Jenkins Windows service account can access Docker Desktop and Kubernetes:
```bash
docker version
kubectl config current-context
kubectl get nodes
```

Configure a Jenkins Pipeline job from SCM:
- Git URL: your GitHub repository
- Branch: `*/main`
- Script path: `Jenkinsfile`

Pipeline stages: Checkout → Build Docker Image → Push Docker Image → Deploy to Kubernetes.

## Verify
```bash
kubectl get deployments
kubectl get pods
kubectl get services
kubectl rollout status deployment/okcredit-deployment
```
Try http://localhost:30082 when the pod is Ready. NodePort 30082 is chosen to avoid the common existing ports 30080/30081; change it if already allocated.

## File purpose
- `app.py`: Flask routes and recommendation calculation
- `templates/`: three HTML pages
- `static/style.css`: page styling
- `requirements.txt`: Python dependency
- `Dockerfile`: instructions to build the container
- `Jenkinsfile`: automated image build/push/deploy pipeline
- `k8s/deployment.yaml`: Kubernetes Deployment (one replica)
- `k8s/service.yaml`: NodePort Service to expose the app
