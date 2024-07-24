import requests

def check_dependencies(url):
    response = requests.get(url)
    dependencies = ["jquery", "angular", "react"]
    
    found_dependencies = []
    for dep in dependencies:
        if dep in response.text:
            found_dependencies.append(dep)
    
    return found_dependencies

if __name__ == "__main__":
    target_url = "http://example.com/static/js/vendor.js"
    dependencies = check_dependencies(target_url)
    print(f"Dependencies found: {dependencies}")
