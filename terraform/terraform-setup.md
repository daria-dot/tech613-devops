# Terraform setup

How I installed Terraform, made it work from any terminal, and set up VS Code.

**Machine:** macOS 26.5 on Apple Silicon (`arm64`)
**Date:** 2026-11-04
**Terraform version:** v1.17.1

## 1. IaC folder

I made a new private GitHub repo, `tech613-iac` (option b), for IaC documentation. Terraform notes go in `terraform/` and Ansible will go in `ansible/`.

## 2. Install Terraform

**Manual option:** download the macOS ARM64 zip from <https://developer.hashicorp.com/terraform/install>, unzip it, and move the `terraform` binary into a folder for command-line tools

```bash
mkdir -p ~/.local/bin
mv ~/Downloads/terraform ~/.local/bin/
chmod +x ~/.local/bin/terraform
```

I also have a copy there at `~/.local/bin/terraform`, the same v1.17.1.

## 3. Test the install

```bash
terraform --version
```

Output:

```
Terraform v1.17.1
on darwin_arm64
```

## 4. Run `terraform` from anywhere (PATH)

A command works from any folder only if its directory is listed in the `PATH` environment variable.

- `/opt/homebrew/bin` is added to `PATH` automatically when Homebrew is installed (via `brew shellenv` in `~/.zprofile`).
- For the manual install I added `~/.local/bin` to `PATH` in `~/.zshrc` (zsh is the default macOS shell):

  ```bash
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
  source ~/.zshrc
  ```

Check which binary is being used and that it works in a new shell:

```bash
which -a terraform
```

```
/Users/user/.local/bin/terraform
/opt/homebrew/bin/terraform
```

The first one listed is the one that runs. I opened a new terminal window, ran `terraform --version` from a different folder, and got the same output as in step 3. It also works in a new bash login shell.

> **Windows equivalent:** put `terraform.exe` in e.g. `C:\my-cmd-line-tools`, then add that folder to **System Properties → Environment Variables → Path**, and open a new Git Bash window.

## 5. Deliverable: version output

```
$ terraform --version
Terraform v1.17.1
on darwin_arm64
```

## 6. VS Code extension

I installed the official **HashiCorp Terraform** extension (`hashicorp.terraform`, v2.40.1). It gives syntax highlighting, autocomplete, validation and formatting for `.tf` files.

Install it from the Extensions panel (search "HashiCorp Terraform", publisher **HashiCorp**), or from the terminal:

```bash
code --install-extension hashicorp.terraform
```

Check that it's installed:

```bash
code --list-extensions --show-versions | grep hashicorp
```

```
hashicorp.terraform@2.40.1
```

## Optional: tab completion

```bash
terraform -install-autocomplete
```

Then open a new terminal.
