// Compile the pinned upstream Codex bundle and expose it through library symlinks.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const library = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const upstream = path.join(library, 'refs/impeccable');
const bundle = path.join(upstream, 'dist/codex/.codex/skills/impeccable');
const canonical = path.join(library, 'skills/also/impeccable');
const codex = path.join(os.homedir(), '.codex/skills/impeccable');
const links = [[canonical, bundle], [codex, canonical]];

// Check collisions before generating files or changing links.
for (const [link, target] of links) {
  const stat = fs.lstatSync(link, { throwIfNoEntry: false });
  if (stat && (!stat.isSymbolicLink() || path.resolve(path.dirname(link), fs.readlinkSync(link)) !== target)) {
    throw new Error(`Refusing to replace existing entry: ${link}`);
  }
}

const { readSourceFiles } = await import(pathToFileURL(path.join(upstream, 'scripts/lib/utils.js')));
const { transformCodex } = await import(pathToFileURL(path.join(upstream, 'scripts/lib/transformers/index.js')));
const { version } = JSON.parse(fs.readFileSync(path.join(upstream, '.claude-plugin/plugin.json'), 'utf8'));
transformCodex(readSourceFiles(upstream).skills, path.join(upstream, 'dist'), { skillsVersion: version });

for (const [link, target] of links) {
  if (!fs.lstatSync(link, { throwIfNoEntry: false })) {
    fs.mkdirSync(path.dirname(link), { recursive: true });
    fs.symlinkSync(path.relative(path.dirname(link), target), link, 'dir');
  }
  console.log(`Linked: ${link} -> ${fs.realpathSync(link)}`);
}
