// ══════════════════════════════════════════════════════════════
// CONCEPT 04 — GLASS TOWER
// Literal 3D transparent glass cylinder
// Spot UV on matte card — glossy cylinder catches light
// ══════════════════════════════════════════════════════════════

(async () => {
  const page = figma.currentPage;
  const oldFrame = page.findOne(n => n.name === "04 — Glass Tower");
  if (oldFrame) oldFrame.remove();

  // ── Main frame — deep dark background ──
  const frame = figma.createFrame();
  frame.name = "04 — Glass Tower";
  frame.resize(800, 600);
  frame.x = 860;
  frame.y = 660;
  frame.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 0.04, g: 0.04, b: 0.06, a: 1 } },
      { position: 1, color: { r: 0.08, g: 0.08, b: 0.10, a: 1 } }
    ],
    gradientTransform: [[0, 1, 0], [-1, 0, 1]]
  }];
  frame.clipsContent = true;
  page.appendChild(frame);

  // ── Load fonts ──
  await figma.loadFontAsync({ family: "Inter", style: "Bold" });
  await figma.loadFontAsync({ family: "Inter", style: "Regular" });
  await figma.loadFontAsync({ family: "Inter", style: "Medium" });
  await figma.loadFontAsync({ family: "Inter", style: "Light" });

  // ── Constants ──
  const CX = 400;
  const CY = 280;
  const CYL_W = 160;
  const CYL_H = 220;
  const CAP_H = 40;

  // ══ Background light source (top-left glow) ══
  const lightSource = figma.createEllipse();
  lightSource.name = "light-source";
  lightSource.resize(400, 400);
  lightSource.x = CX - 320;
  lightSource.y = CY - 350;
  lightSource.fills = [{
    type: "GRADIENT_RADIAL",
    gradientStops: [
      { position: 0, color: { r: 0.3, g: 0.35, b: 0.45, a: 0.06 } },
      { position: 1, color: { r: 0, g: 0, b: 0, a: 0 } }
    ],
    gradientTransform: [[1, 0, 0], [0, 1, 0]]
  }];
  lightSource.strokes = [];
  frame.appendChild(lightSource);

  // ══ Ground reflection ══
  const groundReflection = figma.createEllipse();
  groundReflection.name = "ground-reflection";
  groundReflection.resize(CYL_W + 80, 30);
  groundReflection.x = CX - (CYL_W + 80) / 2;
  groundReflection.y = CY + CYL_H / 2 + 20;
  groundReflection.fills = [{
    type: "GRADIENT_RADIAL",
    gradientStops: [
      { position: 0, color: { r: 0.25, g: 0.30, b: 0.40, a: 0.12 } },
      { position: 0.5, color: { r: 0.15, g: 0.18, b: 0.25, a: 0.06 } },
      { position: 1, color: { r: 0, g: 0, b: 0, a: 0 } }
    ],
    gradientTransform: [[1, 0, 0], [0, 1, 0]]
  }];
  groundReflection.strokes = [];
  frame.appendChild(groundReflection);

  // ══ Cylinder body — glass with edge-lit gradient ══
  const bodyLeft = CX - CYL_W / 2;
  const bodyTop = CY - CYL_H / 2;

  const body = figma.createRectangle();
  body.name = "glass-body";
  body.resize(CYL_W, CYL_H);
  body.x = bodyLeft;
  body.y = bodyTop;
  body.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 0.40, g: 0.45, b: 0.55, a: 0.12 } },
      { position: 0.2, color: { r: 0.30, g: 0.35, b: 0.42, a: 0.04 } },
      { position: 0.5, color: { r: 0.20, g: 0.22, b: 0.28, a: 0.02 } },
      { position: 0.8, color: { r: 0.30, g: 0.35, b: 0.42, a: 0.04 } },
      { position: 1, color: { r: 0.40, g: 0.45, b: 0.55, a: 0.10 } }
    ],
    gradientTransform: [[1, 0, 0], [0, 1, 0]]
  }];
  body.strokes = [];
  frame.appendChild(body);

  // ══ Left edge — bright specular highlight ══
  const leftHighlight = figma.createRectangle();
  leftHighlight.name = "left-highlight";
  leftHighlight.resize(3, CYL_H);
  leftHighlight.x = bodyLeft;
  leftHighlight.y = bodyTop;
  leftHighlight.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 0.7, g: 0.75, b: 0.85, a: 0 } },
      { position: 0.1, color: { r: 0.7, g: 0.75, b: 0.85, a: 0.35 } },
      { position: 0.5, color: { r: 0.8, g: 0.85, b: 0.92, a: 0.5 } },
      { position: 0.9, color: { r: 0.7, g: 0.75, b: 0.85, a: 0.35 } },
      { position: 1, color: { r: 0.7, g: 0.75, b: 0.85, a: 0 } }
    ],
    gradientTransform: [[0, 1, 0], [-1, 0, 1]]
  }];
  leftHighlight.strokes = [];
  frame.appendChild(leftHighlight);

  // ══ Right edge — softer highlight ══
  const rightHighlight = figma.createRectangle();
  rightHighlight.name = "right-highlight";
  rightHighlight.resize(2, CYL_H);
  rightHighlight.x = bodyLeft + CYL_W - 2;
  rightHighlight.y = bodyTop;
  rightHighlight.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 0.5, g: 0.55, b: 0.65, a: 0 } },
      { position: 0.15, color: { r: 0.5, g: 0.55, b: 0.65, a: 0.2 } },
      { position: 0.85, color: { r: 0.5, g: 0.55, b: 0.65, a: 0.2 } },
      { position: 1, color: { r: 0.5, g: 0.55, b: 0.65, a: 0 } }
    ],
    gradientTransform: [[0, 1, 0], [-1, 0, 1]]
  }];
  rightHighlight.strokes = [];
  frame.appendChild(rightHighlight);

  // ══ Interior specular streak (glass reflection) ══
  const specular = figma.createRectangle();
  specular.name = "specular-streak";
  specular.resize(8, CYL_H * 0.7);
  specular.x = bodyLeft + CYL_W * 0.25;
  specular.y = bodyTop + CYL_H * 0.15;
  specular.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 1, g: 1, b: 1, a: 0 } },
      { position: 0.3, color: { r: 1, g: 1, b: 1, a: 0.06 } },
      { position: 0.7, color: { r: 1, g: 1, b: 1, a: 0.06 } },
      { position: 1, color: { r: 1, g: 1, b: 1, a: 0 } }
    ],
    gradientTransform: [[0, 1, 0], [-1, 0, 1]]
  }];
  specular.strokes = [];
  specular.cornerRadius = 4;
  frame.appendChild(specular);

  // ══ Top cap — glass lid with subtle blue tint ══
  const topCap = figma.createEllipse();
  topCap.name = "top-cap";
  topCap.resize(CYL_W, CAP_H);
  topCap.x = bodyLeft;
  topCap.y = bodyTop - CAP_H / 2;
  topCap.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 0.35, g: 0.40, b: 0.52, a: 0.25 } },
      { position: 0.5, color: { r: 0.45, g: 0.50, b: 0.62, a: 0.35 } },
      { position: 1, color: { r: 0.35, g: 0.40, b: 0.52, a: 0.20 } }
    ],
    gradientTransform: [[1, 0, 0], [0, 1, 0]]
  }];
  topCap.strokes = [{
    type: "SOLID",
    color: { r: 0.5, g: 0.55, b: 0.65, a: 0.3 }
  }];
  topCap.strokeWeight = 0.75;
  topCap.effects = [{
    type: "DROP_SHADOW",
    color: { r: 0.3, g: 0.35, b: 0.50, a: 0.15 },
    offset: { x: 0, y: -2 },
    radius: 12,
    spread: 0,
    visible: true,
    blendMode: "NORMAL"
  }];
  frame.appendChild(topCap);

  // ══ Top cap highlight ══
  const topCapShine = figma.createEllipse();
  topCapShine.name = "top-cap-shine";
  topCapShine.resize(CYL_W * 0.5, CAP_H * 0.3);
  topCapShine.x = CX - CYL_W * 0.25;
  topCapShine.y = bodyTop - CAP_H / 2 + CAP_H * 0.15;
  topCapShine.fills = [{
    type: "GRADIENT_RADIAL",
    gradientStops: [
      { position: 0, color: { r: 1, g: 1, b: 1, a: 0.15 } },
      { position: 1, color: { r: 1, g: 1, b: 1, a: 0 } }
    ],
    gradientTransform: [[1, 0, 0], [0, 1, 0]]
  }];
  topCapShine.strokes = [];
  frame.appendChild(topCapShine);

  // ══ Bottom cap — grounding ellipse ══
  const botCap = figma.createEllipse();
  botCap.name = "bottom-cap";
  botCap.resize(CYL_W, CAP_H);
  botCap.x = bodyLeft;
  botCap.y = bodyTop + CYL_H - CAP_H / 2;
  botCap.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 0.15, g: 0.18, b: 0.25, a: 0.15 } },
      { position: 1, color: { r: 0.10, g: 0.12, b: 0.18, a: 0.08 } }
    ],
    gradientTransform: [[1, 0, 0], [0, 1, 0]]
  }];
  botCap.strokes = [{
    type: "SOLID",
    color: { r: 0.4, g: 0.45, b: 0.55, a: 0.2 }
  }];
  botCap.strokeWeight = 0.5;
  frame.appendChild(botCap);

  // ══ Logo text: "ComInc." — etched on glass ══
  const logo = figma.createText();
  logo.name = "logo-text";
  logo.fontName = { family: "Inter", style: "Bold" };
  logo.characters = "ComInc.";
  logo.fontSize = 38;
  logo.letterSpacing = { value: 5, unit: "PIXELS" };
  logo.fills = [{
    type: "GRADIENT_LINEAR",
    gradientStops: [
      { position: 0, color: { r: 0.65, g: 0.70, b: 0.80, a: 0.55 } },
      { position: 0.3, color: { r: 0.80, g: 0.84, b: 0.90, a: 0.75 } },
      { position: 0.5, color: { r: 0.90, g: 0.92, b: 0.95, a: 0.85 } },
      { position: 0.7, color: { r: 0.80, g: 0.84, b: 0.90, a: 0.75 } },
      { position: 1, color: { r: 0.65, g: 0.70, b: 0.80, a: 0.55 } }
    ],
    gradientTransform: [[1, 0, 0], [0, 1, 0]]
  }];
  logo.effects = [{
    type: "DROP_SHADOW",
    color: { r: 0.4, g: 0.5, b: 0.7, a: 0.15 },
    offset: { x: 0, y: 0 },
    radius: 8,
    spread: 2,
    visible: true,
    blendMode: "NORMAL"
  }];
  logo.x = CX - 95;
  logo.y = CY - 15;
  frame.appendChild(logo);

  // ══ Tagline ══
  const tag = figma.createText();
  tag.name = "tagline";
  tag.fontName = { family: "Inter", style: "Light" };
  tag.characters = "YOUR GUIDE TO JOETSU & MYOKO";
  tag.fontSize = 8;
  tag.letterSpacing = { value: 4, unit: "PIXELS" };
  tag.fills = [{ type: "SOLID", color: { r: 0.40, g: 0.45, b: 0.52 } }];
  tag.x = CX - 100;
  tag.y = CY + 32;
  frame.appendChild(tag);

  // ══ Concept label ══
  const label = figma.createText();
  label.name = "concept-label";
  label.fontName = { family: "Inter", style: "Medium" };
  label.characters = "CONCEPT 04 — GLASS TOWER";
  label.fontSize = 9;
  label.letterSpacing = { value: 3, unit: "PIXELS" };
  label.fills = [{ type: "SOLID", color: { r: 0.30, g: 0.32, b: 0.38 } }];
  label.x = 40;
  label.y = 30;
  frame.appendChild(label);

  // ══ Description ══
  const desc = figma.createText();
  desc.name = "description";
  desc.fontName = { family: "Inter", style: "Regular" };
  desc.characters = "Literal 3D transparent glass cylinder.\nSpot UV on matte card \u2014 glossy cylinder catches light. Premium tactile experience.";
  desc.fontSize = 11;
  desc.lineHeight = { value: 20, unit: "PIXELS" };
  desc.fills = [{ type: "SOLID", color: { r: 0.38, g: 0.40, b: 0.45 } }];
  desc.x = 40;
  desc.y = 540;
  frame.appendChild(desc);

  // ══ Print spec ══
  const printSpec = figma.createText();
  printSpec.name = "print-spec";
  printSpec.fontName = { family: "Inter", style: "Regular" };
  printSpec.characters = "PRINT: Spot UV cylinder on 400gsm soft-touch matte";
  printSpec.fontSize = 8;
  printSpec.letterSpacing = { value: 2, unit: "PIXELS" };
  printSpec.fills = [{ type: "SOLID", color: { r: 0.30, g: 0.32, b: 0.38 } }];
  printSpec.x = 500;
  printSpec.y = 570;
  frame.appendChild(printSpec);

  figma.notify("Glass Tower concept refined");
})();
