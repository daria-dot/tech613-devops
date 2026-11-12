# tech613-devops
A repo dedicated for learning devops at Sparta

Notes are grouped into one folder per topic. Each note's images live in an `images/` folder next to it.

## Updating the index

The index below is generated from the folder structure. After adding, renaming or moving a note, run this from anywhere inside the repo:

```bash
python3 scripts/generate_index.py
```

It needs Python 3 and nothing else. It rewrites only the part between the `INDEX:START` and `INDEX:END` markers, so you can edit the rest of this README by hand. Each entry is named after its file, followed by the note's first heading.

## Notes index

<!-- INDEX:START -->

### AI

- [Agentic AI](ai/agentic-ai.md)
- [Prompt engineering assignment](ai/prompt-engineering-assignment.md): Improving an AI Response with Prompt Engineering
- [What is AI](ai/what-is-ai.md): What is AI?

### AWS

- [AMI guide](aws/ami-guide.md): What is an AMI
- [Autoscaling](aws/autoscaling.md): What is autoscaling?
- [Boto3 S3 scripting](aws/boto3-s3-scripting.md): Managing AWS S3 with Python boto3
- [Deploy app with MongoDB](aws/deploy-app-with-mongodb.md): Deploying a database and connecting it to a web-app
- [Deploy webapp on EC2](aws/deploy-webapp-on-ec2.md): Deploying the Node.js 20 Tic-Tac-Toe App on AWS EC2 (Ubuntu)
- [EC2 first deployment notes](aws/ec2-first-deployment-notes.md)
- [EC2 SSH config](aws/ec2-ssh-config.md)
- [Monitoring](aws/monitoring.md): MONITORING DEPLOYED SYSTEMS
- [S3 storage](aws/s3-storage.md): What is S3 storage?
- [VPC two tier architecture](aws/vpc-two-tier-architecture.md): Building a Secure Two-Tier VPC Architecture on AWS

### Cloud

- [App architecture tiers](cloud/app-architecture-tiers.md)
- [Cloud computing basics](cloud/cloud-computing-basics.md): What is cloud computing?

### DevOps intro

- [What is DevOps](devops-intro/what-is-devops.md)

### Git

- [Git commands](git/git-commands.md)

### IaC

- [IaC and Ansible intro](iac/iac-and-ansible-intro.md): Intro to Infastructure as code

### Jenkins

- [CI CD and Jenkins intro](jenkins/ci-cd-and-jenkins-intro.md): Intro to Jenkins & CICD
- [Jenkins GitHub getting started](jenkins/jenkins-github-getting-started.md): Getting started with Jenkins and github
- [Jenkins GitHub SSH setup](jenkins/jenkins-github-ssh-setup.md): Setting up SSH protocal for Jenkins - authenticating GITHUB

### Linux

- [Bash scripting](linux/bash-scripting.md)
- [Changing file permissions](linux/changing-file-permissions.md)
- [File ownership](linux/file-ownership.md): Linux File Ownership
- [File permissions numeric values](linux/file-permissions-numeric-values.md): File Permissions Using Numeric Values
- [File permissions](linux/file-permissions.md): File Permissions - Research
- [Linux commands](linux/linux-commands.md): Linux Terminal
- [Redirection and appending](linux/redirection-and-appending.md)
- [Streams](linux/streams.md)

### Markdown

- [Markdown basics](markdown/markdown-basics.md): Tech613 Learning

### Networking

- [IP addresses and CIDR blocks](networking/ip-addresses-and-cidr-blocks.md): How addresses work?
- [Ports and protocols](networking/ports-and-protocols.md): How do machines communicate?

### Python

- [Python control flow](python/python-control-flow.md): Python Control Flow: Ops Scripting Notes

### Terraform

- [AWS credentials setup](terraform/aws-credentials-setup.md): Setting up AWS credentials on macOS
- [Terraform basics](terraform/terraform-basics.md): Terraform: Commands, Files and Providers
- [Terraform intro](terraform/terraform-intro.md): Intro to Terraform
- [Terraform setup](terraform/terraform-setup.md)

### Web servers

- [Nginx and proxies](web-servers/nginx-and-proxies.md): What is a proxy?

<!-- INDEX:END -->
