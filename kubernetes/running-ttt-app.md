# Kubernetes notes: deploying the tic-tac-toe app locally

## Overview

Running 3 copies of my tic-tac-toe app on the local Kubernetes cluster (Docker Desktop), reachable from my machine on port 30001. 




 `nginx-deploy.yml` -> Deployment -> Keeps 3 app Pods running at all times 

`nginx-service.yml` -> Service (NodePort) -> Gives the Pods one stable address, reachable on port 30001 




## Step 1: Go to the folder with the YAML files

```bash
cd kubernetes/yaml-definitions/local-ttt-app-deploy
ls
```

## Step 2: Deployment file

The Deployment tells Kubernetes to always keep 3 Pods running from my image.

```yaml
# YAML is case sensitive. Indent with spaces, never tabs.
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tttapp-deployment     # name of the Deployment
spec:
  selector:
    matchLabels:
      app: tttapp             # manage Pods that carry this label
  replicas: 3                 # keep 3 Pods running
  template:                   # blueprint for each Pod
    metadata:
      labels:
        app: tttapp           # must match the selector above
    spec:
      containers:
      - name: tttapp
        image: dashaneuro/tech613-tttapp:1.2.0   # my image on Docker Hub
        ports:
        - containerPort: 3000 # the port the app listens on (set in index.js)
```



## Step 3: Create the Deployment and check it

```bash
kubectl apply -f nginx-deploy.yml
kubectl get pods
```



## Step 4: Service file

The Service gives the 3 Pods one address and opens port 30001 on my machine.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: tttapp-service
  namespace: default      # used automatically if left out
spec:
  ports:
  - nodePort: 30001       # port opened on my machine; range is 30000-32767
    port: 80              # the Service's own port inside the cluster
    targetPort: 3000      # the app's port in the container (matches containerPort)
  selector:
    app: tttapp           # send traffic to every Pod with this label
  type: NodePort          # reachable from outside the cluster
```

How a request travels through the ports:

```
browser → localhost:30001 (nodePort) → tttapp-service:80 (port) → Pod:3000 (targetPort)
```

`targetPort` has to be 3000

## Step 5: Create the Service and open the app

```bash
kubectl apply -f nginx-service.yml
kubectl get svc
kubectl get endpoints tttapp-service
```

- `get svc` – `tttapp-service` shows `80:30001/TCP`
- `get endpoints` – lists 3 Pod addresses ending in `:3000`. If it says `<none>`, the labels don't match.

Open **http://localhost:30001**. The tic-tac-toe app loads.

## Step 6: Test self-healing

Delete one Pod and watch the Deployment replace it:

```bash
kubectl get pods
kubectl delete pod <one-tttapp-pod-name>
kubectl get pods -w
```



## To delete

```bash
kubectl delete -f .
kubectl get all
```

