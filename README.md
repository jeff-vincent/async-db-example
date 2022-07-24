# redis-queue-mongo-example-python
flask; redis; redis queue; mongo

## Docker-Compose
```
docker-compose -f docker-compose.yml up
```
## Run in [Velocity](https://docs.velocity.tech/intro-and-overview/readme)
```
helm template /k8s --values /k8s/velocity-values.yml | veloctl env create -f -
```
