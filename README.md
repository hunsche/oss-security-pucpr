# OSS Security PUCPR

This repository is a simple demonstration of a CI/CD pipeline for basic open source security checks. It was created as part of a DevOps course project.

## 🔍 What It Does

The repository includes a Python script that performs a basic security validation by checking for the presence of essential files in open source projects, such as:

- `LICENSE`
- `README.md`
- `requirements.txt`

These files are commonly expected in well-structured open source projects to ensure legal clarity, documentation, and dependency management.

## ⚙️ CI/CD Pipeline

A GitHub Actions workflow is configured to automatically run the security check script on every push or pull request to the `main` branch. The workflow will fail if any of the required files are missing.

## 📁 Project Structure

```
.
├── .github
│   └── workflows
│       └── security.yml        # GitHub Actions workflow
├── check_security.py           # Python script to check required files
├── LICENSE                     # (Required)
├── README.md                   # (Required)
└── requirements.txt            # (Required)
```

## 🧪 How to Run Locally

Make sure you have Python 3.10+ installed, then run:

```bash
python check_security.py
```

## 🧠 Purpose

This project is purely educational. The goal is to simulate a CI/CD use case aligned with open source security practices.
