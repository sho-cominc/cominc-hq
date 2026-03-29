// ══════════════════════════════════════════════════════════════
// CONCEPT 01 — STACK
// Cylinder deconstructed into 3 floating gradient slices
// Sho's favorite — favicon champion, works at any size
// ══════════════════════════════════════════════════════════════

(async () => {
  const page = figma.currentPage;
  const oldFrame = page.findOne(n => n.name === "01 — Stack");
  if (oldFrame) oldFrame.remove();

  // ── Main frame ──
  const frame = figma.createFrame();
  frame.name = "01 — Stack";
  frame.resize(800, 600);
  frame.x = 0;
  frame.y = 0;
  frame.fills = [{ type: "SOLID", color: { r: 0.06, g: 0.06, b: 0.08 } }];
  frame.clipsContent = true;
  page.appendChild(frame);

  // ── Load fonts ──
  await figma.loadFontAsync({ family: "Inter", style: "Bold" });
  await figma.loadFontAsync({ family: "Inter", style: "Light" });
  await figma.loadFontAsync({ family: "Inter", style: "Regular" });
  await figma.loadFontAsync({ family: "Inter", style: "Medium" });

  // ── Constants ──
  const CX = 240;  // center x of icon cluster
  const CY = 265;  // center y of icon cluster

  // ══ Background ambient glow ══
  const ambientGlow = figma.createEllipse();
  ambientGlow.name = "ambient-glow";
  ambientGlow.resize(300, 200);
  ambientGlow.x = CX - 150;
  ambientGlow.y = CY - 100;
  ambientGlow.fills = [{
    type: "GRADIENT_RADIAL",
    gradientStops: [
      { position: 0, color: { r: 0.15, g: 0.55, b: 0.50, a: 0.08 } },
      { position: 0.6, color: { r: 0.10, g: 0.35, b: 0.30, a: 0.03 } },
      { position: 1, color: { r: 0, g: 0, b: 0, a: 0 } }
    ],
    gradientTransform: [[1, 0, 0], [0, 1, 0]]
  }];
  ambientGlow.strokes = [];
  frame.appendChild(ambientGlow);

  // ══ Helper: create a refined gradient slice ══
  function createSlice(name, y, w, h, c1, c2, glowColor, shadowY) {
    // Main ellipse
    const e = figma.createEllipse();
    e.name = name;
    e.resize(w, h);
    e.x = CX - w / 2;
    e.y = y;
    e.fills = [{
      type: "GRADIENT_LINEAR",
      gradientStops: [
        { position: 0, color: { ...c1, a: 0.95 } },
        { position: 0.5, color: { ...c2, a: 1.0 } },
        { position: 1, color: { ...c1, a: 0.85 } }
      ],
      gradientTransform: [[1, 0, 0], [0, 1, 0]]
    }];
    e.strokes = [{
      type: "SOLID",
      color: { ...c2, a: 0.3 }
    }];
    e.strokeWeight = 0.5;
    e.effects = [
      {
        type: "DROP_SHADOW",
        color: { r: 0, g: 0, b: 0, a: 0.4 },
        offset: { x: 0, y: shadowY },
        radius: 16,
        spread: 0,
        visible: true,
        blendMode: "NORMAL"
      },
      {
        type: "DROP_SHADOW",
        color: { ...glowColor, a: 0.2 },
        offset: { x: 0, y: 0 },
        radius: 20,
        spread: 2,
        visible: true,
        blendMode: "NORMAL"
      }
    ];
    frame.appendChild(e);

    // Highlight — inner shine on top half
    const shine = figma.createEllipse();
    shine.name = name + "-shine";
    shine.resize(w * 0.6, h * 0.4);
    shine.x = CX - (w * 0.6) / 2;
    shine.y = y + h * 0.1;
    shine.fills = [{
      type: "GRADIENT_LINEAR",
      gradientStops: [
        { position: 0, color: { r: 1, g: 1, b: 1, a: 0.25 } },
        { position: 1, color: { r: 1, g: 1, b: 1, a: 0 } }
      ],
      gradientTransform: [[0, 1, 0], [-1, 0, 1]]
    }];
    shine.strokes = [];
    frame.appendChild(shine);

    return e;
  }

  // ══ Three slices ══
  // Top — vermillion / coral
  createSlice("slice-top", 190, 100, 28,
    { r: 0.82, g: 0.22, b: 0.12 },
    { r: 0.95, g: 0.35, b: 0.18 },
    { r: 0.9, g: 0.3, b: 0.15 },
    3
  );

  // Middle — teal / emerald (largest)
  createSlice("slice-mid", 240, 130, 34,
    { r: 0.12, g: 0.58, b: 0.50 },
    { r: 0.18, g: 0.72, b: 0.58 },
    { r: 0.15, g: 0.65, b: 0.55 },
    5
  );

  // Bottom — silver / cool grey
  createSlice("slice-bottom", 296, 105, 26,
    { r: 0.50, g: 0.54, b: 0.58 },
    { r: 0.72, g: 0.75, b: 0.78 },
    { r: 0.6, g: 0.63, b: 0.67 },
    4
  );

  // ══ Connecting lines (subtle vertical guides hinting cylinder form) ══
  for (const xOff of [-42, 42]) {
    const line = figma.createRectangle();
    line.name = "guide-line";
    line.resize(0.5, 90);
    line.x = CX + xOff;
    line.y = 210;
    line.fills = [{
      type: "GRADIENT_LINEAR",
      gradientStops: [
        { position: 0, color: { r: 1, g: 1, b: 1, a: 0 } },
        { position: 0.3, color: { r: 1, g: 1, b: 1, a: 0.06 } },
        { position: 0.7, color: { r: 1, g: 1, b: 1, a: 0.06 } },
        { position: 1, color: { r: 1, g: 1, b: 1, a: 0 } }
      ],
      gradientTransform: [[0, 1, 0], [-1, 0, 1]]
    }];
    line.strokes = [];
    frame.appendChild(line);
  }

  // ══ Logo text: "ComInc." ══
  const logo = figma.createText();
  logo.name = "logo-text";
  logo.fontName = { family: "Inter", style: "Bold" };
  logo.characters = "ComInc.";
  logo.fontSize = 48;
  logo.letterSpacing = { value: 6, unit: "PIXELS" };
  logo.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 0.92, g: 0.92, b: 0.93, a: 1 } },
      { position: 1, color: { r: 0.78, g: 0.80, b: 0.82, a: 1 } }
    ],
    gradientTransform: [[0, 1, 0], [-1, 0, 1]]
  }];
  logo.x = 370;
  logo.y = 238;
  frame.appendChild(logo);

  // ══ Tagline ══
  const tag = figma.createText();
  tag.name = "tagline";
  tag.fontName = { family: "Inter", style: "Light" };
  tag.characters = "YOUR GUIDE TO JOETSU & MYOKO";
  tag.fontSize = 9;
  tag.letterSpacing = { value: 4, unit: "PIXELS" };
  tag.fills = [{ type: "SOLID", color: { r: 0.40, g: 0.42, b: 0.45 } }];
  tag.x = 373;
  tag.y = 298;
  frame.appendChild(tag);

  // ══ Concept label ══
  const label = figma.createText();
  label.name = "concept-label";
  label.fontName = { family: "Inter", style: "Medium" };
  label.characters = "CONCEPT 01 — STACK";
  label.fontSize = 9;
  label.letterSpacing = { value: 3, unit: "PIXELS" };
  label.fills = [{ type: "SOLID", color: { r: 0.30, g: 0.32, b: 0.35 } }];
  label.x = 40;
  label.y = 30;
  frame.appendChild(label);

  // ══ Description ══
  const desc = figma.createText();
  desc.name = "description";
  desc.fontName = { family: "Inter", style: "Regular" };
  desc.characters = "Cylinder deconstructed into 3 floating slices.\nMinimal. Scalable. Favicon to billboard.";
  desc.fontSize = 11;
  desc.lineHeight = { value: 20, unit: "PIXELS" };
  desc.fills = [{ type: "SOLID", color: { r: 0.35, g: 0.37, b: 0.40 } }];
  desc.x = 40;
  desc.y = 540;
  frame.appendChild(desc);

  // ══ Favicon preview (48x48) ══
  const fav = figma.createFrame();
  fav.name = "favicon-preview";
  fav.resize(48, 48);
  fav.x = 710;
  fav.y = 30;
  fav.fills = [{ type: "SOLID", color: { r: 0.10, g: 0.10, b: 0.12 } }];
  fav.cornerRadius = 10;
  fav.effects = [{
    type: "DROP_SHADOW",
    color: { r: 0, g: 0, b: 0, a: 0.3 },
    offset: { x: 0, y: 2 },
    radius: 8,
    spread: 0,
    visible: true,
    blendMode: "NORMAL"
  }];
  frame.appendChild(fav);

  function miniSlice(parent, name, y, w, h, color) {
    const e = figma.createEllipse();
    e.name = name;
    e.resize(w, h);
    e.x = 24 - w / 2;
    e.y = y;
    e.fills = [{ type: "SOLID", color }];
    e.strokes = [];
    parent.appendChild(e);
  }
  miniSlice(fav, "fav-top", 12, 18, 6, { r: 0.90, g: 0.30, b: 0.15 });
  miniSlice(fav, "fav-mid", 20, 22, 7, { r: 0.18, g: 0.68, b: 0.55 });
  miniSlice(fav, "fav-bot", 29, 18, 5, { r: 0.65, g: 0.68, b: 0.72 });

  // ══ Dark/Light variant labels ══
  const varLabel = figma.createText();
  varLabel.name = "variant-label";
  varLabel.fontName = { family: "Inter", style: "Regular" };
  varLabel.characters = "Dark mode";
  varLabel.fontSize = 8;
  varLabel.letterSpacing = { value: 1, unit: "PIXELS" };
  varLabel.fills = [{ type: "SOLID", color: { r: 0.30, g: 0.32, b: 0.35 } }];
  varLabel.x = 714;
  varLabel.y = 84;
  frame.appendChild(varLabel);

  figma.notify("Stack concept refined");
})();
