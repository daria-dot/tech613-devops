

source -> reads the variable assignments from the file
The supplied ssh_config selects your private key and the lab's connection route; -F tells SSH to read that configuration file:
ssh -F ssh_config ubuntu@"$PUBLIC_IP"