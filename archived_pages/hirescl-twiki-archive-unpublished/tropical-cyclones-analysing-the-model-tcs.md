---
date: 2020-09-28 16:25:51
description: 'Analysing TRACK output: TS_MODEL'
layout: base_hrcm
order: 19
permalink: /hirescl-twiki-archive-unpublished/tropical-cyclones-analysing-the-model-tcs/
title: 'Tropical cyclones: analysing the model TCs '
---

<p><span style="">Analysing TRACK output: TS_MODEL</span></p>
<div id="patternScreen">
<div id="patternPageShadow">
<div id="patternPage">
<div id="patternWrapper">
<div id="patternOuter">
<div id="patternFloatWrap">
<div id="patternMain">
<div id="patternMainContents">
<div class="patternContent">
<div class="patternTopic">This Twiki page contains information about the <code>ts_model</code>Python module and how to get it running on your local machine.
<p></p>
<div class="twikiToc">
<ul>
<li><a href="#Analysing TRACK output: TS_MODEL"> Analysing TRACK output: TS_MODEL</a>
<ul>
<li><a href="#1. About ts_model"> 1. About ts_model</a></li>
<li><a href="#2. Setting up ts_model"> 2. Setting up ts_model</a></li>
<li><a href="#3. What's in ts_model?"> 3. What's in ts_model?</a></li>
<li><a href="#4. Example code"> 4. Example code</a></li>
<li><a href="#5. Anything else?"> 5. Anything else?</a></li>
<li><a href="#6. Troubleshooting"> 6. Troubleshooting</a></li>
<li><a href="#7. Example images"> 7. Example images</a></li>
<li><a href="#8. Contact"> 8. Contact</a></li>
</ul>
</li>
</ul>
</div>
<p></p>
<h2><a name="1. About ts_model"></a> 1. About ts_model</h2>
<code>ts_model</code> is a Python module written by Joanne Camp to read in and analyse tracking output from Reading Universities <a href="http://www-twiki/Main/JoanneCampTRACK" target="_top">TRACK</a>algorithm.
<p></p>
<h2><a name="2. Setting up ts_model"></a> 2. Setting up ts_model</h2>
<code>ts_model</code> is stored under FCM in the repository: <code>svn://fcm9/GS_svn/TropicalStorms/trunk/ts_model</code>
<p></p>
<ol>
<li>Check out a working copy of this directory (note this will put a copy of <code>ts_model</code>in your current directory):
<ul>
<li>
<pre> fcm co svn://fcm9/GS_svn/TropicalStorms/trunk/ts_model . </pre>
</li>
</ul>
</li>
<li>You then need to set the <code>PYTHONPATH</code>so that Python can find your code:
<ul>
<li>
<pre> USER_SITE=${HOME}/.local/lib/python2.7/site-packages &amp;&amp; mkdir -p $USER_SITE &amp;&amp; echo `pwd` &gt; ${USER_SITE}/ts_model.pth </pre>
</li>
</ul>
</li>
</ol>
<p></p>
<h2><a name="3. What's in ts_model?"></a> 3. What's in ts_model?</h2>
inside <code>ts_model</code> you should find some python code (e.g. <code>track.py</code>, which reads in TRACK model output) and 3 sub-directories: <code>example_code</code>, <code>sample_data</code> and <code>tests</code>:<ol>
<li><code>example_code</code>:
<ul>
<li>Contains example functions that analyse TRACK output and produce example plots. <strong>This directory will be the most useful to you.</strong></li>
</ul>
</li>
<li><code>tests</code>:
<ul>
<li>This is where I've written tests for the main Python routines in this module. <strong>There should be no need to modify these.</strong></li>
</ul>
</li>
<li><code>sample_data</code>:
<ul>
<li>Contains sample TRACKing output files which are used to test code and create example plots.</li>
</ul>
</li>
</ol>
<p></p>
<h2><a name="4. Example code"></a> 4. Example code</h2>
You can have a go at running some of the <code>example_code</code> routines yourself - you just need to navigate to the <code>example_code</code>directory and type the name of the program:<ol>
<li><strong>storm_tracks.py</strong>
<ul>
<li><code>python2.7 storm_tracks.py</code></li>
<li>This program produces 4 individual plots of: storm tracks, storm genesis/formation locations, location of maximum wind speed and lysis/dissipation location for all storms from June-November 1986-2001. Note you have to close the window on the screen in order to produce the next plot. Plots are produced for the whole globe, but you can also see results for individual basins by setting the basin to <code>'na'</code> for the North Atlantic or <code>'ep'</code> for the Eastern Pacific etc. Basins available: North Atlantic (<code>'na'</code>), eastern Pacific (<code>'ep'</code>), [central Pacific (<code>'cp'</code>)], western Pacific (<code>'wp'</code>), North Indian Ocean (<code>'ni'</code>), Southwest Indian Ocean (<code>'si'</code>), Australian region (<code>'au'</code>) and the South Pacific (<code>'sp'</code>).</li>
</ul>
</li>
<li><strong>storm_density.py</strong>
<ul>
<li><code>python2.7 storm_density.py</code></li>
<li>Produces a global plot of monthly-mean tropical storm track density for the period June-November 2000-2011. [Strictly speaking it calculates feature density, as what it does is bin 6-hourly points into lat-lon boxes.]</li>
</ul>
</li>
<li><strong>monthly_variability.py</strong>
<ul>
<li><code>python2.7 monthly_variability.py</code></li>
<li>Produces the average number of storms per months over a pre-defined period as a bar chart and line plot. Example results are for the North Atlantic, but you can change this to any ocean basin (see list above).</li>
</ul>
</li>
<li><strong>monthly_variability_with_obs.py</strong>
<ul>
<li><code>python2.7 monthly_variability_with_obs.py</code></li>
<li>The same code as above, but automatically plots results for all ocean basins and overplots corresponding observations. Note you will need an additional module <code>ts_obs</code> in order for this to work.</li>
</ul>
</li>
</ol>
<p></p>
<h2><a name="5. Anything else?"></a> 5. Anything else?</h2>
I think most of the information that you may need to get from TRACK can be accessed via the test routines; however, if there is anything else that would be useful then please let me know - I've probably got some code somewhere. Other functions which can interrogate the TRACK output can be found in <code>__init__.py</code>. These functions can calculate storm stats such as:
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
List any problems and solutions when running <code>ts_model</code>here:
<ul>
<li>The program <strong>phony_datetime.py</strong> needs to be added.</li>
</ul>
<p></p>
<h2><a name="7. Example images"></a> 7. Example images</h2>
<img alt="storm_tracks.png" height="395" src="/twiki/pub/Project/HiResCL/TS_model/storm_tracks.png" width="640"> <img alt="storm_genesis.png" height="395" src="/twiki/pub/Project/HiResCL/TS_model/storm_genesis.png" width="640"><br> <img alt="storm_vmax.png" height="395" src="/twiki/pub/Project/HiResCL/TS_model/storm_vmax.png" width="640"> <img alt="storm_lysis.png" height="395" src="/twiki/pub/Project/HiResCL/TS_model/storm_lysis.png" width="640"><br> <img alt="storm_density.png" height="542" src="/twiki/pub/Project/HiResCL/TS_model/storm_density.png" width="657">
<p></p>
<h2><a name="8. Contact"></a> 8. Contact</h2>
If you have any problems setting up the code then please contact <a href="mailto:joanne.camp@metoffice.gov.uk">Joanne Camp</a>.
<p></p>
-- <a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/JoanneCamp">JoanneCamp</a>- 04 Jun 2014
<p></p>
<p></p>
-- <a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a> - 2014-12-13</div>
<!-- /patternTopic-->
<div class="twikiContentFooter"></div>
</div>
<!-- /patternContent--> <a name="topic-actions"></a>
<div class="patternTopicActions">
<div class="patternTopicAction"><span class="patternActionButtons"><span><a accesskey="e" href="https://collab.metoffice.gov.uk/twiki/bin/edit/Project/HiResCL/TS_model?t=1601310291" rel="nofollow" title="Edit this topic text"><span class="twikiAccessKey">E</span>dit</a></span><span class="twikiSeparator"> | </span><span><a accesskey="a" href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/TS_model" rel="nofollow" title="Attach an image or document to this topic"><span class="twikiAccessKey">A</span>ttach</a></span><span class="twikiSeparator"> | </span><span><a accesskey="p" href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/TS_model?cover=print" rel="nofollow" title="Printable version of this topic"><span class="twikiAccessKey">P</span>rint version</a></span><span class="twikiSeparator"> | </span><span><span><a accesskey="h" href="{{ site.baseurl }}/twiki/bin/rdiff/Project/HiResCL/TS_model?type=history" rel="nofollow" title="View total topic history"><span class="twikiAccessKey">H</span>istory</a></span>: r1</span><span class="twikiSeparator"> | </span><span><a accesskey="b" href="{{ site.baseurl }}/twiki/bin/oops/Project/HiResCL/TS_model?template=backlinksweb" rel="nofollow" title="Search the Project/HiResCL Web for topics that link to here"><span class="twikiAccessKey">B</span>acklinks</a></span><span class="twikiSeparator"> | </span><span><a accesskey="r" href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/TS_model?raw=on" rel="nofollow" title="View raw text without formatting"><span class="twikiAccessKey">R</span>aw View</a></span><span class="twikiSeparator"> | </span><span><a accesskey="w" href="https://collab.metoffice.gov.uk/twiki/bin/edit/Project/HiResCL/TS_model?t=1601310291;nowysiwyg=1" rel="nofollow" title="Raw Edit this topic text">Ra<span class="twikiAccessKey">w</span> edit</a></span><span class="twikiSeparator"> | </span><span><a accesskey="m" href="{{ site.baseurl }}/twiki/bin/oops/Project/HiResCL/TS_model?template=oopsmore&amp;param1=1&amp;param2=1" rel="nofollow" title="Delete or rename this topic; set parent topic; view and compare revisions"><span class="twikiAccessKey">M</span>ore topic actions</a></span></span></div>
<!--/patternTopicAction--></div>
<!--/patternTopicActions-->
<div class="patternInfo twikiGrayText">
<div class="patternRevInfo">Topic revision: r1 - 2014-12-13 - 17:51:23 - <a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></div>
<!-- /patternRevInfo-->
<div class="patternMoved"></div>
<!-- /patternMoved--></div>
<!-- /patternInfo--></div>
<!-- /patternMainContents--></div>
<!-- /patternMain-->
<div id="patternLeftBar">
<div id="patternClearHeaderLeft"></div>
<div id="patternLeftBarContents">
<div class="patternWebIndicator">
<ul>
<li><a class="twikiCurrentWebHomeLink twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/WebHome"><img align="top" alt="web-bg-small" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif" width="16"> Project/HiResCL</a></li>
</ul>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
