# 📡 GitHub Webhook Receiver – `webhook-repo`

This project listens for GitHub activity from a separate repository (`action-repo`) via custom webhooks triggered by GitHub Actions. It logs event data and displays it on a simple frontend.

---
Technologies Used:
- Flask (Python)
- MongoDB (logging events)
- GitHub Actions (in `action-repo`)
- Ngrok (for exposing local server)
- Vanilla JS + HTML (frontend)


## How It Works
### Workflow Overview

1. **`action-repo`** triggers a GitHub Action when a `push` or `pull_request` occurs.
2. That Action sends a webhook (`POST`) request to this Flask app.
3. This app logs the event in MongoDB and makes it viewable on a web interface.

## Project Structure

```
webhook-repo/
├── app/
│   └── webhook/
│       ├── routes.py        # Defines the Flask route for receiving webhooks
│       └── utils.py         # Functions to extract author, branch, etc.
├── templates/
│   └── index.html           # Frontend to display logged events
├── run.py                   # Flask app entry point
└── requirements.txt         # Python dependencies
```
## Running the Webhook Receiver

1. Clone and Set Up

```
git clone https://github.com/YOUR_USERNAME/webhook-repo.git
cd webhook-repo
python -m venv venv
source venv/bin/activate  # Or venv\Scripts\activate on Windows
pip install -r requirements.txt
```
2. Start Flask Server
```
python run.py
```
3. Expose with Ngrok
In a separate terminal:
```
ngrok http 5000
```
Copy the `https://....ngrok-free.app` URL — this is your public webhook endpoint.
## What Triggers the Webhook?
In `action-repo`, a GitHub Action like this is used:
```
name: Trigger Webhook via Curl

on:
  push:
    branches:
      - '**'
  pull_request:
    types: [opened, closed, synchronize]

jobs:
  notify-webhook:
    runs-on: ubuntu-latest
    steps:
      - name: Send webhook to Flask server
        run: |
          curl -X POST https://<NGROK_URL>/webhook/receiver \
          -H "Content-Type: application/json" \
          -H "X-GitHub-Event: ${GITHUB_EVENT_NAME}" \
          -d '{
            "event_type": "'${{ github.event_name }}'",
            "author": "'${{ github.actor }}'",
            "ref": "'${{ github.ref }}'",
            "repository": "'${{ github.repository }}'",
            "timestamp": "'${{ github.event.head_commit.timestamp }}'"
          }'

```
## Frontend: View the Logs
Open the app in your browser:
```
http://localhost:5000
```
You’ll see:
- Push and Pull Request events
- Author and branch info
- Formatted timestamps
- Automatically updates every 15 seconds

![mongodb collection documents](image-1.png)

<sub>Github events logs in mongoDB documents inside webhook_logs collection</sub>

![Flask Web UI](image-2.png)

<sub>Github events in flask Web UI</sub>