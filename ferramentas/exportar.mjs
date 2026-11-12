// Exporta uma peça HTML para PNG (um arquivo por <section class="peca">) ou PDF, e confere a peça antes.
// Uso: npm run exportar -- pecas/carrosseis/nome.html [--pdf]
//      npm run verificar -- pecas/carrosseis/nome.html      (só confere, não exporta)
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
const so = args.includes('--verificar');
const pdf = args.includes('--pdf');
const arq = args.find(a => !a.startsWith('--'));
if (!arq || !fs.existsSync(arq)) { console.error('Informe a peça: npm run exportar -- pecas/pasta/nome.html'); process.exit(1); }

const RESPIRO_LOGO = 96;   // px entre texto e logo do rodapé (DESIGN.md)
const MARGEM_SEGURA = 60;  // px da borda da peça

let browser;
try { browser = await chromium.launch({ channel: 'chrome' }); }
catch { browser = await chromium.launch(); }
const page = await browser.newPage({ deviceScaleFactor: 1, viewport: { width: 1200, height: 1400 } });
await page.goto(pathToFileURL(path.resolve(arq)).href, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);

const problemas = await page.evaluate(({ RESPIRO_LOGO, MARGEM_SEGURA }) => {
  const out = [];
  const pecas = [...document.querySelectorAll('section.peca')];
  if (!pecas.length) out.push('Nenhum <section class="peca"> na página.');
  const fontesOk = ['300 20px "Cormorant Garamond"', '300 20px "Fahkwang"'].every(f => document.fonts.check(f));
  if (!fontesOk) out.push('Fonte da marca não carregou (Cormorant Garamond ou Fahkwang). Confira o link para marca/componentes.css.');
  pecas.forEach((p, i) => {
    const n = `tela ${String(i + 1).padStart(2, '0')}`;
    const P = p.getBoundingClientRect();
    p.querySelectorAll('img').forEach(im => { if (!im.complete || !im.naturalWidth) out.push(`${n}: imagem não carregou (${im.getAttribute('src')}).`); });
    // elementos com texto próprio
    const textos = [...p.querySelectorAll('*')].filter(e => [...e.childNodes].some(c => c.nodeType === 3 && c.textContent.trim()) && getComputedStyle(e).visibility !== 'hidden');
    const caixas = textos.map(e => {
      const r = document.createRange(); r.selectNodeContents(e);
      const rs = [...r.getClientRects()].filter(q => q.width && q.height);
      if (!rs.length) return null;
      const b = { l: Math.min(...rs.map(q => q.left)), r: Math.max(...rs.map(q => q.right)), t: Math.min(...rs.map(q => q.top)), b: Math.max(...rs.map(q => q.bottom)) };
      return { e, b, txt: e.textContent.trim().slice(0, 40) };
    }).filter(Boolean);
    for (const { e, b, txt } of caixas) {
      if (b.l < P.left + MARGEM_SEGURA || b.r > P.right - MARGEM_SEGURA || b.t < P.top + MARGEM_SEGURA || b.b > P.bottom - MARGEM_SEGURA)
        out.push(`${n}: texto encostado na borda ou cortado: "${txt}".`);
      if (/—/.test(e.textContent)) out.push(`${n}: travessão (—) no texto: "${txt}". Use vírgula, ponto ou dois-pontos.`);
    }
    const logo = p.querySelector('.logo-rodape');
    if (logo) {
      const L = logo.getBoundingClientRect();
      for (const { e, b, txt } of caixas) {
        if (e.closest('.arraste')) continue;
        const sobrepoeX = b.r > L.left - 10 && b.l < L.right + 10;
        const dist = L.top - b.b;
        if (sobrepoeX && b.t < L.bottom && dist < RESPIRO_LOGO)
          out.push(`${n}: texto a ${Math.round(dist)} px do logo do rodapé (mínimo ${RESPIRO_LOGO}): "${txt}". Suba o texto.`);
      }
    }
  });
  return out;
}, { RESPIRO_LOGO, MARGEM_SEGURA });

if (problemas.length) {
  console.log('\nA peça tem problemas:\n' + problemas.map(p => '  · ' + p).join('\n') + '\n');
} else console.log('Conferência: tudo ok.');

if (!so) {
  const nome = path.basename(arq, '.html');
  const dest = path.join('export', path.basename(path.dirname(arq)), nome);
  fs.mkdirSync(dest, { recursive: true });
  const pecas = await page.$$('section.peca');
  if (pdf) {
    const { w, h } = await page.evaluate(() => { const r = document.querySelector('section.peca').getBoundingClientRect(); return { w: r.width, h: r.height }; });
    await page.addStyleTag({ content: 'body{padding:0!important;gap:0!important;background:none!important}section.peca{break-after:page}' });
    await page.pdf({ path: path.join(dest, nome + '.pdf'), width: w + 'px', height: h + 'px', printBackground: true });
    console.log('PDF:', path.join(dest, nome + '.pdf'));
  } else {
    for (let i = 0; i < pecas.length; i++) {
      const f = path.join(dest, `${nome}-${String(i + 1).padStart(2, '0')}.png`);
      await pecas[i].screenshot({ path: f });
      console.log('PNG:', f);
    }
  }
}
await browser.close();
process.exit(problemas.length ? 2 : 0);
