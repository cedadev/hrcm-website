---
date: 2026-10-26 13:46:44
description: 'HRCM Met Office Unified Model simulation catalogue'
layout: base_hrcm
full_width: true
order: 4
permalink: /data/simulations/
title: Simulation catalogue
---

### Search the table below for details of HRCM's Met Office Unified Model atmosphere-only and coupled simulations. In the near future, LFRic simulations will be added.

<!--
<p> </p>
<h4><strong>LATEST VERSION: <a href="{{ site.baseurl }}/assets/media/uploads/HadGEM3_runs/hadgem3_runs_mar_2018.pdf" target="_blank">HadGEM3 simulations - March 2018 (PDF)</a></strong></h4>
<p></p>
<p><strong>ARCHIVED VERSIONS</strong> </p>
<p><strong><a href="{{ site.baseurl }}/assets/media/uploads/HadGEM3_runs/hadgem3_runs_dec_2017.pdf" target="_blank">HadGEM3 simulations - 2017 (PDF)</a></strong></p>
<p><a href="{{ site.baseurl }}/assets/media/uploads/HadGEM3_runs/hadgem3_runs_jan_2016.pdf" target="_blank"><strong>HadGEM3 simulations - 2016 (PDF)</strong></a></p>
<p><strong><a href="{{ site.baseurl }}/assets/media/uploads/HadGEM3_runs/hadgem3_runs_oct_2015.pdf" target="_blank">HadGEM3 simulations - 2015 (PDF)</a></strong></p>
-->

<style>
    :root {
      --hrcm-ink: #263746;
      --hrcm-blue: #5685af;
      --hrcm-pale: #e7f0f6;
      --hrcm-border: #c8d1d8;
      --hrcm-muted: #5c6b76;
      --hrcm-paper: #fff;
      --hrcm-page: #f5f7f8;
    }
    .hadgem3-data-page, .hadgem3-data-page * { box-sizing: border-box; }
    .hadgem3-data-page {
      width: 100%; max-width: none; margin: 0; padding: 32px 15px 56px;
      color: var(--hrcm-ink); font: 16px/1.5 Arial, Helvetica, sans-serif;
    }
    .hadgem3-data-page h1 { margin: 0 0 8px; color: var(--hrcm-blue); font-size: clamp(1.65rem, 3vw, 2.35rem); line-height: 1.2; }
    .hadgem3-data-page .intro { max-width: 900px; margin: 0 0 22px; color: #435461; }
    .hadgem3-data-page .source-note { margin: 0 0 18px; color: var(--hrcm-muted); font-size: 1rem; }
    .hadgem3-data-page .publication-controls {
      display: grid; grid-template-columns: minmax(0, 2fr) minmax(0, 1fr);
      gap: 12px; margin: 25px 0 30px; max-width: 850px; align-items: center;
    }
    .hadgem3-data-page .publication-controls input,
    .hadgem3-data-page .publication-controls select {
      box-sizing: border-box; width: 100%; height: 44px; padding: 10px 14px;
      margin: 0; font-size: 14px; color: #333; background-color: #fff;
      border: 1px solid #d5d5d5; border-radius: 5px; box-shadow: none;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }
    .hadgem3-data-page .publication-controls input:focus,
    .hadgem3-data-page .publication-controls select:focus {
      outline: none; border-color: #DE5E60;
      box-shadow: 0 0 0 3px rgba(222, 94, 96, 0.12);
    }
    .hadgem3-data-page .publication-controls #table-search:focus,
    .hadgem3-data-page .publication-controls #table-search:focus-visible {
      outline: none; outline-offset: 0;
      border-color: #d5d5d5; box-shadow: 0 0 0 3px #dfeaf4;
    }
    .hadgem3-data-page .publication-controls input::placeholder { color: #999; }
    .hadgem3-data-page .publication-controls .result-count {
      grid-column: 1 / -1; color: var(--hrcm-muted); font-size: 1rem;
    }
    @media (max-width: 700px) {
      .hadgem3-data-page .publication-controls { grid-template-columns: 1fr; }
      .hadgem3-data-page .publication-controls .result-count { grid-column: 1; }
    }
    .hadgem3-data-page .table-wrap {
      display: block; width: 100%; max-width: 100%; min-width: 0;
      overflow: auto; max-height: 76vh; background: var(--hrcm-paper);
      border: 1px solid var(--hrcm-border); border-radius: 5px;
      box-shadow: 0 2px 8px rgba(20, 45, 62, .07);
    }
    .hadgem3-data-page table {
      width: 100%;
      min-width: 1800px;
      table-layout: fixed;
      border-collapse: separate;
      border-spacing: 0;
      font-size: 13px;
    }
    .hadgem3-data-page caption { padding: 12px 14px; text-align: left; color: var(--hrcm-muted); font-size: 12px; }
    .hadgem3-data-page th, .hadgem3-data-page td { padding: 8px 9px; vertical-align: top; text-align: left; border-right: 1px solid #e0e5e9; border-bottom: 1px solid #e0e5e9; }
    .hadgem3-data-page thead th {
      position: sticky; top: 0; z-index: 2; color: #fff; background: var(--hrcm-blue);
      border-bottom: 2px solid #103b5a; white-space: nowrap;
    }
    .hadgem3-data-page #runs-table thead,
    .hadgem3-data-page #runs-table thead tr,
    .hadgem3-data-page #runs-table thead th {
      background: #fff !important;
      background-color: #fff !important;
      color: #5685af !important;
    }
    .hadgem3-data-page #runs-table thead th button {
      background: transparent !important;
      color: #5685af !important;
    }
    .hadgem3-data-page #runs-table th,
    .hadgem3-data-page #runs-table td {
      min-width: 0; white-space: normal; overflow-wrap: anywhere;
    }
    .hadgem3-data-page thead th button {
      padding: 0; border: 0; color: inherit; background: transparent; font: inherit;
      font-weight: 700; text-align: left; cursor: pointer;
    }
    .hadgem3-data-page thead th button:focus-visible, .hadgem3-data-page input:focus-visible, .hadgem3-data-page select:focus-visible {
      outline: 3px solid #4089b4; outline-offset: 2px;
    }
    .hadgem3-data-page tbody tr:nth-child(even) { background: #f8fafb; }
    .hadgem3-data-page tbody tr:hover { background: #edf5fa; }
    .hadgem3-data-page tbody td:first-child { font-weight: 700; color: #5685af; }
    .hadgem3-data-page td:nth-child(3), .hadgem3-data-page td:nth-child(4), .hadgem3-data-page td:nth-child(6), .hadgem3-data-page td:nth-child(7), .hadgem3-data-page td:nth-child(8), .hadgem3-data-page td:nth-child(10) { white-space: nowrap; }
    .hadgem3-data-page td:nth-child(5) { font-family: Consolas, Monaco, monospace; }
    .hadgem3-data-page td:nth-child(13) { overflow-wrap: anywhere; font-family: Consolas, Monaco, monospace; font-size: 12px; }
    .hadgem3-data-page .empty { color: #98a4ac; }
    .hadgem3-data-page .table-footer { padding: 12px 2px 0; color: var(--hrcm-muted); font-size: 13px; }
    .hadgem3-data-page .no-results { padding: 24px; text-align: center; color: var(--hrcm-muted); }
    @media (max-width: 640px) {
      main { padding: 24px 12px 40px; }
      .hadgem3-data-page .table-wrap { max-height: 72vh; }
    }
    @media print {
      body { background: #fff; }
      main { max-width: none; padding: 0; }
      .publication-controls, .table-footer { display: none; }
      .hadgem3-data-page .table-wrap { overflow: visible; max-height: none; border: 0; box-shadow: none; }
      .hadgem3-data-page table { min-width: 0; font-size: 7pt; }
      th { position: static; }
    }
  </style>
<section class="hadgem3-data-page">
    <div class="publication-controls">
      <input id="table-search" type="search"
             aria-label="Search simulation data"
             placeholder="Search by model configuration, run identifier, resolution, etc"
             autocomplete="off">
      <select id="model-filter" aria-label="Choose model">
        <option value="">Unified Model</option>
      </select>
      <span class="result-count" id="result-count" aria-live="polite"></span>
    </div>
{% include simulations_table.html %}
    <p class="table-footer">Tip: on a narrow screen, scroll horizontally to see all columns. Column headings can be selected to change the sort order.</p>
</section>

  <script>
    // The table itself is generated by Jekyll from _data/simulations.yml (see
    // _includes/simulations_table.html). This script reads the rendered rows from the page,
    // then provides search, the model dropdown filter, and click-to-sort column headings.
    const searchInput = document.getElementById('table-search');
    const modelFilter = document.getElementById('model-filter');
    const body = document.getElementById('table-body');
    const count = document.getElementById('result-count');
    const noResults = document.getElementById('no-results');
    const headerButtons = Array.from(document.querySelectorAll('#table-head button'));
    const headers = headerButtons.map(b => b.textContent.trim());

    // One entry per table row: the <tr> element plus its cell values as plain text
    // (empty cells, shown as an em dash on the page, count as '').
    const rows = Array.from(body.querySelectorAll('tr')).map(tr => ({
      el: tr,
      cells: Array.from(tr.children).map(td => td.classList.contains('empty') ? '' : td.textContent.trim())
    }));

    let sortColumn = -1;
    let sortDirection = 1;

    function getFilteredRows() {
      const query = searchInput.value.trim().toLocaleLowerCase();
      const model = modelFilter.value;
      let result = rows.filter(row => {
        const text = row.cells.join(' ').toLocaleLowerCase();
        return (!query || text.includes(query)) && (!model || row.cells[0] === model);
      });
      if (sortColumn >= 0) {
        result = result.slice().sort((a, b) => {
          const av = String(a.cells[sortColumn] ?? '').toLocaleLowerCase();
          const bv = String(b.cells[sortColumn] ?? '').toLocaleLowerCase();
          return av.localeCompare(bv, undefined, { numeric: true, sensitivity: 'base' }) * sortDirection;
        });
      }
      return result;
    }

    function render() {
      const visible = getFilteredRows();
      body.replaceChildren(...visible.map(row => row.el));
      count.textContent = `${visible.length} of ${rows.length} entries shown`;
      noResults.hidden = visible.length !== 0;
    }

    headerButtons.forEach((button, index) => {
      button.addEventListener('click', () => {
        if (sortColumn === index) sortDirection *= -1;
        else { sortColumn = index; sortDirection = 1; }
        headerButtons.forEach((b, i) => {
          b.textContent = headers[i] + (sortColumn === i ? (sortDirection === 1 ? ' ▲' : ' ▼') : '');
          b.setAttribute('aria-label', `${headers[i]}${sortColumn === i ? (sortDirection === 1 ? ', ascending' : ', descending') : ', sort'}`);
        });
        render();
      });
    });

    [...new Set(rows.map(row => row.cells[0]).filter(Boolean))].sort((a, b) => a.localeCompare(b)).forEach(model => {
      const option = document.createElement('option');
      option.value = model;
      option.textContent = model;
      modelFilter.appendChild(option);
    });
    searchInput.addEventListener('input', render);
    modelFilter.addEventListener('change', render);
    render();
  </script>
