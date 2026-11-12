
- [Intro to Jenkins \& CICD](#intro-to-jenkins--cicd)
  - [What is CI?](#what-is-ci)
  - [What is CD? Pros?](#what-is-cd-pros)
  - [CI/CD Pipeline Flow](#cicd-pipeline-flow)
- [Jenkins](#jenkins)
  - [Jenkins Architecture](#jenkins-architecture)
  - [Webhook](#webhook)
  - [What Happens During a Single Run](#what-happens-during-a-single-run)
  - [Why use Jenkins?](#why-use-jenkins)
  - [Stages of Jenkins](#stages-of-jenkins)
  - [Example Jeankinsfile](#example-jeankinsfile)
  - [Key Concepts](#key-concepts)
  - [Alternatives to Jenkins](#alternatives-to-jenkins)
  - [Why build pipeline? Buisness value?](#why-build-pipeline-buisness-value)
  - [Jenkins + AWS EC2 Integration](#jenkins--aws-ec2-integration)
    - [1. Architecture](#1-architecture)






# Intro to Jenkins & CICD

## What is CI?
* Continous Integration
* Automatically merging code
* Triggered by: Developers frequently pushing the code changes to shared repo
* Automatic tests are run on the code before main code integration
  
> **Benefits**
> 
> Help you identify and resolve bugs/issues early -> reduced costs
> 
> Helps to maintain stability and functionality of the software build
## What is CD? Pros?
* Can refer to continous Deployment(automatically deploys code to production)/Delivery(manual sign off/approval)
  
Continous Delivery -> ensures software is always in a deployable state, ready/ can bee pushed to production any time
* often involves producing deployable artifact
* requires manual release decision
  > **Benefit** 
  >
  > always have a deployable artifact
  
Continous Deployment (automatically deploys code to production)
* extends Continous Delivery by automating the final step of deploying to production

> **benefits** 
> 
> no manual intervention required
> 
> which is also a disadvantage as:
> removes human approval, relys entirely on automated proccesses


##  CI/CD Pipeline Flow

```mermaid
flowchart TD
    Start(["Code pushed to Git"]) --> Trigger["Jenkins pipeline triggered"]

    subgraph CI["Continuous Integration"]
        Checkout["1. Checkout source code"]
        Build["2. Build / Compile"]
        Unit["3. Unit tests (written before the code)"]
        Quality["4. Static analysis & security scan<br/>SonarQube / SAST / dependency check"]
        Package["5. Package artifact<br/>JAR / Docker image"]
        Publish["6. Push artifact to registry"]
        Checkout --> Build --> Unit --> Quality --> Package --> Publish
    end

    subgraph CD["Continuous Delivery / Deployment"]
        DevEnv["7. Deploy to Dev"]
        IntTest["8. Integration / API tests"]
        Staging["9. Deploy to Staging"]
        E2E["10. E2E / Performance tests"]
        Approval{"11. Manual approval?"}
        Prod["12. Deploy to Production"]
        Monitor["13. Monitor & health checks"]
        DevEnv --> IntTest --> Staging --> E2E --> Approval
        Approval -->|Approved| Prod --> Monitor
        Approval -->|Rejected| Stop(["Stop pipeline"])
    end

    Trigger --> Checkout
    Publish --> DevEnv

    Build -.->|fail| Fail["❌ Mark build failed<br/>Notify team"]
    Unit -.->|fail| Fail
    Quality -.->|fail| Fail
    IntTest -.->|fail| Fail
    E2E -.->|fail| Fail
    Monitor -.->|unhealthy| Rollback["↩️ Rollback to previous version"]

    Monitor --> Done(["Release complete"])
```


# Jenkins

* automation server
* open-source
* primarily used for CICD, bu can automate more 



##  Jenkins Architecture

```mermaid
flowchart LR
    Dev["Developer"] -->|git push / pull request| SCM[("Git Repository<br/>GitHub / GitLab / Bitbucket")]
    SCM -->|"Webhook or Poll SCM"| Controller

    subgraph JENKINS["Jenkins Server"]
        Controller["Jenkins Controller<br/>• Web UI & API<br/>• Reads Jenkinsfile<br/>• Plugins & Credentials<br/>• Schedules builds"]
        Queue["Build Queue"]
        Controller --> Queue
    end

    subgraph AGENTS["Build Agents (Executors)"]
        A1["Agent 1<br/>Linux VM"]
        A2["Agent 2<br/>Windows VM"]
        A3["Agent 3<br/>Docker / Kubernetes Pod"]
    end

    Queue -->|assigns job| A1
    Queue -->|assigns job| A2
    Queue -->|assigns job| A3

    A1 -->|logs & results| Controller
    A2 -->|logs & results| Controller
    A3 -->|logs & results| Controller

    Controller -->|store build output| Artifacts[("Artifact Repository<br/>Nexus / Artifactory / Docker Registry")]
    Controller -->|status| Notify["Notifications<br/>Slack / Email / Teams"]
    Controller -->|commit status ✅❌| SCM
```
## Webhook
-> a notification
-> webhook is sent by git and is being listened for by Jenkins

##  What Happens During a Single Run

```mermaid
sequenceDiagram
    autonumber
    actor Dev as Developer
    participant Git as Git Repo
    participant JC as Jenkins Controller
    participant Agent as Build Agent
    participant Reg as Artifact Registry
    participant Env as Target Environment

    Dev->>Git: git push
    Git->>JC: Webhook (new commit)
    JC->>JC: Read Jenkinsfile, queue build
    JC->>Agent: Assign job to free executor
    Agent->>Git: Checkout code (downloads-clones-)
    Agent->>Agent: Build, test, scan
    alt Stages pass
        Agent->>Reg: Push artifact / image
        Agent->>Env: Deploy
        Agent->>JC: Report SUCCESS
        JC->>Git: Set commit status ✅
    else A stage fails
        Agent->>JC: Report FAILURE + logs
        JC->>Git: Set commit status ❌
    end
    JC->>Dev: Notify (Slack / Email)
```

## Why use Jenkins? 
> **Benefits**
>
> * Automation
> * Extensibility: Jenkins has over 180 plugins
> * Scalability - server can scale easily by adding/using worker nodes/agents to run jobs
> * community support
> * cross-platofrm- across windows linux macos

> **Disadvanages**
> * Can be comlex for beginners
> * Maintainance overhead
> * resource- intensive when running multiple jobs
> * outdated user interface


## Stages of Jenkins

A typical CICD pipeline involves stages - 

1. Source Code management (SCM)
2. Build: Complie the code, build into executable artifact
3. Test: Automated tests (unit,integration,etc)
4. Package: Package into deployable artifact
5. If using Cont. Deployment, the package is deployed into the target environment e.g test, producation
6. Monitor: Monitoring tools may be deployed/configured to observe performance, log issues etc after deployment
  
## Example Jeankinsfile
```groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build') {
            steps { sh 'mvn clean compile' }
        }
        stage('Test') {
            steps { sh 'mvn test' }
        }
        stage('Package') {
            steps { sh 'docker build -t myapp:${BUILD_NUMBER} .' }
        }
        stage('Push') {
            steps { sh 'docker push myregistry/myapp:${BUILD_NUMBER}' }
        }
        stage('Deploy to Staging') {
            steps { sh './deploy.sh staging' }
        }
        stage('Approve Production') {
            steps { input message: 'Deploy to production?' }
        }
        stage('Deploy to Production') {
            steps { sh './deploy.sh production' }
        }
    }

    post {
        success { echo 'Pipeline succeeded' }
        failure { echo 'Pipeline failed - notify team' }
    }
}
```
## Key Concepts

| Term | Meaning |
|---|---|
| **Controller** | The main Jenkins server: hosts the UI, stores config, schedules jobs |
| **Agent** | A machine or container that actually runs build steps |
| **Executor** | A slot on an agent that can run one build at a time |
| **Jenkinsfile** | Pipeline-as-code file stored in the repo that defines the stages |
| **Stage / Step** | A stage is a logical phase (Build, Test); steps are the commands inside it |
| **Trigger** | What starts a build: webhook, polling, schedule (cron), or manual |
| **CI** | Automatically build and test every change |
| **CD** | Automatically deliver/deploy tested changes to environments |

## Alternatives to Jenkins
* Gitlab CI
* Github Actions
* Circle CI
* Travis CI
* Bamboo
* TeamCity
* Azure Devops(Azure pipelines)

## Why build pipeline? Buisness value?
* cost savings - automating repetitive processes
* faster time to market
* reduced risk of human error
* improved quality through continous feedback and improvement

## Jenkins + AWS EC2 Integration

Jenkins server: has three jobs that make up the pipeline:

Job 1 – CI: Test. Runs the tests on the new code

Job 2 – CI: Merge. Merges the code (from the dev branch)

Job 3 – CD: Deploy. Deploys the updated app

Built-in (master) node: set up so that jobs don’t run on it. Its role is to manage and 

delegate: it queues jobs, starts worker nodes, and hands jobs out to them

Worker (agent) nodes: EC2 instances launched from a custom AMI that already has all the 

dependencies the jobs need installed

### 1. Architecture

```mermaid
flowchart LR
    Dev[" Developer"] -->|git push| SCM[("GitHub / GitLab")]
    SCM -->|Webhook| ALB_J

    subgraph AWS["AWS Cloud"]
        IAM["IAM Role<br/>permissions for EC2, ECR, S3"]

        subgraph VPC["VPC"]
            subgraph PUB["Public Subnet"]
                ALB_J["Load Balancer<br/>Jenkins UI :443"]
                ALB_A["Load Balancer<br/>App traffic"]
            end

            subgraph PRIV1["Private Subnet: CI"]
                Controller["Jenkins Controller<br/>EC2 instance<br/>+ EC2 plugin"]
                EBS[("EBS volume<br/>JENKINS_HOME")]
                A1["Agent EC2<br/>on-demand"]
                A2["Agent EC2<br/>spot instance"]
            end

            subgraph PRIV2["Private Subnet: App"]
                App1["App Server EC2 #1"]
                App2["App Server EC2 #2"]
            end
        end

        EC2API["EC2 API"]
        ECR[("ECR / S3<br/>Build artifacts")]
    end

    ALB_J --> Controller
    Controller --- EBS
    IAM -.->|attached to| Controller
    Controller -->|"RunInstances / TerminateInstances"| EC2API
    EC2API -->|launches from AMI| A1
    EC2API -->|launches from AMI| A2
    Controller -->|"SSH: start agent.jar"| A1
    Controller -->|"SSH: start agent.jar"| A2
    A1 -->|checkout| SCM
    A1 -->|push image / artifact| ECR
    A2 -->|push image / artifact| ECR
    A1 -->|"deploy via SSH or CodeDeploy"| App1
    A1 -->|"deploy via SSH or CodeDeploy"| App2
    App1 -->|pull artifact| ECR
    App2 -->|pull artifact| ECR
    Users["🌐 Users"] --> ALB_A
    ALB_A --> App1
    ALB_A --> App2
```


