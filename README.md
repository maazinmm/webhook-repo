# GitHub Webhook Listener Project (Flask + MongoDB + GitHub Actions)

## Overview:
This project implements a GitHub webhook listener using Flask to receive and process `push` and `pull_request` events from GitHub repositories. It logs event data such as author, source branch, and target branch into a MongoDB Atlas database for persistence and auditing. Additionally, GitHub Actions is used to automate sending events via a webhook on repo activity..