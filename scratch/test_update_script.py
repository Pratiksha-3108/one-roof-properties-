file_path = r'd:\DTG\One-Roof-Properties\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Check target strings
old_train_positions = """      function updateTrainPositions(train, nodes, subProgress, targetCenter) {
        if (!train || nodes.length === 0) return;

        const firstNode = nodes[0];
        const nodeWidth = firstNode.offsetWidth || 560;
        const stride = nodeWidth; // Tangent outer rings touch edge-to-edge
        const totalProjects = nodes.length;

        const maxScrollDist = (totalProjects - 1) * stride;
        const currentScroll = subProgress * maxScrollDist;
        const trainLeft = (targetCenter - nodeWidth / 2) - currentScroll;

        train.style.transform = `translate3d(${trainLeft}px, -50%, 0)`;

        nodes.forEach((node, i) => {
          const nodeCenter = trainLeft + i * stride + nodeWidth / 2;
          const dist = nodeCenter - targetCenter;
          const normDist = dist / stride; // negative if moved left, positive if on right

          const portal = node.querySelector('.sr-node-portal');
          const overlay = node.querySelector('.sr-node-overlay');

          if (portal) {
            let scale = 1.0;
            if (normDist < 0) {
              // Scrolled past to the left: inner image circle shrinks to SMALL (down to 0.30)
              scale = Math.max(0.30, 1.0 - 0.70 * Math.abs(normDist));
            } else {
              // Coming from the right: starts medium-big (~0.85) and expands to 1.0
              scale = Math.max(0.85, 1.0 - 0.15 * normDist);
            }
            portal.style.transform = `translate(-50%, -50%) scale(${scale.toFixed(3)})`;

            // When circle shrinks into small circle, fade out the overlay text smoothly
            if (overlay) {
              if (scale < 0.75) {
                const overlayOpacity = Math.max(0, (scale - 0.40) / 0.35);
                overlay.style.opacity = overlayOpacity.toFixed(2);
                overlay.style.pointerEvents = overlayOpacity > 0.3 ? 'auto' : 'none';
              } else {
                overlay.style.opacity = '1';
                overlay.style.pointerEvents = 'auto';
              }
            }
          }
        });
      }"""

new_train_positions = """      function updateTrainPositions(train, nodes, subProgress, targetCenter) {
        if (!train || nodes.length === 0) return;

        const firstNode = nodes[0];
        const nodeWidth = firstNode.offsetWidth || 380;
        const stride = nodeWidth; // Clean card stride
        const totalProjects = nodes.length;

        const maxScrollDist = (totalProjects - 1) * stride;
        const currentScroll = subProgress * maxScrollDist;
        const trainLeft = (targetCenter - nodeWidth / 2) - currentScroll;

        train.style.transform = `translate3d(${trainLeft}px, -50%, 0)`;

        nodes.forEach((node, i) => {
          const nodeCenter = trainLeft + i * stride + nodeWidth / 2;
          const dist = nodeCenter - targetCenter;
          const normDist = dist / stride; // negative if moved left, positive if on right

          const portal = node.querySelector('.sr-node-portal');
          const overlay = node.querySelector('.sr-node-overlay');

          // Keep full arched window proportions (no miniature shrink)
          let scale = 1.0;
          if (normDist > 0) {
            // Subtle natural depth for incoming cards from right
            scale = Math.max(0.96, 1.0 - 0.04 * Math.min(normDist, 2));
          } else {
            scale = 1.0;
          }

          if (portal) {
            portal.style.transform = `translate(-50%, -50%) scale(${scale.toFixed(3)})`;
          }

          // Smoothly fade out card only as it exits past active position into left margin
          if (normDist < 0) {
            const exitOpacity = Math.max(0, 1.0 - 1.25 * Math.abs(normDist));
            node.style.opacity = exitOpacity.toFixed(2);
            node.style.pointerEvents = exitOpacity > 0.3 ? 'auto' : 'none';
          } else {
            node.style.opacity = '1';
            node.style.pointerEvents = 'auto';
          }

          if (overlay) {
            overlay.style.opacity = '1';
            overlay.style.pointerEvents = 'auto';
          }
        });
      }"""

assert old_train_positions in html, "old_train_positions not found"
html = html.replace(old_train_positions, new_train_positions)
print("Replaced updateTrainPositions successfully")

old_target_center = """        const viewportWidth = window.innerWidth;
        const firstNode = resNodes[0] || plotNodes[0];
        const nodeWidth = firstNode ? firstNode.offsetWidth : 560;
        // Position of active project: anchored on the right side of the screen
        const targetCenter = Math.min(viewportWidth * 0.70, viewportWidth - nodeWidth * 0.45);"""

new_target_center = """        const viewportWidth = window.innerWidth;
        const firstNode = resNodes[0] || plotNodes[0];
        const nodeWidth = firstNode ? firstNode.offsetWidth : 380;
        
        // Position active card cleanly right next to brand text block (where small image was, no awkward gap)
        const stageCenter = section.querySelector('.sr-stage-center');
        const brandBlock = section.querySelector('.sr-brand-block');
        let targetCenter;
        if (stageCenter && brandBlock) {
          const brandRect = brandBlock.getBoundingClientRect();
          const stageRect = stageCenter.getBoundingClientRect();
          const brandRightInStage = brandRect.right - stageRect.left;
          targetCenter = brandRightInStage + 28 + (nodeWidth / 2);
        } else {
          targetCenter = Math.min(viewportWidth * 0.48, viewportWidth - nodeWidth * 0.52);
        }"""

assert old_target_center in html, "old_target_center not found"
html = html.replace(old_target_center, new_target_center)
print("Replaced targetCenter successfully")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("ALL CHANGES SAVED TO index.html")

