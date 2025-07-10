# app/webhook/utils.py

def extract_author(data, event_type):
    if event_type == "push":
        # For push events, expect "author" key in custom payload
        return data.get("author")
    elif event_type == "pull_request":
        # For pull_request, check for the PR author if available
        return data.get("pull_request", {}).get("user", {}).get("login") or data.get("author")
    return data.get("author")  # fallback for other types

def extract_from_branch(data, event_type):
    if event_type == "push":
        # Extract branch name from "ref"
        return data.get("ref", "").replace("refs/heads/", "")
    elif event_type == "pull_request":
        return data.get("pull_request", {}).get("head", {}).get("ref") or data.get("from_branch")
    return data.get("from_branch")  # fallback

def extract_to_branch(data, event_type):
    if event_type == "push":
        # From custom payload or fallback to "main"
        repo = data.get("repository")
        if isinstance(repo, dict):
            return repo.get("default_branch", "main")
        return data.get("to_branch") or "main"
    elif event_type == "pull_request":
        return data.get("pull_request", {}).get("base", {}).get("ref") or data.get("to_branch")
    return data.get("to_branch")  # fallback
