const fs = require('fs');
const html = fs.readFileSync('job.html', 'utf8');

const titleMatch = html.match(/<title>(.*?)<\/title>/);
const title = titleMatch ? titleMatch[1] : 'Unknown Title';

let desc = 'Description not found';
const ldjsonMatches = html.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/gi);
if (ldjsonMatches) {
    for (const match of ldjsonMatches) {
        try {
            const inner = match.replace(/<script[^>]*>/i, '').replace(/<\/script>/i, '');
            const ldjson = JSON.parse(inner);
            if (ldjson['@type'] === 'JobPosting') {
                desc = ldjson.description.replace(/<[^>]+>/g, '\n').replace(/\n+/g, '\n');
                break;
            }
        } catch (e) { }
    }
}

if (desc === 'Description not found') {
    const descMatch = html.match(/class="[^"]*show-more-less-html__markup[^"]*"[^>]*>([\s\S]*?)<\/div>/i);
    if (descMatch) {
        desc = descMatch[1].replace(/<[^>]+>/g, '\n').replace(/\n+/g, '\n').trim();
    }
}

console.log(`TITLE: ${title}`);
console.log(`\nDESCRIPTION:\n${desc}`);
