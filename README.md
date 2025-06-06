#  Azure Function CI/CD Demo

This project demonstrates how to create, configure, and deploy an **Azure Function** using **GitHub Actions** for Continuous Integration and Continuous Deployment (CI/CD). The function fetches the USD to INR exchange rate using an external API.

---

##  Features

- ✅ Python-based Azure Function App
- ✅ HTTP-triggered endpoint
- ✅ Returns INR exchange rates for USD
- ✅ GitHub Actions for automated CI/CD
- ✅ Infrastructure as Code (IaC) using Terraform
- ✅ Secrets managed via GitHub repository scerets settings

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
└── README.md                 # Project documentation
