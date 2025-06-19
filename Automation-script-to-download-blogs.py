#donwload blogs from links in txt and make zip
import os
from newspaper import Article
import shutil

# List of URLs
urls = [
    "https://levelup.gitconnected.com/artificial-intelligence-is-not-what-you-think-it-is-442395abd9cb",
    "https://medium.com/data-science/engineering-the-future-common-threads-in-data-software-and-artificial-intelligence-2aa46b262150",
    "https://medium.datadriveninvestor.com/how-i-outperformed-the-market-by-130-because-of-artificial-intelligence-7d7a459a0081",
    "https://medium.datadriveninvestor.com/artificial-intelligence-goldman-says-no-65dae6cd9353",
    "https://medium.com/coinmonks/artificial-intelligence-ai-models-for-trading-0bfd308d012d",
    "https://medium.com/ai-ai-oh/the-new-face-of-artificial-intelligence-9c900d463cf9",
    "https://medium.com/@subaj/augmentedreality-and-artificialintelligence-are-bringing-a-new-spot-experience-in-daily-retail-3c4aae147541",
    "https://abajaj033.medium.com/humanities-perspectives-on-artificial-intelligence-a-new-research-initiative-announced-by-neh-2c65995e9f7c",
    "https://digitalexplorermyth.medium.com/ai-tools-for-easing-your-workload-say-goodbye-to-the-grind-3972779784a0",
    "https://medium.com/@sukantkhurana/ai-written-song-on-indian-independence-day-1e51f8f4d5ff",
    "https://medium.com/@withfries2/us-ai-better-together-62ae164f3ff2",
    "https://medium.com/@HerbertRSim/artificial-intelligence-and-the-brain-can-machines-think-58ce4723bab0",
    "https://medium.com/@HerbertRSim/artificial-intelligence-and-the-brain-can-machines-think-58ce4723bab0",
    "https://arsala-khan.medium.com/how-ai-is-quietly-healing-minds-fd010b55a20c",
    "https://medium.com/illumination-curated/does-artificial-intelligence-help-or-hinder-mindfulness-and-growth-of-a-mindset-48a4deb9efbf",
    "https://medium.datadriveninvestor.com/ai-predictions-top-12-artificial-intelligence-trends-for-2024-c30e22e23b9f",
    "https://cryptorookies.medium.com/decentralized-artificial-intelligence-the-trillion-dollar-opportunity-685212af92f7",
    "https://heartbeat.comet.ml/artificial-intelligence-on-mobile-devices-e570fb99a9d4",
    "https://medium.datadriveninvestor.com/5-free-courses-from-harvard-university-to-master-artificial-intelligence-93e9889ac8c9",
    "https://medium.com/machine-cognition/with-artificial-intelligence-philosophy-of-mind-has-become-an-experimental-science-e0b79dc6601a",
    "https://medium.com/technology-hits/the-future-of-work-is-ai-7e893076c817"
]

# Output folder
output_dir = "extracted_blogs"
os.makedirs(output_dir, exist_ok=True)

for i, url in enumerate(urls, 1):
    try:
        article = Article(url)
        article.download()
        article.parse()

        title = article.title or f"blog_{i}"
        content = article.text.strip()

        # Clean filename to avoid invalid characters
        safe_title = "".join(c if c.isalnum() or c in [' ', '_'] else "_" for c in title)
        filename = os.path.join(output_dir, f"blog_{i:02d}_{safe_title[:50].replace(' ', '_')}.txt")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"{title}\n\n{content}")

        print(f"[✔] Saved: {filename}")

    except Exception as e:
        print(f"[✖] Failed to extract from {url}: {e}")

# Create a zip file of the extracted blogs folder
shutil.make_archive(output_dir, 'zip', output_dir)
print(f"[✔] Zip file created: {output_dir}.zip")
