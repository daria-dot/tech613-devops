
# Setting up AWS credentials on macOS

1. Installed AWS CLI v2 using the official `.pkg` installer
2.  Verified the install with `aws --version`.
3. Ran `aws configure` and entered my access key ID, secret access key, default region and output format. The credentials are stored in `~/.aws/credentials`, which Terraform reads automatically.
4. Ran `aws sts get-caller-identity` to confirm the credentials authenticate successfully.


