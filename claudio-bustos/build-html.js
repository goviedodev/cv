#!/usr/bin/env node
/**
 * Genera guia-entrevista.html a partir de guia-entrevista.md.
 *
 * El markdown es la fuente unica de verdad: edita el .md (o pidele a otra IA
 * que lo continue) y vuelve a ejecutar:
 *
 *   node build-html.js
 */
const fs = require('fs');
const path = require('path');

const dir = __dirname;
const MD = path.join(dir, 'guia-entrevista.md');
const TPL = path.join(dir, '_template.html');
const OUT = path.join(dir, 'guia-entrevista.html');

const markdown = fs.readFileSync(MD, 'utf8');
const template = fs.readFileSync(TPL, 'utf8');

const encoded = Buffer.from(markdown, 'utf8')
  .toString('base64')
  .replace(/(.{120})/g, '$1\n'); // saltos de linea para que el HTML sea legible

if (!template.includes('__MARKDOWN_BASE64__')) {
  console.error('La plantilla no contiene el marcador __MARKDOWN_BASE64__');
  process.exit(1);
}

fs.writeFileSync(OUT, template.replace('__MARKDOWN_BASE64__', encoded), 'utf8');

const kb = (fs.statSync(OUT).size / 1024).toFixed(1);
const secciones = (markdown.match(/^## /gm) || []).length;
console.log(`OK  ${path.basename(OUT)}  (${kb} KB, ${secciones} secciones)`);
