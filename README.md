1-First, we give the necessary permissions to the scripts by running
"chmod +x kubectl-helm.sh", "chmod +x docker.sh" and "chmod +x
terraform-install.sh".

2-We run "kubectl-helm.sh" and "docker.sh" located in the project's root
directory. These scripts install Kubernetes, Docker, and Helm.

3-Now, we run "terraform-install.sh" located in the project's root
directory. This script will install Terraform.

4-Now we can run "terraform init".

5-We need to run the "terraform apply" command in the directory where
the main.tf file is located.

6-To check our Kind cluster, we use "kubectl get nodes".

7-Now it's time to install Jenkins and create pipelines.

8-Now we can run "./jenkins.sh". This script will install Jenkins

If jenkins.sh fails to run, we may need to execute the command "sudo rm
/etc/apt/sources.list.d/docker.list
/etc/apt/sources.list.d/kubernetes.list" to remove potential conflicting
sources. Then, we run ./jenkins.sh again.

9-You should check whether Jenkins is running or not by using the
command systemctl status jenkins.service.

10-It is necessary to install Jenkins' Kubernetes plugins. These are:
Kubernetes Client API Plugin, Kubernetes Credentials Plugin, and
Kubernetes Plugin.

11-The next step will be to load and manage the credentials required for
Jenkins stages. These credentials should be for Github, DockerHub, and
the secret file within kubeconfig.

Jenkins-GitHub access should be with a GitHub token, Jenkins-DockerHub
access should be with a username and password, and Jenkins-Kubernetes
communication should be with a secret file.

12-It will be important for Jenkins to access the docker group for the
application to run and be controlled. Therefore, the Jenkins user should
be added to the docker group on the server.

13-Our application is ready! It can now be built and deployed.
