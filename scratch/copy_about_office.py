import shutil, os

src = r'C:\Users\Admin\.gemini\antigravity\brain\6ea31858-5b2b-44bd-ac91-9f917ce239ee\.user_uploaded\media_1793689910901_f36660e6.jpg'
dst1 = r'assets\one-roof-office-about.jpg'
dst2 = r'assets\about-office.jpg'

shutil.copyfile(src, dst1)
shutil.copyfile(src, dst2)

print(f"Copied to {dst1}, size: {os.path.getsize(dst1)}")
print(f"Copied to {dst2}, size: {os.path.getsize(dst2)}")

