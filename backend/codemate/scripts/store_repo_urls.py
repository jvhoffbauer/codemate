import json
import os

REPO_LIST_FILE = "data/_meta/dependents.json"
REPOS_FOLDERS = "data/processed"
REPO_URL_FILE = "data/_meta/repo_urls.json"


def main():
    # Get repo urls for the files in the processed folder
    # using the full repo names that we stored in dependents.json
    # And save them in repo_urls.json

    repos = json.load(open(REPO_LIST_FILE))
    print("Has repos:", len(repos))
    print(f"First 10: {repos[:10]}")

    repo_urls = {}
    for folder in os.listdir(REPOS_FOLDERS):
        # Get repo name
        repo_name = folder.split("-")[:-1]
        repo_name = "-".join(repo_name)

        # Get branch name
        branch_name = folder.split("-")[-1]

        # Get repo url
        urls = [r for r in repos if repo_name in r]
        url = urls[0]
        url = f"https://github.com/{url}/blob/{branch_name}/"

        repo_urls[repo_name] = url

    # Save repo urls
    json.dump(repo_urls, open(REPO_URL_FILE, "w"))


if __name__ == "__main__":
    main()
