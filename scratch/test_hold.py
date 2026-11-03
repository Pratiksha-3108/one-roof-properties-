stride = 380
targetCenter = 680

for normDist in [0.0, -0.1, -0.2, -0.3, -0.4, -0.5, -1.0]:
    dist = normDist * stride
    holdX = abs(dist) * 0.85 if normDist < 0 else 0
    net_offset = dist + holdX
    opacity = max(0, 1.0 - 3.0 * abs(normDist))
    print(f"normDist={normDist:5.2f} | net movement to left={abs(net_offset):5.1f}px | opacity={opacity:4.2f}")

