# Lambda Cost Optimizer

A serverless project to monitor AWS Lambda costs and suggest cheaper alternatives. This tool scans CloudWatch and Cost Explorer data, logs high-cost functions, and recommends optimized compute options.

## 🔧 Features
- Fetch Lambda usage data via AWS Cost Explorer
- Identify expensive invocations
- Log insights to DynamoDB
- Suggest alternatives (e.g., batching, Fargate)

## 🧰 Tech Stack
- AWS Lambda (Python)
- AWS Cost Explorer API
- Amazon DynamoDB
- AWS CDK (Python or TypeScript)
- GitHub Actions (for CI)

## 🚀 How to Run Locally
1. Clone the repo  
2. Setup AWS credentials  
3. Deploy using CDK  
4. Trigger Lambda with sample data  

## 📦 Future Features
- Slack alert integration  
- Multi-account cost tracking  
- Dashboard using Grafana or CloudWatch

## ⚠️ AI Disclaimer
Some parts of this project use AI-generated boilerplate code (ChatGPT & GitHub Copilot), reviewed and customized before production use.
