#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');
const argv = require('minimist')(process.argv.slice(2));

(async () => {
  const url = argv.url || argv.u || 'http://localhost:8000/resume.html';
  const output = argv.output || argv.o || 'docs/resume-print.pdf';

  try {
    const browser = await puppeteer.launch({ args: ['--no-sandbox','--disable-setuid-sandbox'] });
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'networkidle2' });
    await page.emulateMediaType('screen');
    await page.pdf({ path: output, format: 'A4', printBackground: true, margin: { top: '20mm', bottom: '20mm', left: '15mm', right: '15mm' } });
    console.log('Wrote PDF to', output);
    await browser.close();
  } catch (err) {
    console.error('Failed to generate PDF:', err);
    process.exit(1);
  }
})();

