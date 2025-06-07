#  Azure Function CI/CD Demo

This task demonstrates how to create, configure, and deploy an **Azure Function** using **GitHub Actions** for Continuous Integration and Continuous Deployment (CI/CD). The function fetches the USD to INR exchange rate using an external API.

---

##  Features

- ✅ Python-based Azure Function App
- ✅ HTTP-triggered endpoint
- ✅ Returns INR exchange rates for USD
- ✅ GitHub Actions for automated CI/CD
- ✅ Infrastructure as Code (IaC) using Terraform
- ✅ Secrets managed via GitHub repository secrets settings

---

##  Project Structure

```bash
├── infra
│   ├── main.tf
│   ├── provider.tf
│   ├── terraform.tfstate
│   └── terraform.tfstate.backup
├── MyFunctionProj
│   ├── __pycache__
│   ├── function_app.py
│   ├── host.json
│   ├── local.settings.json
│   └── requirements.txt
└── README.md                

```

##  Infrastructure Setup with Terraform

Use the Infrastructure as Code (IaC) files to provision the Azure infrastructure locally with Terraform.

### Steps:

1. **Initialize Terraform**
   ```bash
   cd infra
   terraform init

2. **Preview Infrastructure Changes**
    ```bash
    terraform plan

3. **Apply Infrastructure**
   ```bash
   terraform apply -auto-approve

This IaC will create an Azure Resource Group, Azure Storage Account, and an Azure Function.
After provisioning infrastructure, push your changes to a new feature branch (new-function) and open a Pull Request (PR) for manual review and approval.
Once the PR is approved and merged into the main branch, the CI/CD pipeline will run automatically.

## CI/CD with GitHub Actions
Trigger:
The pipeline runs on every push to the main branch only if files inside the MyFunctionProj/ directory are changed.

**Workflow Path:**
   ```bash
   .github/workflows/azure-function.yml
   ```
**Key CI/CD Steps**

1. Check-out the repository

2. Set up the Python environment

3. Install dependencies

4. Deploy the Azure Function using the official Azure Functions GitHub Action


**GitHub Secrets**

| Secret Name                         | Purpose                            |
| ----------------------------------- | -----------------------------------|
| `AZURE_FUNCTIONAPP_PUBLISH_PROFILE` | Azure function publish profile XML |

You can download the publish profile from the Azure Portal under your Function App > "Get publish profile".


**Screenshots**

![image](https://github.com/user-attachments/assets/043bf879-0bbc-4fd1-8611-dd0f4cb1b30e)

![image](https://github.com/user-attachments/assets/1201f90c-fdd4-459f-bd33-0ec5ded3181a)

![image](https://github.com/user-attachments/assets/b9b48bcd-d8a2-4787-a54a-e97348ecc5a5)

![image](https://github.com/user-attachments/assets/a046bfc9-5071-4334-b699-af4942f2a06b)

![image](https://github.com/user-attachments/assets/a9f706cb-6b08-4919-afba-7dc3e0f7025e)

