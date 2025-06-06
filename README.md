#  Azure Function CI/CD Demo

This project demonstrates how to create, configure, and deploy an **Azure Function** using **GitHub Actions** for Continuous Integration and Continuous Deployment (CI/CD). The function fetches the USD to INR exchange rate using an external API.

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


After the infrastructure is provisioned, push the code to GitHub to trigger the CI/CD pipeline.


## CI/CD with GitHub Actions
Trigger:
The pipeline runs on every push to the main branch only if files inside the MyFunctionProj/ directory are changed.

**Workflow Path:**
   ```bash
   .github/workflows/azure-function.yml
   ```
**Key CI/CD Steps**

1. Checkout the repository

2. Set up the Python environment

3. Install dependencies

4. Deploy the Azure Function using the official Azure Functions GitHub Action


**GitHub Secrets**

| Secret Name                         | Purpose                            |
| ----------------------------------- | -----------------------------------|
| `AZURE_FUNCTIONAPP_PUBLISH_PROFILE` | Azure function publish profile XML |

You can download the publish profile from the Azure Portal under your Function App > "Get publish profile".

