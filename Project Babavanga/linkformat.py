import requests

def list_github_folder_files(user, repo, branch, folder_path):
    """
    List all files in a GitHub repository folder using GitHub API.
    """
    api_url = f"https://api.github.com/repos/{user}/{repo}/contents/{folder_path}?ref={branch}"
    response = requests.get(api_url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch folder contents: {response.status_code} {response.text}")
    
    files_data = response.json()
    files = []
    for item in files_data:
        if item['type'] == 'file':
            raw_url = item['download_url']  # Direct raw file URL
            files.append(raw_url)
        elif item['type'] == 'dir':  # Recursively fetch subfolders
            files.extend(list_github_folder_files(user, repo, branch, item['path']))
    return files


def print_links_in_format(links):
    """
    Print links in your desired format.
    """
    for link in links:
        print(f'      "{link}",')


# Example usage
user = "Sivatech24"
repo = "ImgHost"
branch = "main"
folder_path = "ImagesSet1"

all_links = list_github_folder_files(user, repo, branch, folder_path)

print("Formatted Links:")
print_links_in_format(all_links)
