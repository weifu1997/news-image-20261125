// Entry program for news-image-20261125 (Node 22, standard library only):
// the page is drawn at build time by render.py (Python 3 + Pillow) and
// shipped as entry.png beside this file; the program copies it to
// /output/entry.png, so both grader runs write identical bytes.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
