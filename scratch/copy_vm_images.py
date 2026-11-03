import shutil, os

vision_src = r'C:\Users\Admin\.gemini\antigravity\brain\6ea31858-5b2b-44bd-ac91-9f917ce239ee\.user_uploaded\media_1793688771878_89396b92.jpg'
mission_src = r'C:\Users\Admin\.gemini\antigravity\brain\6ea31858-5b2b-44bd-ac91-9f917ce239ee\.user_uploaded\media_1793688767513_1b67df2d.jpg'

vision_dst = r'assets\about-vision.jpg'
mission_dst = r'assets\about-mission.jpg'

shutil.copyfile(vision_src, vision_dst)
shutil.copyfile(mission_src, mission_dst)

print(f"Copied vision to {vision_dst}, size: {os.path.getsize(vision_dst)}")
print(f"Copied mission to {mission_dst}, size: {os.path.getsize(mission_dst)}")

