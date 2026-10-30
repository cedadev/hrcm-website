---
date: 2016-03-24 13:45:19
layout: base_hrcm
order: 3
permalink: /publications/
title: Publications
---

<h2>Peer-reviewed publications</h2>

<p id="publication-count" aria-live="polite">Loading publications…</p>

<div class="publication-controls">
  <label for="publication-search">Search publications</label>
  <input id="publication-search" type="search" placeholder="Search title, author, journal or year" autocomplete="off">

  <label for="publication-project">Project / bibliography</label>
  <select id="publication-project">
    <option value="">All projects</option>
    {% assign project_names = site.data.publications | map: "project" | uniq | sort %}
    {% for project in project_names %}
      {% if project and project != "" %}
        <option value="{{ project | escape }}">{{ project | escape }}</option>
      {% endif %}
    {% endfor %}
  </select>
</div>

<div id="publications-list">
  {% assign pubs_by_year = site.data.publications | group_by: "year" | sort: "name" | reverse %}
  {% for year_group in pubs_by_year %}
    {% if year_group.name and year_group.name != "" %}
      <section class="publication-year" data-year="{{ year_group.name }}">
        <h3>{{ year_group.name | escape }}</h3>
        <ul class="publication-items">
          {% assign sorted_pubs = year_group.items | sort_natural: "title" %}
          {% for pub in sorted_pubs %}
            <li class="publication-item"
                data-search="{{ pub.title }} {{ pub.author_text }} {{ pub.journal }} {{ pub.year }} {{ pub.project }} {{ pub.doi }} {{ pub.booktitle }} {{ pub.publisher | escape_once | downcase }}">
              <span class="publication-citation">
                {% if pub.author_text and pub.author_text != "" %}{{ pub.author_text | escape }}. {% endif %}
                {% if pub.title and pub.url and pub.url != "" %}
                  <a href="{{ pub.url | escape }}" target="_blank" rel="noopener noreferrer">{{ pub.title | escape }}</a>.
                {% elsif pub.title %}
                  {{ pub.title | escape }}.
                {% endif %}
                {% if pub.journal and pub.journal != "" %}<em>{{ pub.journal | escape }}</em>{% endif %}
                {% if pub.booktitle and pub.booktitle != "" %}<em>{{ pub.booktitle | escape }}</em>{% endif %}
                {% if pub.volume and pub.volume != "" %} {{ pub.volume | escape }}{% endif %}{% if pub.number and pub.number != "" %}({{ pub.number | escape }}){% endif %}{% if pub.pages and pub.pages != "" %}: {{ pub.pages | escape }}{% endif %}{% if pub.publisher and pub.publisher != "" %}. {{ pub.publisher | escape }}{% endif %}{% if pub.year and pub.year != "" %} ({{ pub.year | escape }}){% endif %}.
                {% if pub.doi and pub.doi != "" %}<a href="https://doi.org/{{ pub.doi | remove: 'https://doi.org/' | remove: 'http://doi.org/' | remove: 'http://dx.doi.org/' | escape }}" target="_blank" rel="noopener noreferrer">DOI</a>{% endif %}
                {% if pub.project and pub.project != "" %}<span class="publication-project">{{ pub.project | escape }}</span>{% endif %}
              </span>
            </li>
          {% endfor %}
        </ul>
      </section>
    {% endif %}
  {% endfor %}
</div>

<p id="publication-no-results" hidden>No publications match your search.</p>

<style>
    /* Publication search controls */
    .publication-controls {
        display: grid;
        grid-template-columns: minmax(0, 2fr) minmax(0, 1fr);
        gap: 18px;
        margin: 25px 0 30px;
        max-width: 850px;
        align-items: end;
    }

    .publication-controls label {
        display: block;
        font-size: 13px;
        font-weight: 600;
        color: #444;
        margin-bottom: 7px;
    }

    .publication-controls input,
    .publication-controls select {
        box-sizing: border-box;
        width: 100%;
        height: 44px;
        padding: 10px 14px;
        margin: 0;
        font-size: 14px;
        color: #333;
        background-color: #fff;
        border: 1px solid #d5d5d5;
        border-radius: 5px;
        box-shadow: none;
        transition: border-color 0.2s ease,
                    box-shadow 0.2s ease;
    }

    .publication-controls input:focus,
    .publication-controls select:focus {
        outline: none;
        border-color: #DE5E60;
        box-shadow: 0 0 0 3px rgba(222, 94, 96, 0.12);
    }

    .publication-controls input::placeholder {
        color: #999;
    }

    /* Publication list */
    .publication-items {
        padding-left: 1.25rem;
    }

    .publication-item {
        margin: 0 0 .9rem;
        line-height: 1.55;
    }

    .publication-project {
        display: inline-block;
        margin-left: .35rem;
        padding: .08rem .4rem;
        border: 1px solid #ccc;
        border-radius: .25rem;
        font-size: .78em;
        white-space: nowrap;
    }

    .publication-year[hidden],
    .publication-item[hidden] {
        display: none !important;
    }

    /* Mobile layout */
    @media (max-width: 600px) {
        .publication-controls {
            grid-template-columns: 1fr;
            gap: 12px;
        }
    }
</style>

<script>
(function () {
  var search = document.getElementById('publication-search');
  var project = document.getElementById('publication-project');
  var count = document.getElementById('publication-count');
  var noResults = document.getElementById('publication-no-results');
  var sections = Array.prototype.slice.call(document.querySelectorAll('.publication-year'));
  var items = Array.prototype.slice.call(document.querySelectorAll('.publication-item'));

  function filterPublications() {
    var query = (search.value || '').toLocaleLowerCase().trim();
    var selectedProject = project.value;
    var visible = 0;

    items.forEach(function (item) {
      var text = (item.getAttribute('data-search') || item.textContent).toLocaleLowerCase();
      var projectLabel = item.querySelector('.publication-project');
      var itemProject = projectLabel ? projectLabel.textContent : '';
      var matches = (!query || text.indexOf(query) !== -1) &&
                    (!selectedProject || itemProject === selectedProject);
      item.hidden = !matches;
      if (matches) visible += 1;
    });

    sections.forEach(function (section) {
      var hasVisible = section.querySelector('.publication-item:not([hidden])') !== null;
      section.hidden = !hasVisible;
    });

    count.textContent = visible + (visible === 1 ? ' publication' : ' publications');
    noResults.hidden = visible !== 0;
  }

  search.addEventListener('input', filterPublications);
  project.addEventListener('change', filterPublications);
  filterPublications();
}());
</script>
