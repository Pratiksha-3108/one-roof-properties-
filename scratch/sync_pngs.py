import shutil, os

pairs = [
    ('assets/service-selling-properties-plots.jpg', 'assets/service1.png'),
    ('assets/service-reselling-purchasing.jpg', 'assets/service2.png'),
    ('assets/service-construction-projects.jpg', 'assets/service3.png'),
    ('assets/service-investment-projects.jpg', 'assets/service4.png'),
    ('assets/service-redevelopment-projects.jpg', 'assets/service5.png'),
    ('assets/service-engineer-contractor.jpg', 'assets/service6.png'),
]

for src, dst in pairs:
    shutil.copyfile(src, dst)
    print(f'Synced {src} -> {dst}')

