// ══════════════════════════════════════════════════════════════
// CONCEPT 03 — TORU (透る)
// Wireframe cylinder with transparency overlay
// Top cap vermillion — like a hanko seal
// Silver metallic ink for print
// ══════════════════════════════════════════════════════════════

(async () => {
  const page = figma.currentPage;
  const oldFrame = page.findOne(n => n.name === "03 — Toru (透る)");
  if (oldFrame) oldFrame.remove();

  // ── Main frame — clean white ──
  const frame = figma.createFrame();
  frame.name = "03 — Toru (透る)";
  frame.resize(800, 600);
  frame.x = 0;
  frame.y = 660;
  frame.fills = [{ type: "SOLID", color: { r: 0.98, g: 0.98, b: 0.98 } }];
  frame.clipsContent = true;
  page.appendChild(frame);

  // ── Load fonts ──
  await figma.loadFontAsync({ family: "Inter", style: "Medium" });
  await figma.loadFontAsync({ family: "Inter", style: "Regular" });
  await figma.loadFontAsync({ family: "Inter", style: "Light" });
  await figma.loadFontAsync({ family: "Inter", style: "Semi Bold" });

  // ── Constants ──
  const CX = 400;
  const CY = 285;
  const CYL_W = 180;
  const CYL_H = 200;
  const CAP_H = 45;

  // ══ Shadow on ground ══
  const shadow = figma.createEllipse();
  shadow.name = "ground-shadow";
  shadow.resize(CYL_W + 30, 20);
  shadow.x = CX - (CYL_W + 30) / 2;
  shadow.y = CY + CYL_H / 2 + 15;
  shadow.fills = [{
    type: "GRADIENT_RADIAL",
    gradientStops: [
      { position: 0, color: { r: 0, g: 0, b: 0, a: 0.08 } },
      { position: 1, color: { r: 0, g: 0, b: 0, a: 0 } }
    ],
    gradientTransform: [[1, 0, 0], [0, 1, 0]]
  }];
  shadow.strokes = [];
  frame.appendChild(shadow);

  // ══ Cylinder body — transparent fill with edge highlights ══
  const body = figma.createRectangle();
  body.name = "cylinder-body";
  body.resize(CYL_W, CYL_H);
  body.x = CX - CYL_W / 2;
  body.y = CY - CYL_H / 2;
  body.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 0.75, g: 0.78, b: 0.80, a: 0.08 } },
      { position: 0.15, color: { r: 0.85, g: 0.87, b: 0.89, a: 0.03 } },
      { position: 0.5, color: { r: 0.90, g: 0.92, b: 0.93, a: 0.01 } },
      { position: 0.85, color: { r: 0.85, g: 0.87, b: 0.89, a: 0.03 } },
      { position: 1, color: { r: 0.75, g: 0.78, b: 0.80, a: 0.08 } }
    ],
    gradientTransform: [[1, 0, 0], [0, 1, 0]]
  }];
  body.strokes = [];
  frame.appendChild(body);

  // ══ Left edge highlight ══
  const leftEdge = figma.createRectangle();
  leftEdge.name = "left-edge";
  leftEdge.resize(2, CYL_H);
  leftEdge.x = CX - CYL_W / 2;
  leftEdge.y = CY - CYL_H / 2;
  leftEdge.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 0.55, g: 0.58, b: 0.60, a: 0 } },
      { position: 0.15, color: { r: 0.55, g: 0.58, b: 0.60, a: 0.4 } },
      { position: 0.85, color: { r: 0.55, g: 0.58, b: 0.60, a: 0.4 } },
      { position: 1, color: { r: 0.55, g: 0.58, b: 0.60, a: 0 } }
    ],
    gradientTransform: [[0, 1, 0], [-1, 0, 1]]
  }];
  leftEdge.strokes = [];
  frame.appendChild(leftEdge);

  // ══ Right edge highlight ══
  const rightEdge = figma.createRectangle();
  rightEdge.name = "right-edge";
  rightEdge.resize(2, CYL_H);
  rightEdge.x = CX + CYL_W / 2 - 2;
  rightEdge.y = CY - CYL_H / 2;
  rightEdge.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 0.55, g: 0.58, b: 0.60, a: 0 } },
      { position: 0.15, color: { r: 0.55, g: 0.58, b: 0.60, a: 0.3 } },
      { position: 0.85, color: { r: 0.55, g: 0.58, b: 0.60, a: 0.3 } },
      { position: 1, color: { r: 0.55, g: 0.58, b: 0.60, a: 0 } }
    ],
    gradientTransform: [[0, 1, 0], [-1, 0, 1]]
  }];
  rightEdge.strokes = [];
  frame.appendChild(rightEdge);

  // ══ Vertical wireframe ribs (3 internal) ══
  const ribPositions = [-0.25, 0, 0.25];
  for (const pos of ribPositions) {
    const rib = figma.createRectangle();
    rib.name = "wireframe-rib";
    rib.resize(0.75, CYL_H);
    rib.x = CX + pos * CYL_W * 0.8;
    rib.y = CY - CYL_H / 2;
    rib.fills = [{
      type: "GRADIENT_LINEAR",
      gradientStops: [
        { position: 0, color: { r: 0.6, g: 0.63, b: 0.65, a: 0 } },
        { position: 0.2, color: { r: 0.6, g: 0.63, b: 0.65, a: 0.12 } },
        { position: 0.8, color: { r: 0.6, g: 0.63, b: 0.65, a: 0.12 } },
        { position: 1, color: { r: 0.6, g: 0.63, b: 0.65, a: 0 } }
      ],
      gradientTransform: [[0, 1, 0], [-1, 0, 1]]
    }];
    rib.strokes = [];
    frame.appendChild(rib);
  }

  // ══ Top cap — VERMILLION (hanko seal style) ══
  const topCap = figma.createEllipse();
  topCap.name = "top-cap-vermillion";
  topCap.resize(CYL_W, CAP_H);
  topCap.x = CX - CYL_W / 2;
  topCap.y = CY - CYL_H / 2 - CAP_H / 2;
  topCap.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 0.78, g: 0.18, b: 0.10, a: 0.85 } },
      { position: 0.4, color: { r: 0.88, g: 0.25, b: 0.12, a: 0.92 } },
      { position: 0.6, color: { r: 0.92, g: 0.30, b: 0.15, a: 0.95 } },
      { position: 1, color: { r: 0.80, g: 0.20, b: 0.10, a: 0.88 } }
    ],
    gradientTransform: [[1, 0, 0], [0, 1, 0]]
  }];
  topCap.strokes = [];
  topCap.effects = [{
    type: "DROP_SHADOW",
    color: { r: 0.85, g: 0.25, b: 0.12, a: 0.2 },
    offset: { x: 0, y: 4 },
    radius: 16,
    spread: 0,
    visible: true,
    blendMode: "NORMAL"
  }];
  frame.appendChild(topCap);

  // ══ Top cap inner shine ══
  const topShine = figma.createEllipse();
  topShine.name = "top-cap-shine";
  topShine.resize(CYL_W * 0.6, CAP_H * 0.35);
  topShine.x = CX - CYL_W * 0.3;
  topShine.y = CY - CYL_H / 2 - CAP_H / 2 + CAP_H * 0.15;
  topShine.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 1, g: 1, b: 1, a: 0.3 } },
      { position: 1, color: { r: 1, g: 1, b: 1, a: 0 } }
    ],
    gradientTransform: [[0, 1, 0], [-1, 0, 1]]
  }];
  topShine.strokes = [];
  frame.appendChild(topShine);

  // ══ Bottom cap — silver outline only ══
  const botCap = figma.createEllipse();
  botCap.name = "bottom-cap";
  botCap.resize(CYL_W, CAP_H);
  botCap.x = CX - CYL_W / 2;
  botCap.y = CY + CYL_H / 2 - CAP_H / 2;
  botCap.fills = [];
  botCap.strokes = [{
    type: "SOLID",
    color: { r: 0.65, g: 0.68, b: 0.70, a: 0.4 }
  }];
  botCap.strokeWeight = 1;
  frame.appendChild(botCap);

  // ══ Logo text: "ComInc." — on the cylinder surface ══
  const logo = figma.createText();
  logo.name = "logo-text";
  logo.fontName = { family: "Inter", style: "Semi Bold" };
  logo.characters = "ComInc.";
  logo.fontSize = 36;
  logo.letterSpacing = { value: 4, unit: "PIXELS" };
  logo.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 0.25, g: 0.25, b: 0.28, a: 0.7 } },
      { position: 0.5, color: { r: 0.20, g: 0.20, b: 0.22, a: 0.85 } },
      { position: 1, color: { r: 0.25, g: 0.25, b: 0.28, a: 0.7 } }
    ],
    gradientTransform: [[1, 0, 0], [0, 1, 0]]
  }];
  logo.textAlignHorizontal = "CENTER";
  logo.x = CX - 88;
  logo.y = CY - 18;
  frame.appendChild(logo);

  // ══ Tagline ══
  const tag = figma.createText();
  tag.name = "tagline";
  tag.fontName = { family: "Inter", style: "Light" };
  tag.characters = "YOUR GUIDE TO JOETSU & MYOKO";
  tag.fontSize = 8;
  tag.letterSpacing = { value: 4, unit: "PIXELS" };
  tag.fills = [{ type: "SOLID", color: { r: 0.55, g: 0.55, b: 0.58 } }];
  tag.x = CX - 100;
  tag.y = CY + 28;
  frame.appendChild(tag);

  // ══ Concept label ══
  const label = figma.createText();
  label.name = "concept-label";
  label.fontName = { family: "Inter", style: "Medium" };
  label.characters = "CONCEPT 03 — TORU (透る)";
  label.fontSize = 9;
  label.letterSpacing = { value: 3, unit: "PIXELS" };
  label.fills = [{ type: "SOLID", color: { r: 0.55, g: 0.55, b: 0.58 } }];
  label.x = 40;
  label.y = 30;
  frame.appendChild(label);

  // ══ Description ══
  const desc = figma.createText();
  desc.name = "description";
  desc.fontName = { family: "Inter", style: "Regular" };
  desc.characters = "Wireframe cylinder with transparency overlay.\nTop cap vermillion — like a hanko seal. Silver metallic ink for print.";
  desc.fontSize = 11;
  desc.lineHeight = { value: 20, unit: "PIXELS" };
  desc.fills = [{ type: "SOLID", color: { r: 0.50, g: 0.50, b: 0.53 } }];
  desc.x = 40;
  desc.y = 540;
  frame.appendChild(desc);

  // ══ Print spec ══
  const printSpec = figma.createText();
  printSpec.name = "print-spec";
  printSpec.fontName = { family: "Inter", style: "Regular" };
  printSpec.characters = "PRINT: Silver metallic + vermillion spot color on uncoated stock";
  printSpec.fontSize = 8;
  printSpec.letterSpacing = { value: 2, unit: "PIXELS" };
  printSpec.fills = [{ type: "SOLID", color: { r: 0.65, g: 0.65, b: 0.68 } }];
  printSpec.x = 420;
  printSpec.y = 570;
  frame.appendChild(printSpec);

  figma.notify("Toru concept refined");
})();
