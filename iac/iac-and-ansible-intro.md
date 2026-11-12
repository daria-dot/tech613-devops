# Intro to Infastructure as code

* automate and manage infrastructure
* your platform
* and services that run on that platform
  
Terraform is open source and declarative -> define the end result wanted

Preparing infrastructure:
1. private network space
2. ec2 server instance
3. install docker and other tools
4. security
   
## What problem needs solving?

provisioning servers --> the process of setting up and configuring servers



## solving the problem

Infrastructure as code (IaC) can do all the provsioning of:
* the infrastructure itself ( servers & the network & extra resources)
* configuring the servers i.e installing the correct software and configuring the settings.. in an automated + repeatable manner
  
The process typically involves:
1. creating the server instance
2. configuring os and software
3. deploy application
4. configuring monitoring and logging

## Ansible vs Terraform
- terraform is mainly an infrastructure provisioning tool
- can also deploy apps on that infrastructure
- more advanced in orchestraction
- Ansible - mainly a configuration tool - configure the infrastructure


## Ansible


# Intro to Ansible

* What is Ansible?
  * configuration management tool
  * best at configuring software
  * command-based not GUI
  * Red Hat leads development, guaranteeing quality open-source code
  * Application is written in Python
  * Started off with a few core modules for managing/configuring Linux servers
  * Can be used now with almost any system

* How does Ansible work?
  * It's like having recipes that your robot (Ansible) follows to setup/configure software on
  * We write the configuration files in YAML (the recipes) - called "playbooks"
  * The robot (Ansible) can login via SSH and then configure the software on a device
  * "Ansible Control Node" (a controller computer/host) to tell the Target Nodes (the machines/hosts/servers that need configuring) what to do
  * "Playbooks" and "Inventory" (list of Target Nodes)
  * Unique attributes:
    * Module-based architecture
    * Agentless
      * No need to install Ansible on Target Nodes
      * Instead, Ansible controller will SSH into Target Nodes
      * A Python intepreter is required on Linux Target Nodes