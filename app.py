from flask import Flask
from flask import Response
from flask import Flask, render_template, request,flash
import requests

app = Flask(__name__)
YOUTUBE_API_KEY='AIzaSyBElcB_NePouOTp_pBZDvJ6Y_a6umwALN0'

def get_video_title(video_id):
    """Fetch video title using YouTube Data API"""
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "items" in data and len(data["items"]) > 0:
        return data["items"][0]["snippet"]["title"]
    return "Unknown Title"

@app.route('/video/<video_id>')
def handle_video(video_id):
    title = get_video_title(video_id)
    from TextSim import compute_tfidf_score

    sc=compute_tfidf_score(title)
    print(f"✅ Debug: sc={sc}, video_id={video_id}, title={title}")
    return render_template("reshome.html",  sc=sc,  video_id=str(video_id), title=title)
    
    

@app.route("/sentiment",methods =["GET", "POST"])
def sentiment():

        vid = request.form.get("vid")
        
        from youtube import get_video_data
        data=get_video_data(vid)
        comments=data[2]


        from sentiment import analyze_sentiments
        res=analyze_sentiments(comments)
        data = zip(comments, res)

        from Graph import generate
        graph=generate(res)



        
        return render_template("viewres.html", data=data, graph=graph,)
        

if __name__ == '__main__':
    app.run(debug=True)
