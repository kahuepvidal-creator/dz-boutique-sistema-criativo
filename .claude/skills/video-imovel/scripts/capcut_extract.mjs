// Tira do index.html (HyperFrames) do imóvel as camadas gráficas em PNG de tela cheia
// e as caixas dos textos, para montar o projeto do CapCut (capcut_build.py).
// Uso: node capcut_extract.mjs <projeto> [<projeto> ...]
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
const keys = process.argv.slice(2).map(p => path.resolve(p));
let browser;
try { browser = await chromium.launch({ channel: 'chrome', args: ['--hide-scrollbars', '--allow-file-access-from-files'] }); }
catch { browser = await chromium.launch({ args: ['--hide-scrollbars', '--allow-file-access-from-files'] }); }
for (const key of keys) {
  const out = `${key}/capcut`; fs.mkdirSync(out, { recursive: true });
  const p = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  // sem GSAP: tudo no estado final do CSS, sem blur nem deslocamento de entrada
  await p.route('**/*', r => r.request().url().includes('gsap') ? r.abort() : r.continue());
  await p.goto(`file://${key}/index.html`, { waitUntil: 'networkidle', timeout: 90000 });
  await p.evaluate(() => document.fonts.ready);
  // tudo visível, sem animação
  await p.addStyleTag({ content: '*{opacity:1 !important; transition:none !important} .clip{visibility:visible !important}' });
  const boxes = await p.evaluate(() => {
    const r = s => { const e = document.querySelector(s); if (!e) return null; const b = e.getBoundingClientRect(); return { x: b.x, y: b.y, w: b.width, h: b.height }; };
    const o = { bairro: r('#c-bairro-in .bairro'), dia: r('#c-bairro-in .dia'), rua: r('#c-bairro-in .rua'), ig: r('#c-ig-in .ig span'), igsvg: r('#c-ig-in svg'),
      logo: r('#end-logo'), nome: r('#end-nome'), endig: r('#end-ig'), wm: r('#wm-img'), lines: [] };
    document.querySelectorAll('#c-tipo-in .ln').forEach(l => { const b = l.querySelector('span').getBoundingClientRect(), d = l.querySelector('.dot').getBoundingClientRect(); o.lines.push({ text: l.textContent, x: b.x, y: b.y, w: b.width, h: b.height, dot: { x: d.x, y: d.y, w: d.width, h: d.height } }); });
    return o;
  });
  fs.writeFileSync(`${out}/boxes.json`, JSON.stringify(boxes, null, 1));
  // camadas: mostra só o seletor pedido, fundo transparente
  const layer = async (name, show, opaque = false) => {
    await p.evaluate((show, opaque) => {
      for (const e of document.querySelectorAll('#root *')) e.style.visibility = 'hidden';
      for (const e of [document.documentElement, document.body, document.getElementById('root')]) e.style.background = opaque ? '' : 'transparent';
      for (const s of show) for (const e of document.querySelectorAll(s)) { e.style.visibility = 'visible'; let a = e.parentElement; while (a && a.id !== 'root') { a.style.visibility = 'visible'; a = a.parentElement; } for (const c of e.querySelectorAll('*')) c.style.visibility = 'visible'; }
      // pais ficam visíveis, mas irmãos não: esconde de novo os filhos dos pais que não estão no caminho
    }, show, opaque);
    await p.screenshot({ path: `${out}/${name}.png`, omitBackground: !opaque });
  };
  await layer('veu', ['.veil']);
  await layer('sombra-bairro', ['#c-bairro-sh']);
  await layer('sombra-tipologia', ['#c-tipo-sh']);
  await layer('sombra-instagram', ['#c-ig-sh', '#c-ig-in svg']);
  await layer('marca-dagua', ['#wm-img']);
  await layer('cartela-fundo', ['#end-bg'], true);
  await layer('cartela-logo', ['#end-logo']);
  await p.close();
  console.log(path.basename(key), 'ok', JSON.stringify(boxes).slice(0, 300));
}
await browser.close();
