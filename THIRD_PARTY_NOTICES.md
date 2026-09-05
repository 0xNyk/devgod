# Third-party notices

## Deep-Research-skills

The research pipeline in `references/deep-research.md` and the adapted validator
in `scripts/research-validate-json.py` credit
[Weizhena/Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills).
The upstream MIT notice is reproduced below. Verified against upstream LICENSE
blob `57d6df8dfc71cd3e6b35fd6c2776084843f2d73b` on 2026-09-05.
The original adaptation revision was not recorded; this license check does not
establish which source revision was copied.

MIT License

Copyright (c) 2026 Lan Zheng

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Build and validation dependencies

The validation workflow checks out the public unmachined scanner at a pinned
revision. The scanner is not vendored into this package. PyYAML, TypeScript, and
GitHub Actions are build or fixture dependencies with their own upstream licenses.
Source links in research reports identify reference material; they do not grant
permission to redistribute upstream text or code. Preserve applicable notices
when adding copied material and record its revision at the point of import.
