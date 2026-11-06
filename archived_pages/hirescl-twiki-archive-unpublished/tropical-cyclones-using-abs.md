---
date: 2020-09-28 16:26:36
description: 'Analysing tropical storm observations: TS_OBS'
layout: base_hrcm
order: 20
permalink: /hirescl-twiki-archive-unpublished/tropical-cyclones-using-abs/
title: 'Tropical cyclones: using obs'
---

<p><span style="">Analysing tropical storm observations: TS_OBS</span></p>
<div id="patternScreen">
<div id="patternPageShadow">
<div id="patternPage">
<div id="patternWrapper">
<div id="patternOuter">
<div id="patternFloatWrap">
<div id="patternMain">
<div id="patternMainContents">
<div class="patternContent">
<div class="patternTopic">This Twiki page contains information about the <code>ts_obs</code>Python module and how to get it running on your local machine.
<p></p>
<div class="twikiToc">
<ul>
<li><a href="#Analysing tropical storm observa"> Analysing tropical storm observations: TS_OBS</a>
<ul>
<li><a href="#1. About ts_obs"> 1. About ts_obs</a></li>
<li><a href="#2. Setting up ts_obs"> 2. Setting up ts_obs</a></li>
<li><a href="#3. What's in ts_obs?"> 3. What's in ts_obs?</a></li>
<li><a href="#4. Example code"> 4. Example code</a></li>
<li><a href="#5. Anything else?"> 5. Anything else?</a></li>
<li><a href="#6. Troubleshooting"> 6. Troubleshooting</a></li>
<li><a href="#6. Contact"> 6. Contact</a></li>
</ul>
</li>
</ul>
</div>
<p></p>
<h2><a name="1. About ts_obs"></a> 1. About ts_obs</h2>
<code>ts_obs</code> is a Python module written by Joanne Camp to read in and analyse global tropical storm observations. Observations for the North Atlantic and eastern Pacific are obtained from the NOAA <a href="http://www.aoml.noaa.gov/hrd/hurdat/Data_Storm.html" target="_top">U.S. National Hurricane Center</a> (NHC); observations for the rest of the world are obtained from the U.S. Navy's <a href="http://www.usno.navy.mil/NOOC/nmfc-ph/RSS/jtwc/best_tracks/" target="_top">Joint Typhoon Warning Centre</a>(JTWC).
<p></p>
<h2><a name="2. Setting up ts_obs"></a> 2. Setting up ts_obs</h2>
<code>ts_obs</code> is stored under FCM in the repository: <code>svn://fcm9/GS_svn/TropicalStorms/trunk/ts_obs</code>
<p></p>
<ol>
<li>Check out a working copy of this directory (note this will put a copy of <code>ts_obs</code>in your current directory):
<ul>
<li>
<pre> fcm co svn://fcm9/GS_svn/TropicalStorms/trunk/ts_obs . </pre>
</li>
</ul>
</li>
<li>You then need to set the <code>PYTHONPATH</code>so that Python can find your code:
<ul>
<li>
<pre> USER_SITE=${HOME}/.local/lib/python2.7/site-packages &amp;&amp; mkdir -p $USER_SITE &amp;&amp; echo `pwd` &gt; ${USER_SITE}/ts_obs.pth </pre>
</li>
</ul>
</li>
</ol>
<p></p>
<h2><a name="3. What's in ts_obs?"></a> 3. What's in ts_obs?</h2>
inside <code>ts_obs</code> you should find some python code (e.g. <code>hurdat2.py</code>), which reads in different observation datasets, and 3 sub-directories: <code>example_code</code>, <code>sample_data</code> and <code>tests</code>:<ol>
<li><code>example_code</code>:
<ul>
<li>Contains example functions that are used to analyse tropical storm observations and produce example plots. <strong>This directory will be the most useful to you.</strong></li>
</ul>
</li>
<li><code>tests</code>:
<ul>
<li>This is where I've written tests for all the main Python routines in the module. <strong>There should be no need to modify these.</strong></li>
</ul>
</li>
<li><code>sample_data</code>:
<ul>
<li>Contains text files of observations which are used to test code and generate example plots. The best-track data are available up to 2011. The module also allows you to read in real-time observations which are used for inoput into the Global Model. These observations are kept on <a href="http://www-nwp/~frjh/tropicalcyclone/database.html" target="_top">Julian Heming's webpage.</a> (you need the 'unsorted' data).</li>
</ul>
</li>
</ol>
<p></p>
<h2><a name="4. Example code"></a> 4. Example code</h2>
You can have a go at running some of the <code>example_code</code> routines yourself - you just need to navigate to the <code>example_code</code>directory and type the name of the program:<ol>
<li><strong>storm_tracks.py</strong>
<ul>
<li><code>python2.7 storm_tracks.py</code></li>
<li>This program produces 4 individual plots of: storm tracks, storm genesis/formation locations, location of maximum wind speed and lysis/dissipation location. Note you have to close the window on the screen in order to produce the next plot. Plots are produced for the whole globe, but you can also see results for individual basins by setting the basin to <code>'na'</code> for the North Atlantic or <code>'ep'</code> for the Eastern Pacific etc. Basins available: North Atlantic (<code>'na'</code>), eastern Pacific (<code>'ep'</code>), [central Pacific (<code>'cp'</code>)], western Pacific (<code>'wp'</code>), North Indian Ocean (<code>'ni'</code>), Southwest Indian Ocean (<code>'si'</code>), Australian region (<code>'au'</code>) and the South Pacific (<code>'sp'</code>).</li>
</ul>
</li>
<li><strong>storm_track_density.py</strong>
<ul>
<li><code>python2.7 storm_track_density.py</code></li>
<li>Produces a global plot of monthly-mean tropical storm track density for the period June-November 1996-2009.</li>
</ul>
</li>
<li><strong>annual_variability.py</strong>
<ul>
<li><code>python2.7 annual_variability.py</code></li>
<li>Plots annual average tropical storm counts over the period 1996-2009. Plot produced for the North Atlantic. This can be changed to any basin by setting <code>basin</code> (see bullet 1 for basin list).</li>
</ul>
</li>
</ol>
<p></p>
<h2><a name="5. Anything else?"></a> 5. Anything else?</h2>
I think most of the information that you may need to get from the tropical storm observations can be accessed via the test routines; however, if there is anything else that would be useful then please let me know - I've probably got some code somewhere. Other functions which can interrogate the observational data can be found in <code>__init__.py</code>. These functions can calculate storm stats such as:
<ul>
<li>Maximum wind speed</li>
<li>Minimum central pressure</li>
<li>Lifetime</li>
<li>Formation date</li>
<li>Dissipation date</li>
<li>ACE index</li>
<li>etc....</li>
</ul>
<p></p>
<h2><a name="6. Troubleshooting"></a> 6. Troubleshooting</h2>
List any problems and solutions when running <code>ts_obs</code>here:
<ul>
<li>The module requires an auto-update script so that all the latest observations can be retrieved from the respective operational centres. At the moment some of the test data only runs to 2010.</li>
<li>It would be good to get more example images and code (e.g. include reanalysis datasets?)</li>
</ul>
<p></p>
<p></p>
<h2><a name="6. Contact"></a> 6. Contact</h2>
If you have any problems setting up the code then please contact <a href="mailto:joanne.camp@metoffice.gov.uk">Joanne Camp</a>.
<p></p>
<p></p>
<p></p>
<p></p>
<p></p>
<p></p>
-- <a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/JoanneCamp">JoanneCamp</a>- 04 Jun 2014
<p></p>
-- <a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a> - 2014-12-13</div>
<!-- /patternTopic-->
<div class="twikiContentFooter"></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div id="patternBottomBar">
<div id="patternBottomBarContents"><!--/patternWebBottomBar--></div>
<!-- /patternBottomBarContents--></div>
<!-- /patternBottomBar--></div>
<!-- /patternPage--></div>
<!-- /patternPageShadow--></div>
<!-- /patternScreen-->
