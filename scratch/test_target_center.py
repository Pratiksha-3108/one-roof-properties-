screens = [1920, 1536, 1440, 1280, 1024]

for w in screens:
    # brandBlock width: clamp(380px, 36vw, 560px)
    bw = max(380, min(560, w * 0.36))
    # padding of wrapper: clamp(24px, 4.5vw, 64px)
    pad = max(24, min(64, w * 0.045))
    # nodeWidth: clamp(340px, 30vw, 430px)
    nw = max(340, min(430, w * 0.30))
    # portalWidth: clamp(280px, 24vw, 350px)
    pw = max(280, min(350, w * 0.24))
    
    brand_right = bw # inside stageCenter, brandBlock is first child
    target_center = brand_right + 28 + nw / 2
    card0_left = target_center - nw / 2
    card0_portal_left = card0_left + (nw - pw) / 2
    gap_from_text = card0_portal_left - brand_right
    card0_portal_right = card0_portal_left + pw
    
    # second card
    card1_portal_left = card0_portal_left + nw
    card1_portal_right = card1_portal_left + pw
    
    # third card
    card2_portal_left = card1_portal_left + nw
    
    print(f"Screen {w}px:")
    print(f"  Brand block: 0 to {brand_right:.0f}px (width: {bw:.0f}px)")
    print(f"  Gap to portal: {gap_from_text:.0f}px")
    print(f"  Card 0 portal: {card0_portal_left:.0f}px - {card0_portal_right:.0f}px")
    print(f"  Card 1 portal: {card1_portal_left:.0f}px - {card1_portal_right:.0f}px")
    print(f"  Card 2 portal: {card2_portal_left:.0f}px (starts at)")
    print(f"  Stage width approx: {w - pad*2:.0f}px")
    print()

