import requests

def directory_brute_force(url, wordlist_file):
    with open(wordlist_file, 'r') as file:
        directories = file.readlines()

    found_dirs = []
    for directory in directories:
        directory = directory.strip()
        full_url = url + "/" + directory
        response = requests.get(full_url)
        if response.status_code == 200:
            found_dirs.append(full_url)
    return found_dirs

if __name__ == "__main__":
    target_url = "http://example.com"
    wordlist = "directory_brute_force_common_dirs.txt"
    found_dirs = directory_brute_force(target_url, wordlist)
    print(f"Found directories: {found_dirs}")
