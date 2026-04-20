import { chromium } from 'playwright';
import { mkdirSync } from 'node:fs';

process.env.PLAYWRIGHT_BROWSERS_PATH = '/opt/pw-browsers';

const outDir = '/home/user/cominc-hq/bkc-yume-web/preview';
mkdirSync(outDir, { recursive: true });

const pages = [
  { url: 'http://localhost:3000/ja/', name: '01-top-ja' },
  { url: 'http://localhost:3000/en/', name: '02-top-en' },
  { url: 'http://localhost:3000/ja/menu', name: '03-menu-ja' },
  { url: 'http://localhost:3000/ja/schedule', name: '04-schedule-ja' },
  { url: 'http://localhost:3000/ja/about', name: '05-about-ja' },
  { url: 'http://localhost:3000/ja/contact', name: '06-contact-ja' },
];

const browser = await chromium.launch({
  executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
});

for (const viewport of [
  { label: 'mobile', width: 390, height: 844 },
  { label: 'desktop', width: 1280, height: 900 },
]) {
  const ctx = await browser.newContext({
    viewport: { width: viewport.width, height: viewport.height },
    deviceScaleFactor: 2,
  });
  for (const p of pages) {
    const page = await ctx.newPage();
    await page.goto(p.url, { waitUntil: 'networkidle', timeout: 20000 });
    await page.waitForTimeout(600);
    const path = `${outDir}/${p.name}-${viewport.label}.png`;
    await page.screenshot({ path, fullPage: true });
    console.log('✓', path);
    await page.close();
  }
  await ctx.close();
}
await browser.close();
