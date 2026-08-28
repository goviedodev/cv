const fs = require('fs');
const base = fs.readFileSync(process.argv[2], 'utf8').split('\n').filter(Boolean);
const offers = fs.readFileSync(process.argv[3], 'utf8').split('\n').filter(Boolean);

const norm = s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, ' ').trim();
// baseline keys: title normalized + company first word
const baseKeys = new Set();
base.forEach(l => {
  const [t, c] = l.split(' @@ ');
  if (!t || !c) return;
  baseKeys.add(norm(t) + '|' + norm(c).split(' ')[0]);
});

const AFF = /java|backend|back end|full ?stack|arquitecto de software|ingenier[oa] de software|tech lead|lider tecnico|desarrollador senior|programador senior|spring|software engineer/i;
const EXCL = /\.net|dotnet|c#|cobol|salesforce|murex| sap |dynamics|prestashop| php |python|django|vue|golang|mainframe|\bqa\b|practica|soporte|power bi|\betl\b|sharepoint|shopify|wordpress|redes|pallet|ventas|pedagog/i;

const out = [];
offers.forEach(l => {
  const i = l.indexOf(' ||| ');
  const url = l.slice(0, i), txt = l.slice(i + 5);
  if (/ Postulado /.test(txt)) return;
  if (!AFF.test(txt)) return;
  if (EXCL.test(txt)) return;
  // derive title+company guess from url slug is unreliable; use text
  const clean = txt.replace(/Se precisa Urgente|Empleo destacado|Vista/g, '').trim();
  const m = clean.match(/^(.*?)\s+(?:\d,\d\s+)?(.+?)\s+(Santiago|Puerto Montt|Talca|Viña|Coquimbo|Iquique|concón|Colina|San Bernardo|Puente Alto)/i);
  const title = m ? m[1] : clean.slice(0, 50);
  const comp = m ? m[2] : '';
  const key = norm(title) + '|' + norm(comp).split(' ')[0];
  const applied = baseKeys.has(key);
  out.push({ url, title: title.trim(), comp: comp.trim(), applied, txt: clean.slice(0, 160) });
});

const fresh = out.filter(o => !o.applied);
console.log('TOTAL AFFINITY: ' + out.length + '  | already in baseline: ' + (out.length - fresh.length) + '  | FRESH: ' + fresh.length);
console.log('---');
fresh.forEach((o, i) => console.log((i + 1) + '. [' + o.comp + '] ' + o.title + '\n   ' + o.url));
