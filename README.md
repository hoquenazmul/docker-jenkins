# Docker-Jenkins
## Jenkins Infrastructure
**Jenkins Master Server:** It handles the scheduling of jobs, dispathces them to agents for execution, and monitors their progress.
**Jenkins Agent:** An agent is machine or a process that performs the tasks that Jenkins Master assigns to it. For example: building software, running tests, or deploy apps.
#### How They Work Together
- The master server sends a job to an agent based on it's availability
- The agent runs the job, performs the necessary tasks, and then sends the results back to the master
- The master collects all results and displays them in the Jenkins dashboard, providing feedback to the users.

For example, Dev commits some code in git repo, the Jenkins master becomes aware of this commit and trigger the appropriate pipeline, and distribute the build to one of the agent to run. Agent selected based on configured labels. Then the agent runs the build.

## Setting up Jenkins Using Docker
### To build jenkins image based on Dockerfile
`docker build -t jenkins-blueocean-python:2.462.1-jdk17 .`

### To create a jenkins to attach with Jenkins Docker Container
`docker network create jenkins`

### To run Jenkins as Docker Container
**For Linux/Mac**
```bash
docker run --name jenkins-blueocean --restart=on-failure --detach \
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  jenkins-blueocean-python:2.462.1-jdk17
```
**For Windows**
```bash
docker run --name jenkins-blueocean --restart=on-failure --detach `
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 `
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 `
  --volume jenkins-data:/var/jenkins_home `
  --volume jenkins-docker-certs:/certs/client:ro `
  --publish 8080:8080 --publish 50000:50000 jenkins-blueocean-python:2.462.1-jdk17
```

Then we should see jenkins running on `localhost:8080`
And restart jenkins anytime, we can use `<jenkins_url>/safeRestart` or `<jenkins_url>/restart` 

**We need initial password in order to open jenkins dashboard for very first time. here is the way to get that pass:**
`docker exec <container-id> cat /var/jenkins_home/secrets/initialAdminPassword`

For more info, please visit: https://www.jenkins.io/doc/book/installing/docker/

## Setting up your Local Machine/VM as a Docker Cloud
- Go to Manage Jenkins => Clouds => Install 'Cloud Provider' Plugins => Docker (In our case, we've to install 'Docker' plugin only)
- Go to Manage Jenkins => Clouds => New Cloud => Create new Docker Cloud => for the Docker Host URI, please follow next 3 steps
- To set your physical/virtual machine as docker cloud, please launch a container first using alpine/socat image
 - `docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock`
- Inspect the socat container and grab the IP address
  - `docker inspect <socat-container>`
- Now use socat container IP address as 'Docker Host URI' inside Configure Cloud, like this: tcp://<socat-container-ip>:2375
- After hitting 'Test Connection' button, if you see the version, that means you're connected properly
- Click 'Save' Button at the bottom
<img src="jenkins-agent/img/create-new-cloud.png">
For more info, please visit: https://stackoverflow.com/questions/47709208/how-to-find-docker-host-uri-to-be-used-in-jenkins-docker-plugin


<br/><br/>
Once the Docker Cloud setup completed, we can create Jenkins Agent following Docker Agent templates steps, so Jenkins Master can distribute workloads on those agent.
<img src="jenkins-agent/img/create-docker-agent-templates.png">
