import os

images = [
    'assets/service-selling-properties-plots.jpg',
    'assets/service-reselling-purchasing.jpg',
    'assets/service-construction-projects.jpg',
    'assets/service-investment-projects.jpg',
    'assets/service-redevelopment-projects.jpg',
    'assets/service-engineer-contractor.jpg'
]

for img in images:
    exists = os.path.exists(img)
    size = os.path.getsize(img) if exists else 0
    print(f'{img}: exists={exists}, size={size}')

