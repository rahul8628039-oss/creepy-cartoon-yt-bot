import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

def upload():
    creds = Credentials(
        None,
        refresh_token=os.environ["YT_REFRESH_TOKEN"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.environ["YT_CLIENT_ID"],
        client_secret=os.environ["YT_CLIENT_SECRET"],
        scopes=["https://www.googleapis.com/auth/youtube.upload"]
    )

    youtube = build("youtube", "v3", credentials=creds)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": os.environ.get("DEFAULT_TITLE", "Creepy Cartoon Story"),
                "description": os.environ.get("DEFAULT_DESCRIPTION", "Auto-generated horror cartoon"),
                "tags": os.environ.get("DEFAULT_TAGS", "creepy,cartoon,horror").split(","),
                "categoryId": "24"
            },
            "status": {"privacyStatus": "public"}
        },
        media_body=MediaFileUpload("outputs/video.mp4")
    )

    response = request.execute()
    print("Uploaded:", response["id"])


if __name__ == "__main__":
    upload()
