import requests

# URL of the image
url = 'https://i.postimg.cc/0QfR4nJQ/3o.png'

# Send a GET request to fetch the image
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the image to a file
    with open('downloaded_image.png', 'wb') as file:
        file.write(response.content)
    print("Image downloaded and saved as 'downloaded_image.png'")
else:
    print(f"Failed to download image. Status code: {response.status_code}")
