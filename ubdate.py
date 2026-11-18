import requests
import json
from datetime import datetime

# এখানে আপনার অনুমোদিত ডাটা সোর্স বা এপিআই লিংক বসান
SOURCE_URL = "https://your-authorized-api-or-source.com"

def update_playlist():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(SOURCE_URL, headers=headers, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            
            # ডাটা প্রসেস করে আপনার অ্যাপের ফরম্যাটে সেভ করা
            output = {
                "last_updated": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
                "matches": data
            }
            
            with open("matches.json", "w", encoding="utf-8") as f:
                json.dump(output, f, indent=2, ensure_ascii=False)
            print("Successfully updated matches.json")
        else:
            print(f"Failed to fetch data. Status: {response.status_code}")
            
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    update_playlist()
