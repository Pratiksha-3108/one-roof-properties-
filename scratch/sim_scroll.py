# Simulate onScrollSync
# section height: 380vh
# window height: say 900px
# totalDistance = 380 * 9 - 900 = 3420 - 900 = 2520px
# Let's inspect what happens across progress 0.0 to 1.0

total_vh = 380
window_h = 900
viewport_w = 1536
node_w = 380
stride = 380
target_center = min(viewport_w * 0.70, viewport_w - node_w * 0.45) # 1536 * 0.7 = 1075.2, 1536 - 171 = 1365 -> 1075.2

print(f"targetCenter: {target_center}")

for p in [0.0, 0.24, 0.48, 0.50, 0.52, 0.70, 0.76, 0.90, 1.0]:
    if p < 0.48:
        sub = p / 0.48
        cat = "Residential"
    elif p < 0.52:
        sub = 0
        cat = "Plotting (trans)"
    else:
        sub = (p - 0.52) / 0.48
        cat = "Plotting"
    
    max_scroll = 2 * stride
    cur_scroll = sub * max_scroll
    train_left = (target_center - node_w / 2) - cur_scroll
    
    c0 = train_left + 0 * stride + node_w / 2
    c1 = train_left + 1 * stride + node_w / 2
    c2 = train_left + 2 * stride + node_w / 2
    
    print(f"p={p:.2f} ({cat}): sub={sub:.2f} | c0={c0:.0f}, c1={c1:.0f}, c2={c2:.0f}")

