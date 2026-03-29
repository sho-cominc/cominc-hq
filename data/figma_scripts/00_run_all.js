// ══════════════════════════════════════════════════════════════
// MASTER RUNNER — Execute all 4 concept refinements
//
// Usage: Run this via Figma MCP use_figma tool when rate limit resets.
// It combines all 4 scripts into one call to minimize API usage.
//
// File: bXlWmKXgUJU6xBuOpZgvLD
// ══════════════════════════════════════════════════════════════

(async () => {
  const page = figma.currentPage;

  // Remove all existing frames to start fresh
  for (const child of [...page.children]) child.remove();

  // ── Load all fonts upfront ──
  await Promise.all([
    figma.loadFontAsync({ family: "Inter", style: "Thin" }),
    figma.loadFontAsync({ family: "Inter", style: "Light" }),
    figma.loadFontAsync({ family: "Inter", style: "Regular" }),
    figma.loadFontAsync({ family: "Inter", style: "Medium" }),
    figma.loadFontAsync({ family: "Inter", style: "Semi Bold" }),
    figma.loadFontAsync({ family: "Inter", style: "Bold" }),
  ]);

  // ════════════════════════════════════════════════════════════
  // CONCEPT 01 — STACK
  // ════════════════════════════════════════════════════════════
  {
    const frame = figma.createFrame();
    frame.name = "01 — Stack";
    frame.resize(800, 600);
    frame.x = 0; frame.y = 0;
    frame.fills = [{ type: "SOLID", color: { r: 0.06, g: 0.06, b: 0.08 } }];
    frame.clipsContent = true;
    page.appendChild(frame);

    const CX = 240, CY = 265;

    // Ambient glow
    const glow = figma.createEllipse();
    glow.resize(300, 200); glow.x = CX - 150; glow.y = CY - 100;
    glow.fills = [{ type: "GRADIENT_RADIAL", gradientStops: [
      { position: 0, color: { r: 0.15, g: 0.55, b: 0.50, a: 0.08 } },
      { position: 1, color: { r: 0, g: 0, b: 0, a: 0 } }
    ], gradientTransform: [[1,0,0],[0,1,0]] }];
    glow.strokes = [];
    frame.appendChild(glow);

    function stackSlice(name, y, w, h, c1, c2, glowC, shadowY) {
      const e = figma.createEllipse();
      e.name = name; e.resize(w, h);
      e.x = CX - w/2; e.y = y;
      e.fills = [{ type: "GRADIENT_LINEAR", gradientStops: [
        { position: 0, color: { ...c1, a: 0.95 } },
        { position: 0.5, color: { ...c2, a: 1.0 } },
        { position: 1, color: { ...c1, a: 0.85 } }
      ], gradientTransform: [[1,0,0],[0,1,0]] }];
      e.strokes = [{ type: "SOLID", color: { ...c2, a: 0.3 } }];
      e.strokeWeight = 0.5;
      e.effects = [
        { type: "DROP_SHADOW", color: { r:0,g:0,b:0,a:0.4 }, offset:{x:0,y:shadowY}, radius:16, spread:0, visible:true, blendMode:"NORMAL" },
        { type: "DROP_SHADOW", color: { ...glowC, a:0.2 }, offset:{x:0,y:0}, radius:20, spread:2, visible:true, blendMode:"NORMAL" }
      ];
      frame.appendChild(e);
      // Shine
      const s = figma.createEllipse();
      s.name = name + "-shine"; s.resize(w*0.6, h*0.4);
      s.x = CX - (w*0.6)/2; s.y = y + h*0.1;
      s.fills = [{ type: "GRADIENT_LINEAR", gradientStops: [
        { position: 0, color: { r:1,g:1,b:1,a:0.25 } },
        { position: 1, color: { r:1,g:1,b:1,a:0 } }
      ], gradientTransform: [[0,1,0],[-1,0,1]] }];
      s.strokes = [];
      frame.appendChild(s);
    }

    stackSlice("slice-top", 190, 100, 28, {r:0.82,g:0.22,b:0.12},{r:0.95,g:0.35,b:0.18},{r:0.9,g:0.3,b:0.15}, 3);
    stackSlice("slice-mid", 240, 130, 34, {r:0.12,g:0.58,b:0.50},{r:0.18,g:0.72,b:0.58},{r:0.15,g:0.65,b:0.55}, 5);
    stackSlice("slice-bottom", 296, 105, 26, {r:0.50,g:0.54,b:0.58},{r:0.72,g:0.75,b:0.78},{r:0.6,g:0.63,b:0.67}, 4);

    // Guide lines
    for (const xOff of [-42, 42]) {
      const l = figma.createRectangle();
      l.resize(0.5, 90); l.x = CX + xOff; l.y = 210;
      l.fills = [{ type: "GRADIENT_LINEAR", gradientStops: [
        { position:0, color:{r:1,g:1,b:1,a:0} }, { position:0.3, color:{r:1,g:1,b:1,a:0.06} },
        { position:0.7, color:{r:1,g:1,b:1,a:0.06} }, { position:1, color:{r:1,g:1,b:1,a:0} }
      ], gradientTransform:[[0,1,0],[-1,0,1]] }];
      l.strokes = [];
      frame.appendChild(l);
    }

    // Logo
    const logo = figma.createText();
    logo.fontName = { family: "Inter", style: "Bold" };
    logo.characters = "ComInc."; logo.fontSize = 48;
    logo.letterSpacing = { value: 6, unit: "PIXELS" };
    logo.fills = [{ type: "GRADIENT_LINEAR", gradientStops: [
      { position:0, color:{r:0.92,g:0.92,b:0.93,a:1} },
      { position:1, color:{r:0.78,g:0.80,b:0.82,a:1} }
    ], gradientTransform:[[0,1,0],[-1,0,1]] }];
    logo.x = 370; logo.y = 238;
    frame.appendChild(logo);

    // Tagline
    const tag = figma.createText();
    tag.fontName = { family: "Inter", style: "Light" };
    tag.characters = "YOUR GUIDE TO JOETSU & MYOKO";
    tag.fontSize = 9; tag.letterSpacing = { value: 4, unit: "PIXELS" };
    tag.fills = [{ type: "SOLID", color: { r:0.40,g:0.42,b:0.45 } }];
    tag.x = 373; tag.y = 298;
    frame.appendChild(tag);

    // Label
    const lbl = figma.createText();
    lbl.fontName = { family: "Inter", style: "Medium" };
    lbl.characters = "CONCEPT 01 — STACK"; lbl.fontSize = 9;
    lbl.letterSpacing = { value: 3, unit: "PIXELS" };
    lbl.fills = [{ type: "SOLID", color: { r:0.30,g:0.32,b:0.35 } }];
    lbl.x = 40; lbl.y = 30;
    frame.appendChild(lbl);

    // Description
    const desc = figma.createText();
    desc.fontName = { family: "Inter", style: "Regular" };
    desc.characters = "Cylinder deconstructed into 3 floating slices.\nMinimal. Scalable. Favicon to billboard.";
    desc.fontSize = 11; desc.lineHeight = { value: 20, unit: "PIXELS" };
    desc.fills = [{ type: "SOLID", color: { r:0.35,g:0.37,b:0.40 } }];
    desc.x = 40; desc.y = 540;
    frame.appendChild(desc);

    // Favicon
    const fav = figma.createFrame();
    fav.name = "favicon-48"; fav.resize(48, 48);
    fav.x = 710; fav.y = 30;
    fav.fills = [{ type: "SOLID", color: { r:0.10,g:0.10,b:0.12 } }];
    fav.cornerRadius = 10;
    fav.effects = [{ type:"DROP_SHADOW",color:{r:0,g:0,b:0,a:0.3},offset:{x:0,y:2},radius:8,spread:0,visible:true,blendMode:"NORMAL" }];
    frame.appendChild(fav);
    for (const [y,w,h,c] of [[12,18,6,{r:0.90,g:0.30,b:0.15}],[20,22,7,{r:0.18,g:0.68,b:0.55}],[29,18,5,{r:0.65,g:0.68,b:0.72}]]) {
      const e = figma.createEllipse(); e.resize(w,h); e.x=24-w/2; e.y=y;
      e.fills=[{type:"SOLID",color:c}]; e.strokes=[]; fav.appendChild(e);
    }
  }

  // ════════════════════════════════════════════════════════════
  // CONCEPT 02 — MA-CYLINDER (間)
  // ════════════════════════════════════════════════════════════
  {
    const frame = figma.createFrame();
    frame.name = "02 — MA-Cylinder (間)";
    frame.resize(800, 600);
    frame.x = 860; frame.y = 0;
    frame.fills = [{ type: "GRADIENT_LINEAR", gradientStops: [
      { position:0, color:{r:0.96,g:0.94,b:0.91,a:1} },
      { position:1, color:{r:0.93,g:0.91,b:0.87,a:1} }
    ], gradientTransform:[[0,1,0],[-1,0,1]] }];
    frame.clipsContent = true;
    page.appendChild(frame);

    const CX = 400, CY = 290, PH = 200, GAP = 280;
    const leftX = CX - GAP/2, rightX = CX + GAP/2;
    const topY = CY - PH/2, botY = CY + PH/2;

    // Texture dots
    for (let r = 0; r < 12; r++) for (let c = 0; c < 16; c++) {
      const d = figma.createEllipse(); d.resize(1,1);
      d.x = 50+c*50; d.y = 50+r*50;
      d.fills=[{type:"SOLID",color:{r:0.82,g:0.80,b:0.76,a:0.3}}]; d.strokes=[];
      frame.appendChild(d);
    }

    // Pillar lines
    for (const x of [leftX, rightX]) {
      const p = figma.createRectangle(); p.resize(1.5, PH); p.x = x; p.y = topY;
      p.fills=[{type:"GRADIENT_LINEAR",gradientStops:[
        {position:0,color:{r:0.35,g:0.33,b:0.30,a:0.15}},{position:0.2,color:{r:0.35,g:0.33,b:0.30,a:0.6}},
        {position:0.8,color:{r:0.35,g:0.33,b:0.30,a:0.6}},{position:1,color:{r:0.35,g:0.33,b:0.30,a:0.15}}
      ],gradientTransform:[[0,1,0],[-1,0,1]]}];
      p.strokes=[];
      p.effects=[{type:"DROP_SHADOW",color:{r:0.35,g:0.33,b:0.30,a:0.1},offset:{x:1,y:1},radius:2,spread:0,visible:true,blendMode:"NORMAL"}];
      frame.appendChild(p);
    }

    // Caps
    for (const [y, op] of [[topY, 0.25], [botY, 0.18]]) {
      const cap = figma.createEllipse(); cap.resize(GAP+2, 16);
      cap.x = leftX - 0.5; cap.y = y - 8;
      cap.fills=[]; cap.strokes=[{type:"SOLID",color:{r:0.40,g:0.38,b:0.35,a:op}}];
      cap.strokeWeight = 0.75;
      frame.appendChild(cap);
    }

    // Serifs
    for (const y of [topY, botY]) {
      const s = figma.createRectangle(); s.resize(GAP+40, 0.5);
      s.x = leftX - 20; s.y = y;
      s.fills=[{type:"SOLID",color:{r:0.40,g:0.38,b:0.35,a:0.35}}]; s.strokes=[];
      frame.appendChild(s);
    }

    // 間 kanji (background)
    const kanji = figma.createText();
    kanji.fontName = { family: "Inter", style: "Thin" };
    kanji.characters = "間"; kanji.fontSize = 160;
    kanji.fills=[{type:"SOLID",color:{r:0.82,g:0.80,b:0.76,a:0.08}}];
    kanji.x = CX - 80; kanji.y = CY - 95;
    frame.appendChild(kanji);

    // Logo
    const logo = figma.createText();
    logo.fontName = { family: "Inter", style: "Light" };
    logo.characters = "ComInc."; logo.fontSize = 42;
    logo.letterSpacing = { value: 12, unit: "PIXELS" };
    logo.fills=[{type:"SOLID",color:{r:0.25,g:0.23,b:0.20}}];
    logo.x = CX - 120; logo.y = CY - 22;
    frame.appendChild(logo);

    // Tagline
    const tag = figma.createText();
    tag.fontName = { family: "Inter", style: "Regular" };
    tag.characters = "YOUR GUIDE TO JOETSU & MYOKO";
    tag.fontSize = 8; tag.letterSpacing = { value: 5, unit: "PIXELS" };
    tag.fills=[{type:"SOLID",color:{r:0.50,g:0.48,b:0.44}}];
    tag.x = CX - 105; tag.y = CY + 35;
    frame.appendChild(tag);

    // Label
    const lbl = figma.createText();
    lbl.fontName = { family: "Inter", style: "Medium" };
    lbl.characters = "CONCEPT 02 — MA-CYLINDER (間)"; lbl.fontSize = 9;
    lbl.letterSpacing = { value: 3, unit: "PIXELS" };
    lbl.fills=[{type:"SOLID",color:{r:0.55,g:0.53,b:0.50}}];
    lbl.x = 40; lbl.y = 30;
    frame.appendChild(lbl);

    // Desc
    const desc = figma.createText();
    desc.fontName = { family: "Inter", style: "Regular" };
    desc.characters = "間 (Ma) \u2014 the void defines the form.\nLetterpress on washi. Lines debossed, no ink. Space is the design.";
    desc.fontSize = 11; desc.lineHeight = { value: 20, unit: "PIXELS" };
    desc.fills=[{type:"SOLID",color:{r:0.50,g:0.48,b:0.44}}];
    desc.x = 40; desc.y = 540;
    frame.appendChild(desc);

    // Print note
    const pn = figma.createText();
    pn.fontName = { family: "Inter", style: "Regular" };
    pn.characters = "PRINT: Blind deboss on 350gsm cotton washi"; pn.fontSize = 8;
    pn.letterSpacing = { value: 2, unit: "PIXELS" };
    pn.fills=[{type:"SOLID",color:{r:0.65,g:0.63,b:0.60}}];
    pn.x = 570; pn.y = 570;
    frame.appendChild(pn);
  }

  // ════════════════════════════════════════════════════════════
  // CONCEPT 03 — TORU (透る)
  // ════════════════════════════════════════════════════════════
  {
    const frame = figma.createFrame();
    frame.name = "03 — Toru (透る)";
    frame.resize(800, 600);
    frame.x = 0; frame.y = 660;
    frame.fills = [{ type: "SOLID", color: { r:0.98,g:0.98,b:0.98 } }];
    frame.clipsContent = true;
    page.appendChild(frame);

    const CX = 400, CY = 285, CW = 180, CH = 200, CAP = 45;
    const bodyLeft = CX - CW/2, bodyTop = CY - CH/2;

    // Ground shadow
    const sh = figma.createEllipse(); sh.resize(CW+30, 20);
    sh.x = CX-(CW+30)/2; sh.y = CY+CH/2+15;
    sh.fills=[{type:"GRADIENT_RADIAL",gradientStops:[
      {position:0,color:{r:0,g:0,b:0,a:0.08}},{position:1,color:{r:0,g:0,b:0,a:0}}
    ],gradientTransform:[[1,0,0],[0,1,0]]}]; sh.strokes=[];
    frame.appendChild(sh);

    // Body
    const body = figma.createRectangle(); body.resize(CW, CH);
    body.x = bodyLeft; body.y = bodyTop;
    body.fills=[{type:"GRADIENT_LINEAR",gradientStops:[
      {position:0,color:{r:0.75,g:0.78,b:0.80,a:0.08}},{position:0.15,color:{r:0.85,g:0.87,b:0.89,a:0.03}},
      {position:0.5,color:{r:0.90,g:0.92,b:0.93,a:0.01}},{position:0.85,color:{r:0.85,g:0.87,b:0.89,a:0.03}},
      {position:1,color:{r:0.75,g:0.78,b:0.80,a:0.08}}
    ],gradientTransform:[[1,0,0],[0,1,0]]}]; body.strokes=[];
    frame.appendChild(body);

    // Edge lines
    for (const [x, w, a] of [[bodyLeft, 2, 0.4], [bodyLeft+CW-2, 2, 0.3]]) {
      const e = figma.createRectangle(); e.resize(w, CH); e.x = x; e.y = bodyTop;
      e.fills=[{type:"GRADIENT_LINEAR",gradientStops:[
        {position:0,color:{r:0.55,g:0.58,b:0.60,a:0}},{position:0.15,color:{r:0.55,g:0.58,b:0.60,a:a}},
        {position:0.85,color:{r:0.55,g:0.58,b:0.60,a:a}},{position:1,color:{r:0.55,g:0.58,b:0.60,a:0}}
      ],gradientTransform:[[0,1,0],[-1,0,1]]}]; e.strokes=[];
      frame.appendChild(e);
    }

    // Ribs
    for (const pos of [-0.25, 0, 0.25]) {
      const r = figma.createRectangle(); r.resize(0.75, CH);
      r.x = CX + pos*CW*0.8; r.y = bodyTop;
      r.fills=[{type:"GRADIENT_LINEAR",gradientStops:[
        {position:0,color:{r:0.6,g:0.63,b:0.65,a:0}},{position:0.2,color:{r:0.6,g:0.63,b:0.65,a:0.12}},
        {position:0.8,color:{r:0.6,g:0.63,b:0.65,a:0.12}},{position:1,color:{r:0.6,g:0.63,b:0.65,a:0}}
      ],gradientTransform:[[0,1,0],[-1,0,1]]}]; r.strokes=[];
      frame.appendChild(r);
    }

    // Top cap — vermillion
    const topCap = figma.createEllipse(); topCap.resize(CW, CAP);
    topCap.x = bodyLeft; topCap.y = bodyTop - CAP/2;
    topCap.fills=[{type:"GRADIENT_LINEAR",gradientStops:[
      {position:0,color:{r:0.78,g:0.18,b:0.10,a:0.85}},{position:0.5,color:{r:0.92,g:0.30,b:0.15,a:0.95}},
      {position:1,color:{r:0.80,g:0.20,b:0.10,a:0.88}}
    ],gradientTransform:[[1,0,0],[0,1,0]]}]; topCap.strokes=[];
    topCap.effects=[{type:"DROP_SHADOW",color:{r:0.85,g:0.25,b:0.12,a:0.2},offset:{x:0,y:4},radius:16,spread:0,visible:true,blendMode:"NORMAL"}];
    frame.appendChild(topCap);

    // Top shine
    const ts = figma.createEllipse(); ts.resize(CW*0.6, CAP*0.35);
    ts.x = CX - CW*0.3; ts.y = bodyTop - CAP/2 + CAP*0.15;
    ts.fills=[{type:"GRADIENT_LINEAR",gradientStops:[
      {position:0,color:{r:1,g:1,b:1,a:0.3}},{position:1,color:{r:1,g:1,b:1,a:0}}
    ],gradientTransform:[[0,1,0],[-1,0,1]]}]; ts.strokes=[];
    frame.appendChild(ts);

    // Bottom cap
    const bc = figma.createEllipse(); bc.resize(CW, CAP);
    bc.x = bodyLeft; bc.y = bodyTop + CH - CAP/2;
    bc.fills=[]; bc.strokes=[{type:"SOLID",color:{r:0.65,g:0.68,b:0.70,a:0.4}}];
    bc.strokeWeight = 1;
    frame.appendChild(bc);

    // Logo
    const logo = figma.createText();
    logo.fontName = { family: "Inter", style: "Semi Bold" };
    logo.characters = "ComInc."; logo.fontSize = 36;
    logo.letterSpacing = { value: 4, unit: "PIXELS" };
    logo.fills=[{type:"GRADIENT_LINEAR",gradientStops:[
      {position:0,color:{r:0.25,g:0.25,b:0.28,a:0.7}},{position:0.5,color:{r:0.20,g:0.20,b:0.22,a:0.85}},
      {position:1,color:{r:0.25,g:0.25,b:0.28,a:0.7}}
    ],gradientTransform:[[1,0,0],[0,1,0]]}];
    logo.x = CX - 88; logo.y = CY - 18;
    frame.appendChild(logo);

    // Tagline
    const tag = figma.createText();
    tag.fontName = { family: "Inter", style: "Light" };
    tag.characters = "YOUR GUIDE TO JOETSU & MYOKO";
    tag.fontSize = 8; tag.letterSpacing = { value: 4, unit: "PIXELS" };
    tag.fills=[{type:"SOLID",color:{r:0.55,g:0.55,b:0.58}}];
    tag.x = CX - 100; tag.y = CY + 28;
    frame.appendChild(tag);

    // Label
    const lbl = figma.createText();
    lbl.fontName = { family: "Inter", style: "Medium" };
    lbl.characters = "CONCEPT 03 — TORU (透る)"; lbl.fontSize = 9;
    lbl.letterSpacing = { value: 3, unit: "PIXELS" };
    lbl.fills=[{type:"SOLID",color:{r:0.55,g:0.55,b:0.58}}];
    lbl.x = 40; lbl.y = 30;
    frame.appendChild(lbl);

    // Desc
    const desc = figma.createText();
    desc.fontName = { family: "Inter", style: "Regular" };
    desc.characters = "Wireframe cylinder with transparency overlay.\nTop cap vermillion — like a hanko seal. Silver metallic ink for print.";
    desc.fontSize = 11; desc.lineHeight = { value: 20, unit: "PIXELS" };
    desc.fills=[{type:"SOLID",color:{r:0.50,g:0.50,b:0.53}}];
    desc.x = 40; desc.y = 540;
    frame.appendChild(desc);

    // Print spec
    const ps = figma.createText();
    ps.fontName = { family: "Inter", style: "Regular" };
    ps.characters = "PRINT: Silver metallic + vermillion spot color on uncoated stock";
    ps.fontSize = 8; ps.letterSpacing = { value: 2, unit: "PIXELS" };
    ps.fills=[{type:"SOLID",color:{r:0.65,g:0.65,b:0.68}}];
    ps.x = 420; ps.y = 570;
    frame.appendChild(ps);
  }

  // ════════════════════════════════════════════════════════════
  // CONCEPT 04 — GLASS TOWER
  // ════════════════════════════════════════════════════════════
  {
    const frame = figma.createFrame();
    frame.name = "04 — Glass Tower";
    frame.resize(800, 600);
    frame.x = 860; frame.y = 660;
    frame.fills = [{ type: "GRADIENT_LINEAR", gradientStops: [
      { position:0, color:{r:0.04,g:0.04,b:0.06,a:1} },
      { position:1, color:{r:0.08,g:0.08,b:0.10,a:1} }
    ], gradientTransform:[[0,1,0],[-1,0,1]] }];
    frame.clipsContent = true;
    page.appendChild(frame);

    const CX = 400, CY = 280, CW = 160, CH = 220, CAP = 40;
    const bL = CX-CW/2, bT = CY-CH/2;

    // Light source
    const ls = figma.createEllipse(); ls.resize(400,400);
    ls.x = CX-320; ls.y = CY-350;
    ls.fills=[{type:"GRADIENT_RADIAL",gradientStops:[
      {position:0,color:{r:0.3,g:0.35,b:0.45,a:0.06}},{position:1,color:{r:0,g:0,b:0,a:0}}
    ],gradientTransform:[[1,0,0],[0,1,0]]}]; ls.strokes=[];
    frame.appendChild(ls);

    // Ground reflection
    const gr = figma.createEllipse(); gr.resize(CW+80, 30);
    gr.x = CX-(CW+80)/2; gr.y = CY+CH/2+20;
    gr.fills=[{type:"GRADIENT_RADIAL",gradientStops:[
      {position:0,color:{r:0.25,g:0.30,b:0.40,a:0.12}},{position:1,color:{r:0,g:0,b:0,a:0}}
    ],gradientTransform:[[1,0,0],[0,1,0]]}]; gr.strokes=[];
    frame.appendChild(gr);

    // Body
    const body = figma.createRectangle(); body.resize(CW, CH);
    body.x = bL; body.y = bT;
    body.fills=[{type:"GRADIENT_LINEAR",gradientStops:[
      {position:0,color:{r:0.40,g:0.45,b:0.55,a:0.12}},{position:0.2,color:{r:0.30,g:0.35,b:0.42,a:0.04}},
      {position:0.5,color:{r:0.20,g:0.22,b:0.28,a:0.02}},{position:0.8,color:{r:0.30,g:0.35,b:0.42,a:0.04}},
      {position:1,color:{r:0.40,g:0.45,b:0.55,a:0.10}}
    ],gradientTransform:[[1,0,0],[0,1,0]]}]; body.strokes=[];
    frame.appendChild(body);

    // Left highlight
    const lh = figma.createRectangle(); lh.resize(3, CH); lh.x = bL; lh.y = bT;
    lh.fills=[{type:"GRADIENT_LINEAR",gradientStops:[
      {position:0,color:{r:0.7,g:0.75,b:0.85,a:0}},{position:0.1,color:{r:0.7,g:0.75,b:0.85,a:0.35}},
      {position:0.5,color:{r:0.8,g:0.85,b:0.92,a:0.5}},{position:0.9,color:{r:0.7,g:0.75,b:0.85,a:0.35}},
      {position:1,color:{r:0.7,g:0.75,b:0.85,a:0}}
    ],gradientTransform:[[0,1,0],[-1,0,1]]}]; lh.strokes=[];
    frame.appendChild(lh);

    // Right highlight
    const rh = figma.createRectangle(); rh.resize(2, CH); rh.x = bL+CW-2; rh.y = bT;
    rh.fills=[{type:"GRADIENT_LINEAR",gradientStops:[
      {position:0,color:{r:0.5,g:0.55,b:0.65,a:0}},{position:0.15,color:{r:0.5,g:0.55,b:0.65,a:0.2}},
      {position:0.85,color:{r:0.5,g:0.55,b:0.65,a:0.2}},{position:1,color:{r:0.5,g:0.55,b:0.65,a:0}}
    ],gradientTransform:[[0,1,0],[-1,0,1]]}]; rh.strokes=[];
    frame.appendChild(rh);

    // Specular streak
    const sp = figma.createRectangle(); sp.resize(8, CH*0.7);
    sp.x = bL + CW*0.25; sp.y = bT + CH*0.15;
    sp.fills=[{type:"GRADIENT_LINEAR",gradientStops:[
      {position:0,color:{r:1,g:1,b:1,a:0}},{position:0.3,color:{r:1,g:1,b:1,a:0.06}},
      {position:0.7,color:{r:1,g:1,b:1,a:0.06}},{position:1,color:{r:1,g:1,b:1,a:0}}
    ],gradientTransform:[[0,1,0],[-1,0,1]]}]; sp.strokes=[]; sp.cornerRadius = 4;
    frame.appendChild(sp);

    // Top cap
    const tc = figma.createEllipse(); tc.resize(CW, CAP);
    tc.x = bL; tc.y = bT - CAP/2;
    tc.fills=[{type:"GRADIENT_LINEAR",gradientStops:[
      {position:0,color:{r:0.35,g:0.40,b:0.52,a:0.25}},{position:0.5,color:{r:0.45,g:0.50,b:0.62,a:0.35}},
      {position:1,color:{r:0.35,g:0.40,b:0.52,a:0.20}}
    ],gradientTransform:[[1,0,0],[0,1,0]]}];
    tc.strokes=[{type:"SOLID",color:{r:0.5,g:0.55,b:0.65,a:0.3}}]; tc.strokeWeight = 0.75;
    tc.effects=[{type:"DROP_SHADOW",color:{r:0.3,g:0.35,b:0.50,a:0.15},offset:{x:0,y:-2},radius:12,spread:0,visible:true,blendMode:"NORMAL"}];
    frame.appendChild(tc);

    // Top shine
    const tcs = figma.createEllipse(); tcs.resize(CW*0.5, CAP*0.3);
    tcs.x = CX-CW*0.25; tcs.y = bT-CAP/2+CAP*0.15;
    tcs.fills=[{type:"GRADIENT_RADIAL",gradientStops:[
      {position:0,color:{r:1,g:1,b:1,a:0.15}},{position:1,color:{r:1,g:1,b:1,a:0}}
    ],gradientTransform:[[1,0,0],[0,1,0]]}]; tcs.strokes=[];
    frame.appendChild(tcs);

    // Bottom cap
    const bc = figma.createEllipse(); bc.resize(CW, CAP);
    bc.x = bL; bc.y = bT+CH-CAP/2;
    bc.fills=[{type:"GRADIENT_LINEAR",gradientStops:[
      {position:0,color:{r:0.15,g:0.18,b:0.25,a:0.15}},{position:1,color:{r:0.10,g:0.12,b:0.18,a:0.08}}
    ],gradientTransform:[[1,0,0],[0,1,0]]}];
    bc.strokes=[{type:"SOLID",color:{r:0.4,g:0.45,b:0.55,a:0.2}}]; bc.strokeWeight = 0.5;
    frame.appendChild(bc);

    // Logo — etched glass
    const logo = figma.createText();
    logo.fontName = { family: "Inter", style: "Bold" };
    logo.characters = "ComInc."; logo.fontSize = 38;
    logo.letterSpacing = { value: 5, unit: "PIXELS" };
    logo.fills=[{type:"GRADIENT_LINEAR",gradientStops:[
      {position:0,color:{r:0.65,g:0.70,b:0.80,a:0.55}},{position:0.3,color:{r:0.80,g:0.84,b:0.90,a:0.75}},
      {position:0.5,color:{r:0.90,g:0.92,b:0.95,a:0.85}},{position:0.7,color:{r:0.80,g:0.84,b:0.90,a:0.75}},
      {position:1,color:{r:0.65,g:0.70,b:0.80,a:0.55}}
    ],gradientTransform:[[1,0,0],[0,1,0]]}];
    logo.effects=[{type:"DROP_SHADOW",color:{r:0.4,g:0.5,b:0.7,a:0.15},offset:{x:0,y:0},radius:8,spread:2,visible:true,blendMode:"NORMAL"}];
    logo.x = CX-95; logo.y = CY-15;
    frame.appendChild(logo);

    // Tagline
    const tag = figma.createText();
    tag.fontName = { family: "Inter", style: "Light" };
    tag.characters = "YOUR GUIDE TO JOETSU & MYOKO";
    tag.fontSize = 8; tag.letterSpacing = { value: 4, unit: "PIXELS" };
    tag.fills=[{type:"SOLID",color:{r:0.40,g:0.45,b:0.52}}];
    tag.x = CX-100; tag.y = CY+32;
    frame.appendChild(tag);

    // Label
    const lbl = figma.createText();
    lbl.fontName = { family: "Inter", style: "Medium" };
    lbl.characters = "CONCEPT 04 — GLASS TOWER"; lbl.fontSize = 9;
    lbl.letterSpacing = { value: 3, unit: "PIXELS" };
    lbl.fills=[{type:"SOLID",color:{r:0.30,g:0.32,b:0.38}}];
    lbl.x = 40; lbl.y = 30;
    frame.appendChild(lbl);

    // Desc
    const desc = figma.createText();
    desc.fontName = { family: "Inter", style: "Regular" };
    desc.characters = "Literal 3D transparent glass cylinder.\nSpot UV on matte card \u2014 glossy cylinder catches light. Premium tactile.";
    desc.fontSize = 11; desc.lineHeight = { value: 20, unit: "PIXELS" };
    desc.fills=[{type:"SOLID",color:{r:0.38,g:0.40,b:0.45}}];
    desc.x = 40; desc.y = 540;
    frame.appendChild(desc);

    // Print spec
    const ps = figma.createText();
    ps.fontName = { family: "Inter", style: "Regular" };
    ps.characters = "PRINT: Spot UV cylinder on 400gsm soft-touch matte";
    ps.fontSize = 8; ps.letterSpacing = { value: 2, unit: "PIXELS" };
    ps.fills=[{type:"SOLID",color:{r:0.30,g:0.32,b:0.38}}];
    ps.x = 500; ps.y = 570;
    frame.appendChild(ps);
  }

  // ════════════════════════════════════════════════════════════
  // COMPARISON PAGE — All 4 logos side by side (small)
  // ════════════════════════════════════════════════════════════
  {
    const comp = figma.createFrame();
    comp.name = "05 — Comparison";
    comp.resize(1660, 200);
    comp.x = 0; comp.y = 1320;
    comp.fills = [{ type: "SOLID", color: { r: 0.95, g: 0.95, b: 0.95 } }];
    page.appendChild(comp);

    const titles = ["STACK", "MA-CYLINDER", "TORU", "GLASS TOWER"];
    for (let i = 0; i < 4; i++) {
      const t = figma.createText();
      t.fontName = { family: "Inter", style: "Medium" };
      t.characters = `0${i+1} — ${titles[i]}`;
      t.fontSize = 12;
      t.letterSpacing = { value: 2, unit: "PIXELS" };
      t.fills = [{ type: "SOLID", color: { r: 0.3, g: 0.3, b: 0.3 } }];
      t.x = 40 + i * 410;
      t.y = 90;
      comp.appendChild(t);
    }
  }

  figma.notify("All 4 concepts refined + comparison frame created");
})();
