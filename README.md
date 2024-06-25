# Webserver

## Description

This repo contains an example webserver, which can be hosted on a Kubernetes cluster.
Based on a helm chart, the webserver is deployed in a blue/green setup, where traffic is
load balanced between 2 different instances.

Both instances show a different string, which can be used to identity the instance you are
actually connected to

## Prerequisites

In order to work with this setup locally, make sure following is installed:

- Container runtime (e.g. Docker or Rancher)
- [helm](https://helm.sh)
- [kubectl](https://kubernetes.io/docs/reference/kubectl/)
- Kubernetes setup (e.g. [minikube](https://minikube.sigs.k8s.io/docs/))

## Container image

The container image is based on a small Python container hosting a Flask webserver.
Using an environment variable, the string displayed in the webserver can be set.

All source code related to the container image can be found in the [container](./container) subfolder

To build the container image, run the following command:

```bash
docker build -t webserver .
```

To start the container image, run:

```bash
docker run -d -p 80:80 -e DISPLAY_MESSAGE="Hello from Docker" webserver
```

## Helm chart

To deploy the webserver container image in Kubernetes, a helm chart can be found in the [bluegreen-deployment](./bluegreen-deployment) folder.
This setup deploys 2 containers, which both display a different string, "Hello" & "World".
Using a load balancer, traffic is being distributed between the 2 instances.

In order to deploy the setup, run the following command:

```bash
helm install bluegreen-deployment ./bluegreen-deployment
```

The deployment can be verified by running:

```bash
kubectl get deployments
kubectl get pods
kubectl get svc
kubectl get ingress
```

To retrieve the IP on which the load balancer is listeing, run:

```bash
kubectl get svc
```

Checkout the IP for the `bluegreen-deployment` in the `EXTERNAL IP` column.

Note: When running this setup in a local minikube setup, make sure to start a tunnel, this allows you to connect to the minikube internal network.

```bash
minikube tunnel
```

This above fetched IP can be used to connect to the load balancer via the browser to checkout the running webserver.

Alternativly, the following command can be used in the terminal:

```bash
for i in {1..10}; do curl http://localhost; echo; done
```
