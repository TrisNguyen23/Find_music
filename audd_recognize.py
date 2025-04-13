import requests

API_TOKEN = "360af03566632305d850a3d901628082"
API_URL = "https://api.audd.io/"

def recognize_song(file_path: str):
    data = {
        'api_token': API_TOKEN,
        'return': 'apple_music,spotify'
    }
    files = {
        'file': open(file_path, 'rb')
    }
    print("Đang gửi file lên AudD để nhận dạng...")
    resp = requests.post(API_URL, data=data, files=files)
    result = resp.json()
    if result.get("status") == "success" and result.get("result"):
        song = result["result"]
        print(f"🎵 Tìm thấy: {song['title']} – {song['artist']}")
        print(f"Link Spotify: {song['spotify']['external_urls']['spotify']}")
    else:
        print("Không tìm thấy bài hát nào khớp.")

if __name__ == "__main__":
    recognize_song("query.wav")
