import random
import streamlit as st
from yt_extractor import get_info
import db_service as dbs


@st.cache(allow_output_mutation=True)
def get_videos():
    return dbs.get_all_videos()

def get_duration_text(duration_s):
    seconds = duration_s % 60
    minutes = int((duration_s / 60) % 60)
    hours = int((duration_s / (60*60)) % 24)
    text = ''
    if hours > 0:
        text += f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        text += f'{minutes:02d}:{seconds:02d}'
    return text

st.title("Watch Later APP")

menu_options = ("Today's video", "All videos", "Add a new video")
selection = st.sidebar.selectbox("Menu", menu_options)

if selection == "All videos":
    st.markdown(f"## All videos")
    
    videos = get_videos()
    # st.text(videos)
    if not videos:
        st.text("No videos in Database!")
    else:
        for vid in videos:
            url = "https://youtu.be/" + vid["video_id"]
            st.text(vid['title'])
            st.text(f"{vid['channel']} - {get_duration_text(vid['duration'])}")           
            # st.text(f"Description: {vid['description']}")
            # st.text(f"Views: {vid['view_count']}")
            # st.text(f"Likes: {vid['like_count']}")
            # if vid['tags'] is not None:
            #     st.text(f"Tags: {vid['tags']}")
            # if vid['categories'] is not None:
            #     st.text(f"Categories: {vid['categories']}")
            # st.text(vid)
            
            ok = st.button('Delete video', key=vid["video_id"])
            if ok:
                dbs.delete_video(vid["video_id"])
                st.legacy_caching.clear_cache()
                st.experimental_rerun()

            st.video(url)
        
elif selection == "Add a new video":
    st.markdown(f"## Add a video")
    
    url = st.text_input('Please enter the video url')
    if url:
        video_data = get_info(url)
        if video_data is None:
            st.text("Could not find video")
        else:
            st.text(video_data['title'])
            st.text(video_data['channel'])
            st.video(url)
            if st.button("Add video"):
                dbs.insert_video(video_data)
                st.text("Added video!")
                st.legacy_caching.clear_cache()
                
else:
    st.markdown(f"## Today's video")
    
    videos = get_videos()
    if not videos:
        st.text("No videos in Database!")
    else:
        vid = dbs.get_video_today()
        
        if not vid:
            # not yet defined
            videos = get_videos()
            n = len(videos)
            idx = random.randint(0, n-1)
            vid = videos[idx]
            dbs.update_video_today(vid, insert=True)
        else:
            # first item in list
            vid = vid[0]
        
        if st.button("Choose another video"):
            videos = get_videos()
            n = len(videos)
            if n > 1:
                idx = random.randint(0, n-1)
                vid_new = videos[idx]
                while vid_new['video_id'] == vid['video_id']:
                    idx = random.randint(0, n-1)
                    vid_new = videos[idx]
                vid = vid_new
                dbs.update_video_today(vid)
        
        url = "https://youtu.be/" + vid["video_id"]
        st.text(vid['title'])
        st.text(f"{vid['channel']} - {get_duration_text(vid['duration'])}")
        st.video(url)
