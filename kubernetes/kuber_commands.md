
# kubectl Cheat Sheet

## Look at what's running

```bash
kubectl get pods                      # list Pods in the current namespace
kubectl get pods -A                   # list Pods in all namespaces
kubectl get pods -o wide              # include node and IP
kubectl get deployments,services      # list several object types at once
kubectl get all                       # most object types in the namespace
kubectl get nodes                     # list the cluster's nodes
```

## Inspect and debug

```bash
kubectl describe pod <name>           # full details plus recent events (check this first when something breaks)
kubectl logs <pod>                    # container logs
kubectl logs -f <pod>                 # stream logs live
kubectl logs <pod> -c <container>     # logs from one container in a multi-container Pod
kubectl logs <pod> --previous         # logs from the last crashed instance
kubectl exec -it <pod> -- sh          # open a shell inside the container
kubectl get events --sort-by=.metadata.creationTimestamp
kubectl top pods                      # CPU/memory use (needs metrics-server)
```

## Create, update, delete

```bash
kubectl apply -f file.yaml            # create or update objects from a file
kubectl apply -f ./folder/            # apply every file in a folder
kubectl delete -f file.yaml           # delete the objects in a file
kubectl delete pod <name>             # delete one object
kubectl edit deployment <name>        # edit a live object in your editor
kubectl diff -f file.yaml             # preview what apply would change
```

## Manage Deployments

```bash
kubectl scale deployment <name> --replicas=5
kubectl set image deployment/<name> <container>=<image>:<tag>
kubectl rollout status deployment/<name>    # watch a rollout finish
kubectl rollout history deployment/<name>
kubectl rollout undo deployment/<name>      # roll back to the previous version
kubectl rollout restart deployment/<name>   # restart all Pods
```

## Networking

```bash
kubectl port-forward pod/<name> 8080:80     # reach a Pod at localhost:8080
kubectl port-forward svc/<name> 8080:80     # same, through a Service
kubectl expose deployment <name> --port=80 --type=ClusterIP
```

## Contexts and namespaces

```bash
kubectl config get-contexts                               # list clusters you can talk to
kubectl config use-context <name>                         # switch cluster
kubectl config set-context --current --namespace=<ns>     # change the default namespace
kubectl get pods -n <namespace>                           # run a command against one namespace
kubectl create namespace <name>
```

## Handy extras

```bash
kubectl explain deployment.spec             # built-in docs for any field
kubectl get pod <name> -o yaml              # the full live object as YAML
kubectl create deployment web --image=nginx --dry-run=client -o yaml > web.yaml   # generate starter YAML
kubectl api-resources                       # list every object type and its short name
```

## Shortcuts

| Short name | Object       |
|------------|--------------|
| `po`       | pods         |
| `deploy`   | deployments  |
| `svc`      | services     |
| `ns`       | namespaces   |
| `cm`       | configmaps   |
| `no`       | nodes        |

Add `alias k=kubectl` to your shell profile, then `kubectl get pods` becomes `k get po`.