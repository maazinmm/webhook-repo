# app/webhook/utils.py



def extract_author(data, event_type):
    if event_type == "push":
        # For push events, the author is usually the pusher
        return data.get("pusher", {}).get("name")
    elif event_type == "pull_request":
        # For pull_request events, the author is the user who opened the PR
        return data.get("pull_request", {}).get("user", {}).get("login")
    return None

def extract_from_branch(data, event_type):
    if event_type == "push":
        # For push events, the source branch is usually the one being pushed
        return data.get("ref", "").replace("refs/heads/", "")
    elif event_type == "pull_request":
        # For pull_request events, the source branch is the one from which the PR is created
        return data.get("pull_request", {}).get("head", {}).get("ref")
    return None

def extract_to_branch(data, event_type):
    if event_type == "push":
        # For push events, the target branch is usually the one being pushed to
        return data.get("repository", {}).get("default_branch")
    elif event_type == "pull_request":
        # For pull_request events, the target branch is the one into which the PR is merged
        return data.get("pull_request", {}).get("base", {}).get("ref")
    return None 