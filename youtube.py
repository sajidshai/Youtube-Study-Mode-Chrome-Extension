

#Create a project on Google Cloud Console.
#Enable the YouTube Data API v3 for your project.
#Generate an API key.

from googleapiclient.discovery import build

# Replace with your API key
api_key = 'AIzaSyBElcB_NePouOTp_pBZDvJ6Y_a6umwALN0'

# Build a service object for the API

youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_comments(video_id):

    comments = []
    next_page_token = None

    while True:
        # Request for video comments
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            pageToken=next_page_token,
            maxResults=50,  # You can adjust the number of results per request
            textFormat="plainText"
        )
        response = request.execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)

        next_page_token = response.get('nextPageToken')

        if not next_page_token:
            break

    return comments

# Replace with the ID of the video you want to get comments from
def get_video_data(video_id):
    

    video_response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()

    video_title = video_response['items'][0]['snippet']['title']
    video_thumbnail = video_response['items'][0]['snippet']['thumbnails']['high']['url']

    print(f"Title: {video_title}")
    print(f"Thumbnail: {video_thumbnail}")



    # Fetch comments
    comments = get_video_comments(video_id)

    # Print comments
    comments_list=[]

    for i, comment in enumerate(comments, start=1):
        #print(f"{i}: {comment}")
        comments_list.append(comment)

    return video_title, video_thumbnail, comments_list[:50]


if __name__ == '__main__':
    video_id = 'NcCYq3bvlJM'
    print(get_video_data(video_id))