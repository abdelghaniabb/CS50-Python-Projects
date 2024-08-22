import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Regular expression to match the YouTube embed URL in the src attribute
    pattern = r'src="(https?://(?:www\.)?youtube\.com/embed/([^"]+))"'
    match = re.search(pattern, s)

    if match:
        # Extract the video ID from the matched URL
        video_id = match.group(2)
        # Return the short URL format
        return f"https://youtu.be/{video_id}"

    return None

if __name__ == "__main__":
    main()
