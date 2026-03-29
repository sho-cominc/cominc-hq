// ══════════════════════════════════════════════════════════════
// CONCEPT 02 — MA-CYLINDER (間)
// The void defines the form. Two lines, text floats in between.
// Letterpress on washi aesthetic. Debossed lines, no ink.
// ══════════════════════════════════════════════════════════════

(async () => {
  const page = figma.currentPage;
  const oldFrame = page.findOne(n => n.name === "02 — MA-Cylinder (間)");
  if (oldFrame) oldFrame.remove();

  // ── Main frame — warm parchment/washi background ──
  const frame = figma.createFrame();
  frame.name = "02 — MA-Cylinder (間)";
  frame.resize(800, 600);
  frame.x = 860;
  frame.y = 0;
  frame.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 0.96, g: 0.94, b: 0.91, a: 1 } },
      { position: 1, color: { r: 0.93, g: 0.91, b: 0.87, a: 1 } }
    ],
    gradientTransform: [[0, 1, 0], [-1, 0, 1]]
  }];
  frame.clipsContent = true;
  page.appendChild(frame);

  // ── Load fonts ──
  await figma.loadFontAsync({ family: "Inter", style: "Light" });
  await figma.loadFontAsync({ family: "Inter", style: "Regular" });
  await figma.loadFontAsync({ family: "Inter", style: "Medium" });
  await figma.loadFontAsync({ family: "Inter", style: "Thin" });

  // ── Constants ──
  const CX = 400;
  const CY = 290;
  const PILLAR_H = 200;
  const GAP = 280; // distance between two vertical lines

  // ══ Subtle texture — faint grid dots (washi hint) ══
  for (let row = 0; row < 12; row++) {
    for (let col = 0; col < 16; col++) {
      const dot = figma.createEllipse();
      dot.name = "texture-dot";
      dot.resize(1, 1);
      dot.x = 50 + col * 50;
      dot.y = 50 + row * 50;
      dot.fills = [{ type: "SOLID", color: { r: 0.82, g: 0.80, b: 0.76, a: 0.3 } }];
      dot.strokes = [];
      frame.appendChild(dot);
    }
  }

  // ══ Left vertical line — with subtle top/bottom ellipse caps ══
  const leftX = CX - GAP / 2;
  const rightX = CX + GAP / 2;
  const topY = CY - PILLAR_H / 2;
  const botY = CY + PILLAR_H / 2;

  function createPillarLine(x) {
    const line = figma.createRectangle();
    line.name = "pillar";
    line.resize(1.5, PILLAR_H);
    line.x = x;
    line.y = topY;
    line.fills = [{
      type: "GRADIENT_LINEAR",
      gradientStops: [
        { position: 0, color: { r: 0.35, g: 0.33, b: 0.30, a: 0.15 } },
        { position: 0.2, color: { r: 0.35, g: 0.33, b: 0.30, a: 0.6 } },
        { position: 0.8, color: { r: 0.35, g: 0.33, b: 0.30, a: 0.6 } },
        { position: 1, color: { r: 0.35, g: 0.33, b: 0.30, a: 0.15 } }
      ],
      gradientTransform: [[0, 1, 0], [-1, 0, 1]]
    }];
    line.strokes = [];
    line.effects = [{
      type: "DROP_SHADOW",
      color: { r: 0.35, g: 0.33, b: 0.30, a: 0.1 },
      offset: { x: 1, y: 1 },
      radius: 2,
      spread: 0,
      visible: true,
      blendMode: "NORMAL"
    }];
    frame.appendChild(line);
  }

  createPillarLine(leftX);
  createPillarLine(rightX);

  // ══ Top ellipse cap (subtle, hinting cylinder top) ══
  function createCap(y, opacity) {
    const cap = figma.createEllipse();
    cap.name = "cylinder-cap";
    cap.resize(GAP + 2, 16);
    cap.x = leftX - 0.5;
    cap.y = y - 8;
    cap.fills = [];
    cap.strokes = [{
      type: "SOLID",
      color: { r: 0.40, g: 0.38, b: 0.35, a: opacity }
    }];
    cap.strokeWeight = 0.75;
    frame.appendChild(cap);
  }

  createCap(topY, 0.25);     // top cap — very subtle
  createCap(botY, 0.18);     // bottom cap — even subtler

  // ══ Horizontal serif lines at top and bottom ══
  function createSerif(y) {
    const serif = figma.createRectangle();
    serif.name = "serif-line";
    serif.resize(GAP + 40, 0.5);
    serif.x = leftX - 20;
    serif.y = y;
    serif.fills = [{ type: "SOLID", color: { r: 0.40, g: 0.38, b: 0.35, a: 0.35 } }];
    serif.strokes = [];
    frame.appendChild(serif);
  }

  createSerif(topY);
  createSerif(botY);

  // ══ Logo text: "ComInc." — centered between pillars ══
  const logo = figma.createText();
  logo.name = "logo-text";
  logo.fontName = { family: "Inter", style: "Light" };
  logo.characters = "ComInc.";
  logo.fontSize = 42;
  logo.letterSpacing = { value: 12, unit: "PIXELS" };
  logo.fills = [{ type: "SOLID", color: { r: 0.25, g: 0.23, b: 0.20 } }];
  logo.textAlignHorizontal = "CENTER";
  // Center between pillars
  logo.x = CX - 120;
  logo.y = CY - 22;
  frame.appendChild(logo);

  // ══ "間" character — large, faint, behind text ══
  const kanji = figma.createText();
  kanji.name = "ma-kanji";
  kanji.fontName = { family: "Inter", style: "Thin" };
  kanji.characters = "間";
  kanji.fontSize = 160;
  kanji.fills = [{ type: "SOLID", color: { r: 0.82, g: 0.80, b: 0.76, a: 0.08 } }];
  kanji.x = CX - 80;
  kanji.y = CY - 95;
  frame.appendChild(kanji);
  // Move behind logo text
  frame.insertChild(frame.children.length - 2, kanji);

  // ══ Tagline — below logo ══
  const tag = figma.createText();
  tag.name = "tagline";
  tag.fontName = { family: "Inter", style: "Regular" };
  tag.characters = "YOUR GUIDE TO JOETSU & MYOKO";
  tag.fontSize = 8;
  tag.letterSpacing = { value: 5, unit: "PIXELS" };
  tag.fills = [{ type: "SOLID", color: { r: 0.50, g: 0.48, b: 0.44 } }];
  tag.x = CX - 105;
  tag.y = CY + 35;
  frame.appendChild(tag);

  // ══ Concept label ══
  const label = figma.createText();
  label.name = "concept-label";
  label.fontName = { family: "Inter", style: "Medium" };
  label.characters = "CONCEPT 02 — MA-CYLINDER (間)";
  label.fontSize = 9;
  label.letterSpacing = { value: 3, unit: "PIXELS" };
  label.fills = [{ type: "SOLID", color: { r: 0.55, g: 0.53, b: 0.50 } }];
  label.x = 40;
  label.y = 30;
  frame.appendChild(label);

  // ══ Description ══
  const desc = figma.createText();
  desc.name = "description";
  desc.fontName = { family: "Inter", style: "Regular" };
  desc.characters = "間 (Ma) \u2014 the void defines the form.\nLetterpress on washi. Lines debossed, no ink. Space is the design.";
  desc.fontSize = 11;
  desc.lineHeight = { value: 20, unit: "PIXELS" };
  desc.fills = [{ type: "SOLID", color: { r: 0.50, g: 0.48, b: 0.44 } }];
  desc.x = 40;
  desc.y = 540;
  frame.appendChild(desc);

  // ══ Print note ══
  const printNote = figma.createText();
  printNote.name = "print-note";
  printNote.fontName = { family: "Inter", style: "Regular" };
  printNote.characters = "PRINT: Blind deboss on 350gsm cotton washi";
  printNote.fontSize = 8;
  printNote.letterSpacing = { value: 2, unit: "PIXELS" };
  printNote.fills = [{ type: "SOLID", color: { r: 0.65, g: 0.63, b: 0.60 } }];
  printNote.x = 570;
  printNote.y = 570;
  frame.appendChild(printNote);

  figma.notify("MA-Cylinder concept refined");
})();
