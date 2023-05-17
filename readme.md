# Install yugabyte with Helm
```sh
helm install yugabyte charts/yugabyte -n yugabyte --create-namespace
```
# Monitoring Yugabyte
Now that we have our cluster we want to monitor it using Grafana and Prometheus. To achieve that we are going to use the kube-prometheus-stack.
```sh
helm install prometheus helm-charts/kube-prometheus-stack -n monitoring --create-namespace
```
Now that we have prometheus operator running, we are going to provide the prometheus configmap to get metrics from yugabyte.
```sh
kubectl apply -f yamls/monitoring/rbac.yaml
kubectl apply -f yamls/monitoring/role.yaml
kubectl apply -f yamls/monitoring/role-binding.yaml
kubectl apply -f yamls/monitoring/prometheus-config-new.yaml
kubectl apply -f yamls/monitoring/prometheus-service.yaml
kubectl apply -f yamls/monitoring/prometheus-deployment.yaml
kubectl apply -f yamls/monitoring/pv.yaml
kubectl apply -f yamls/monitoring/grafana-pvc.yaml
kubectl apply -f yamls/monitoring/grafana-deployment.yaml
kubectl apply -f yamls/monitoring/grafana-service.yaml
```