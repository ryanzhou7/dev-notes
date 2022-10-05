- [Crash course](https://news.ycombinator.com/item?id=32213066)

## [Docker](https://blog.gruntwork.io/a-crash-course-on-docker-34073b9e1833)

- `docker run -p 5000:5000 training/webapp`

## [K8](https://blog.gruntwork.io/a-crash-course-on-kubernetes-a96c3891ad82)

- **k8**: container orchestration tool
- dev -> api call -> k8 cluster[ control plane -manages-> worker nodes ]
- `kubectl config use-context docker-desktop`
- `kubectl create deployment simple-webapp --image training/webapp --replicas=2 --port=5000`
- `kubectl create service loadbalancer simple-webapp --tcp=80:5000`
  - Deploy loadbalancer to route traffic across replicas
  - Map port 80 -> 5000 (docker container)
  - `curl localhost`
- `kubectl get deployments`
  - in k8 **pods** rather than containers are deployed
  - **Pod**: group of containers meant to be deployed together
- `kubectl get pods`
- `docker kill container-id`
  - See that k8 will self-heal
- `kubectl get services`
- `kubectl set env deployment/simple-webapp PROVIDER=Gruntwork`
  - World of Hello world gets replaced
- Clean up
  - `kubectl delete service simple-webapp`
  - `kubectl delete deployment simple-webapp`
- But as IAC, .yml
- `kubectl apply -f deployment.yml`
- `kubectl apply -f service.yml`

## [In AWS](https://blog.gruntwork.io/a-crash-course-on-aws-59e4bc0bf398)

## [With TF](https://blog.gruntwork.io/a-crash-course-on-terraform-5add0d9ef9b4)

- [Code](https://github.com/brikis98/terraform-up-and-running-code)
-
