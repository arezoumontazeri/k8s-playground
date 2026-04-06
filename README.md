# k8s-playground

A hands-on Kubernetes playground to explore, experiment, and build a deep understanding of core concepts.

## Phase 1
This phase focuses on:
- Pod
- Deployment
- Service
- Replicas
- Labels and selectors
- Self-healing
- Rollout behavior

## Project Structure

```bash
app/
k8s/

## Build

docker build -t simple-fastapi:v1 ./app

## Apply

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

## Test 

kubectl port-forward svc/simple-fastapi 8080:80
curl http://localhost:8080/healthz

