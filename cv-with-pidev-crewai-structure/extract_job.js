const fs = require('fs');
const https = require('https');

https.get('https://www.linkedin.com/jobs/view/4407443652', (res) => {
    let data = '';
    res.on('data', chunk => { data += chunk; });
    res.on('end', () => {
        // extract title
        const titleMatch = data.match(/<title>(.*?)<\/title>/);
        const title = titleMatch ? titleMatch[1] : 'Unknown Title';
        
        // extract description from script block application/ld+json
        let desc = 'Description not found';
        const ldjsonMatch = data.match(/<script type="application\/ld\+json">\s*(\{.*?\})\s*<\/script>/is);
        if (ldjsonMatch) {
            try {
                const ldjson = JSON.parse(ldjsonMatch[1]);
                if (ldjson.description) {
                    desc = ldjson.description.replace(/<[^>]+>/g, '\n').replace(/\n+/g, '\n');
                }
            } catch (e) {
                console.error('Error parsing ld+json', e);
            }
        }
        
        if (desc === 'Description not found') {
            const descMatch = data.match(/<div class="description__text description__text--rich">([\s\S]*?)<\/div>/i);
            if (descMatch) {
                desc = descMatch[1].replace(/<[^>]+>/g, '\n').replace(/\n+/g, '\n').trim();
            }
        }

        console.log(`TITLE: ${title}`);
        console.log(`DESCRIPTION:\n${desc}`);
    });
});
