---
date: 2026-10-30 09:24:04
description: 'People'
layout: base_hrcm
order: 1
permalink: /people/
title: People
---

<style>
.people-page {
    max-width: 1170px;
    margin: 0 auto;
    padding: 20px 15px 55px;
}

.people-page .people-intro {
    max-width: 850px;
    margin-bottom: 35px;
}

.people-page .people-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 28px;
}

.people-page .person-card {
    overflow: hidden;
    background: #fff;
    border: 1px solid #e1e6e9;
    border-radius: 5px;
    box-shadow: 0 2px 8px rgba(30, 55, 70, 0.06);
}

.people-page .person-photo {
    display: block;
    width: 100%;
    aspect-ratio: 4 / 3;
    object-fit: cover;
    object-position: center 35%;
    background: #edf1f3;
}

.people-page .person-content {
    padding: 20px 22px 24px;
}

.people-page .person-name {
    margin: 0 0 8px;
    color: #174f78;
    font-size: 20px;
    line-height: 1.3;
}

.people-page .person-name a {
    color: inherit;
    text-decoration: none;
}

.people-page .person-name a:hover,
.people-page .person-name a:focus {
    text-decoration: underline;
}

.people-page .person-role {
    margin: 0 0 5px;
    font-weight: 600;
    color: #263746;
}

.people-page .person-affiliation {
    margin: 0 0 13px;
    color: #5c6b76;
    font-size: 14px;
}

.people-page .person-interests {
    margin: 0;
    color: #435461;
    font-size: 14px;
    line-height: 1.6;
}

.people-page .person-interests strong {
    color: #263746;
    font-weight: 600;
}

.people-page .people-section-heading {
    margin: 50px 0 25px;
    padding-bottom: 12px;
    color: #174f78;
    font-size: 27px;
    border-bottom: 2px solid #dce7ed;
}

@media (max-width: 900px) {
    .people-page .people-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}

@media (max-width: 600px) {
    .people-page .people-grid {
        grid-template-columns: 1fr;
        gap: 20px;
    }

    .people-page .person-photo {
        aspect-ratio: 16 / 9;
    }

    .people-page .people-section-heading {
        font-size: 24px;
    }
}
</style>

<section class="people-page">

    <h2>People</h2>

    <div class="people-intro">
        The High-Resolution Climate Modelling group brings together
        researchers working on high-resolution climate modelling,
        model development and the evaluation of climate simulations.
    </div>

    <div class="people-grid">

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/vidale_pierluigi.jpg"
                 alt="Prof. Pier Luigi Vidale"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://www.met.reading.ac.uk/~vidale/" target="_blank" rel="noopener">Prof. Pier Luigi Vidale</a></h3>
                <p class="person-role">Professor of Climate System Science</p>
                <p class="person-affiliation">Department of Meteorology, University of Reading</p>
                <p class="person-interests"><strong>Research interests:</strong> Global high-resolution climate model development, tropical and extratropical cyclones, land-surface processes, heat waves.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/roberts_malcolm.jpg"
                 alt="Dr Malcolm Roberts"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://scholar.google.co.uk/citations?hl=en&is_public_preview=1&sortby=pubdate&user=4HqmT-kAAAAJ&view_op=list_works" target="_blank" rel="noopener">Dr Malcolm Roberts</a></h3>
                <p class="person-role">Manager of the High-Resolution Modelling Group</p>
                <p class="person-affiliation">Met Office Hadley Centre</p>
                <p class="person-interests"><strong>Research interests:</strong> Global high-resolution coupled model development, ocean-atmosphere interaction, tropical cyclones.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/hodges_kevin.jpg"
                 alt="Dr Kevin Hodges"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://www.met.reading.ac.uk/userpages/sgshoges.php" target="_blank" rel="noopener">Dr Kevin Hodges</a></h3>
                <p class="person-role">Principal Research Fellow</p>
                <p class="person-affiliation">Department of Meteorology, University of Reading</p>
                <p class="person-interests"><strong>Research interests:</strong> Global high-resolution model evaluation, cyclones, feature-tracking methods.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/feng_xiangbo.jpg"
                 alt="Dr Xiangbo Feng"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://research.reading.ac.uk/meteorology/people/xiangbo-feng/" target="_blank" rel="noopener">Dr Xiangbo Feng</a></h3>
                <p class="person-role">Principal Research Scientist</p>
                <p class="person-affiliation">Department of Meteorology, University of Reading</p>
                <p class="person-interests"><strong>Research interests:</strong> Global high-resolution model evaluation, tropical cyclones, tropical wave activity.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/baker_alexander.jpg"
                 alt="Dr Alexander Baker"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://www.researchgate.net/profile/Alexander_Baker3" target="_blank" rel="noopener">Dr Alexander Baker</a></h3>
                <p class="person-role">Senior Research Scientist</p>
                <p class="person-affiliation">Department of Meteorology, University of Reading</p>
                <p class="person-interests"><strong>Research interests:</strong> Tropical and extratropical cyclones, global high-resolution model evaluation, industry collaboration.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/sommer_anna.jpg"
                 alt="Dr Anna Sommer"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://research.reading.ac.uk/meteorology/people/anna-sommer-denvil-sommer/" target="_blank" rel="noopener">Dr Anna Sommer</a></h3>
                <p class="person-role">Research Scientist</p>
                <p class="person-affiliation">Department of Meteorology, University of Reading</p>
                <p class="person-interests"><strong>Research interests:</strong> Global high-resolution ocean modelling, machine-learning methods.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/dey_ipshita.jpg"
                 alt="Dr Ipshita Dey"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://research.reading.ac.uk/meteorology/people/ipshita-dey/" target="_blank" rel="noopener">Dr Ipshita Dey</a></h3>
                <p class="person-role">Research Scientist</p>
                <p class="person-affiliation">Department of Meteorology, University of Reading</p>
                <p class="person-interests"><strong>Research interests:</strong> Ocean mesoscale-resolving models, extratropical cyclones, feature-tracking methods.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/auerswald_torsten.jpg"
                 alt="Dr Torsten Auerswald"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://research.reading.ac.uk/meteorology/people/torsten-auerswald/" target="_blank" rel="noopener">Dr Torsten Auerswald</a></h3>
                <p class="person-role">Research Scientist</p>
                <p class="person-affiliation">Department of Meteorology, University of Reading</p>
                <p class="person-interests"><strong>Research interests:</strong> Global high-resolution model evaluation, mesoscale convective systems, feature-tracking methods.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/saffin_leo.jpg"
                 alt="Dr Leo Saffin"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://leosaffin.github.io/" target="_blank" rel="noopener">Dr Leo Saffin</a></h3>
                <p class="person-role">Research Scientist</p>
                <p class="person-affiliation">Department of Meteorology, University of Reading</p>
                <p class="person-interests"><strong>Research interests:</strong> Tropical cyclones and extratropical interactions, feature-tracking methods.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/kangari_narenderreddy.jpg"
                 alt="Dr Narender Reddy Kangari"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://knreddy.online/" target="_blank" rel="noopener">Dr Narender Reddy Kangari</a></h3>
                <p class="person-role">Research Scientist</p>
                <p class="person-affiliation">Department of Meteorology, University of Reading</p>
                <p class="person-interests"><strong>Research interests:</strong> Global high-resolution land modelling and terrestrial carbon, energy, and water fluxes.</p>
            </div>
        </article>

    </div>

    <h2 class="people-section-heading">Affiliates &amp; collaborators</h2>

    <div class="people-grid">

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/seddon_jon.jpg"
                 alt="Jon Seddon"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name">Jon Seddon</h3>
                <p class="person-role">Scientific Software Engineer</p>
                <p class="person-affiliation">Met Office Hadley Centre</p>
                <p class="person-interests"><strong>Research interests:</strong> Managing peta-scale climate model output, development of analysis tools.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/vanniere_benoit.jpg"
                 alt="Dr Benoît Vannière"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://www.met.reading.ac.uk/userpages/nr912752.php" target="_blank" rel="noopener">Dr Benoît Vannière</a></h3>
                <p class="person-role">Research Scientist</p>
                <p class="person-affiliation">Department of Meteorology, University of Reading</p>
                <p class="person-interests"><strong>Research interests:</strong> Global hydrological cycle, tropical and extratropical cyclones, global high-resolution model evaluation.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/schiemann_reinhard.jpg"
                 alt="Dr Reinhard Schiemann"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://www.met.reading.ac.uk/~reinhard/home/" target="_blank" rel="noopener">Dr Reinhard Schiemann</a></h3>
                <p class="person-role">Senior Research Scientist</p>
                <p class="person-affiliation">Department of Meteorology, University of Reading</p>
                <p class="person-interests"><strong>Research interests:</strong> Global high-resolution model evaluation, cyclonic systems, atmospheric blocking, precipitation variability.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/berthou_segოლene.jpg"
                 alt="Dr Ségolène Berthou"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://www.lmd.jussieu.fr/Members/sberthou" target="_blank" rel="noopener">Dr Ségolène Berthou</a></h3>
                <p class="person-role">Research Scientist</p>
                <p class="person-affiliation">Met Office Hadley Centre</p>
                <p class="person-interests"><strong>Research interests:</strong> Air-sea coupling, regional climate modelling, global high-resolution model evaluation, Mediterranean climate.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/shaffrey_len.jpg"
                 alt="Prof. Len Shaffrey"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://www.met.reading.ac.uk/~swrshaff/" target="_blank" rel="noopener">Prof. Len Shaffrey</a></h3>
                <p class="person-role">Professor of Climate Science</p>
                <p class="person-affiliation">Department of Meteorology, University of Reading</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/demory_marieestelle.jpg"
                 alt="Dr Marie-Estelle Demory"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://usys.ethz.ch/en/people/profile.MjQ0NDUy.TGlzdC82MzcsMzIwMTk3MjIy.html" target="_blank" rel="noopener">Dr Marie-Estelle Demory</a></h3>
                <p class="person-role">Postdoctoral Scientist</p>
                <p class="person-affiliation">Institute for Atmospheric and Climate Science, ETH Zurich</p>
                <p class="person-interests"><strong>Research interests:</strong> Global high-resolution climate model development, global energy and hydrological cycles, land surface processes.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/muller_omar.jpg"
                 alt="Dr Omar Müller"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://research.reading.ac.uk/meteorology/people/omar-mueller/" target="_blank" rel="noopener">Dr Omar Müller</a></h3>
                <p class="person-role">Research Scientist in Land-surface Processes</p>
                <p class="person-affiliation">Department of Meteorology, University of Reading</p>
                <p class="person-interests"><strong>Research interests:</strong> Land surface processes, global high-resolution model evaluation.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/mizielinski_matthew.jpg"
                 alt="Dr Matthew Mizielinski"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://www.metoffice.gov.uk/research/people/matthew-mizielinski" target="_blank" rel="noopener">Dr Matthew Mizielinski</a></h3>
                <p class="person-role">Climate Research Scientist</p>
                <p class="person-affiliation">Met Office Hadley Centre</p>
                <p class="person-interests"><strong>Research interests:</strong> Global high-resolution climate modelling, CMIP6.</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/verhoef_anne.jpg"
                 alt="Prof. Anne Verhoef"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://www.reading.ac.uk/ges/Aboutus/Staff/a-verhoef.aspx" target="_blank" rel="noopener">Prof. Anne Verhoef</a></h3>
                <p class="person-role">Professor of Soil Physics and Micrometeorology</p>
                <p class="person-affiliation">Department of Geography and Environmental Science, University of Reading</p>
            </div>
        </article>

        <article class="person-card">
            <img class="person-photo"
                 src="{{ site.baseurl }}/assets/media/uploads/people/stevens_david.jpg"
                 alt="Prof. David Stevens"
                 loading="lazy">
            <div class="person-content">
                <h3 class="person-name"><a href="https://www.uea.ac.uk/mathematics/people/profile/d-stevens" target="_blank" rel="noopener">Prof. David Stevens</a></h3>
                <p class="person-role">Professor of Applied Mathematics</p>
                <p class="person-affiliation">School of Mathematics, University of East Anglia</p>
            </div>
        </article>

    </div>
</section>
```
