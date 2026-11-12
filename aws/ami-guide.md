# What is an AMI

An Amazon Machine Image (AMI) is an image that contains the software
configuration required to set up and boot an instance.

The lifecycle of an AMI includes creating, copying, deprecating, 
disabling, and deleting (deregistering) the AMI.

Automate the AMI lifecycle. You can use Amazon Data Lifecycle Manager to 
automate the creation, retention, copy, deprecation, and deregistration of 
Amazon EBS-backed AMIs and their backing snapshots. You can also use EC2 Image
Builder to automate the creation, management, an deployment of customized AMIs.

When selecting an AMI, consider the following requirements you might have for the instances that you want to launch:

The AWS Region of the AMI as AMI IDs are unique to each Region.

The operating system (for example, Linux or Windows).

The architecture (for example, 32-bit, 64-bit, or 64-bit ARM).

The root volume type (for example, Amazon EBS or instance store).

The provider (for example, Amazon Web Services).

Additional software (for example, SQL Server).


EC2 Image Builder is a fully managed AWS service that helps you to automate the creation, management,
and deployment of customized, secure, and up-to-date server images. You can use the AWS Management
Console, AWS Command Line Interface, or APIs to create custom images in your AWS account.

# deploying an app using an image on AMI

![Screenshot 2026-10-26 at 16.08.15.png](images/Screenshot%202026-10-26%20at%2016.08.15.png)

Deploying an app with an AMI

Part 1: Build the image

Launch a base instance: Ubuntu, key pair, and a security group allowing SSH (22) and HTTP (80).
Run your setup script over SSH or as user data. It installs Node 20, gets the app code, runs npm install, sets up pm2 (or systemd) and configures nginx to forward port 80 to 3000.
Check it works: open http://<public-ip>. For the auto-start version
Create the image: Instance → Actions → Image and templates → Create image. Give it a clear name and wait until the status is Available.
Terminate the builder instance to save cost.

Part 2: Deploy from the image

Launch from the AMI: AMIs → select yours → Launch instance from AMI, with the same key pair and security group.
Add user data if needed:
pm2 image: paste the short user-data.sh, which only starts the app. Nothing gets installed.
Auto-start (systemd) image: leave user data empty.
Test: after about a minute, open http://<public-ip>.