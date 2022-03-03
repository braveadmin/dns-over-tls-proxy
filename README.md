# dns-over-tls-proxy
Creates a docker container where dns petitions can be send and converts it to dns-over-tls.

## Installation

1. Create the docker image
> docker build -t dot-proxy .

2. Create the docker container in detach mode.
> docker run -ti -d --name dot-proxy dot-proxy

3. Get the container's IP
> docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' dot-proxy

4. Run the dig command replacing the `{DOCKER_IP}` with the IP get in the previous command
> dig @{DOCKER_IP} +tcp wikipedia.org

