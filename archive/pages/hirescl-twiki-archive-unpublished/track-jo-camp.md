---
date: 2020-09-23 18:19:31
description: Welcome to TRACK! This Twiki page contains information about Reading
  University's TRACK algorithm and how to get it running on your local machine.
layout: base_hrcm
order: 1
permalink: /hirescl-twiki-archive-unpublished/track-jo-camp/
title: "TRACK \u2014 Jo Camp"
---

<p>Welcome to TRACK! This Twiki page contains information about Reading University's TRACK algorithm and how to get it running on your local machine.</p>
<p></p>
<div class="twikiToc">
<ul>
<li><a href="#Tropical storm tracking: TRACK"> Tropical storm tracking: TRACK</a>
<ul>
<li><a href="#1. About TRACK"> 1. About TRACK</a></li>
<li><a href="#2. Setting up TRACK"> 2. Setting up TRACK</a>
<ul>
<li>
<ul>
<li><a href="#2.1 Downloading TRACK from FCM"> 2.1 Downloading TRACK from FCM</a></li>
<li><a href="#2.2 Retrieve large files from MA"> 2.2 Retrieve large files from MASS &amp; create a track.tc file</a></li>
<li><a href="#2.3 Set environment variables"> 2.3 Set environment variables</a></li>
<li><a href="#2.4 Create directories"> 2.4 Create directories</a></li>
<li><a href="#2.5 Check tracking programs are"> 2.5 Check tracking programs are present</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#3. Getting data"> 3. Getting data</a></li>
<li><a href="#4. Running TRACK"> 4. Running TRACK</a></li>
<li><a href="#5. **USEFUL SCRIPTS**"> 5. *USEFUL SCRIPTS*</a></li>
<li><a href="#6. TRACK output"> 6. TRACK output</a></li>
<li><a href="#7. Housekeeping"> 7. Housekeeping</a></li>
<li><a href="#8. Useful Twiki pages"> 8. Useful Twiki pages</a></li>
<li><a href="#9. Who is using TRACK?"> 9. Who is using TRACK?</a></li>
<li><a href="#10. External platforms"> 10. External platforms</a></li>
<li><a href="#11. TRAC changes"> 11. TRAC changes</a></li>
<li><a href="#12. Troubleshooting"> 12. Troubleshooting</a></li>
<li><a href="#13. References"> 13. References</a></li>
</ul>
</li>
</ul>
</div>
<p></p>
<h2><a name="1. About TRACK"></a> 1. About TRACK</h2>
<p>TRACK is a feature based tracking algorithm used to track tropical storms in models as well as reanalysis datasets such as ERA-Interim, JRA25 and MERRA. Full details of the tracking algorithm can be found in Hodges (<a href="http://journals.ametsoc.org/doi/pdf/10.1175/1520-0493%281995%29123%3C3458%3AFTOTUS%3E2.0.CO%3B2" target="_top">1995</a>,<a href="http://journals.ametsoc.org/doi/pdf/10.1175/1520-0493%281996%29124%3C2914%3ASNEATT%3E2.0.CO%3B2" target="_top">1996</a>,<a href="http://journals.ametsoc.org/doi/pdf/10.1175/1520-0493%281999%29127%3C1362%3AACFFT%3E2.0.CO%3B2" target="_top">1999</a>) and <a href="http://www.tellusa.net/index.php/tellusa/article/download/15121/16940" target="_top">Bengtsson et al (2007)</a>. Recent work using TRACK includes <a href="http://journals.ametsoc.org/doi/pdf/10.1175/JCLI-D-12-00012.1" target="_top">Strachan et al (2013)</a> and, using the Met Office setup (<strong>TRACK vn 1.4.0</strong>), in <a href="http://journals.ametsoc.org/doi/full/10.1175/JCLI-D-14-00131.1" target="_top">Roberts et al (2015)</a> and <a href="http://www-hc/~hadjn/papers/Tropical_cyclones_in_GloSea5_qjrms.pdf" target="_top">Camp et al (2015)</a>.</p>
<p></p>
<p><strong>Data: TRACK requires 6-hourly fields of MSLP and u and v winds at 925, 850, 500, 300, 200hPa.</strong> If you have them, then the filtered vorticity files are also extremely useful as these can speed up the tracking process (note these are currently only available for <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/GloSea5?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="GloSea5 (this topic does not yet exist; you can create it)">GloSea5</a></span>data; the stash codes you need are 30455, 30456, 30457 and 30458. 30455=Vorticity 850 hPa, 30456=Filtered vorticity 850hPa, 30457=vorticity TC, 30458=filtered vorticity TC).</p>
<p></p>
<h2><a name="2. Setting up TRACK"></a> 2. Setting up TRACK</h2>
<h4><a name="2.1 Downloading TRACK from FCM"></a> 2.1 Downloading TRACK from FCM</h4>
<p><strong>TRACK is stored under FCM in the repository:</strong> <code>svn://fcm9/GS_svn/GS_PP/branches/dev/hadjn/r1126_TropicalStormProcessing/python/modules/TRACK</code></p>
<p></p>
<ol>
<li>Check out a working copy of this repository into a directory of your choice. You can place it in any subdirectory or on another disc (e.g. <code>/project</code> or <code>JASMIN</code>) if you prefer:
<ul>
<li>
<pre> mkdir TRACK </pre>
</li>
<li>
<pre> fcm co svn://fcm9/GS_svn/GS_PP/branches/dev/hadjn/r1126_TropicalStormProcessing/python/modules/TRACK TRACK/ </pre>
</li>
</ul>
</li>
<li>Then set the <code>PYTHONPATH</code>so that Python can find your code:
<ul>
<li>
<pre> USER_SITE=${HOME}/.local/lib/python2.7/site-packages &amp;&amp; mkdir -p $USER_SITE &amp;&amp; echo `pwd` &gt; ${USER_SITE}/TRACK.pth </pre>
</li>
<li>IMPORTANT - do not <code>cd TRACK</code> before running this command (it needs to be set in the directory above TRACK, not in TRACK itself).</li>
</ul>
</li>
</ol>
<p></p>
<ul>
<li>If everything has worked then inside <code>TRACK</code> you should find some python code and various sub-directories (such as <code>programs</code> and <code>indat</code>).
<ul>
<li>The sub-directories store the original TRACK programs (written in Fortran) and calling scripts. <strong>You should not need to modify any of the files or programs in the subdirectories</strong>.</li>
</ul>
</li>
</ul>
<p></p>
<p></p>
<h4><a name="2.2 Retrieve large files from MA"></a> 2.2 Retrieve large files from MASS &amp; create a track.tc file</h4>
<p>Now you have a copy of <code>TRACK</code> you are ready to set it up for your data. The first thing you need to do is run the script <strong>setup_track.py</strong>. This retrieves all the large/binary data files from MASS which are required to run TRACK but couldn't be stored under FCM (such as the spectral files). It also automatically creates a <strong>track.tc</strong>file, which is a compiled fortran program used for tracking. Make sure the script successfully downloads the spectral files and a track.tc file has been created before moving onto the next step.</p>
<pre>python2.7 setup_track.py
ls programs/spectral/
ls programs/track.tc
</pre>
<p></p>
<h4><a name="2.3 Set environment variables"></a> 2.3 Set environment variables</h4>
<p>All of the variables used to run TRACK are set in either <strong>config/default.cfg</strong> (if you are using the full version of TRACK) or <strong>config/vort_diags.cfg</strong> (if you are using the extra vorticity diagnostics e.g. <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/GloSea5?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="GloSea5 (this topic does not yet exist; you can create it)">GloSea5</a></span> data - see section 1 for more details). Take a copy of the config file relevant to you (save it as any name you'd like e.g. <code>my_config.cfg</code>) and update all the variables and directories. Once these are defined, these variables are then passed automatically to all the TRACK routines via the program <strong>config.py</strong>.</p>
<pre> cp config/default.cfg config/my_config.cfg</pre>
<p>or</p>
<pre> cp config/vort_diags.cfg config/my_config.cfg</pre>
<p></p>
<p></p>
<h4><a name="2.4 Create directories"></a> 2.4 Create directories</h4>
<p>Create the directory structure used to store the tracking output by running <strong>create_track_directories.py</strong>. This goes through each of the directories you defined in your config file e.g. <code>my_config.cfg</code> and checks they exist. It then creates any of the directories which are not already set up. The program also creates a symbolic link to the <strong>outdat</strong> directory. Check this is setup correctly and that it contains the subdirectory <strong>track_scr</strong> before proceeding. The <strong>track_scr</strong>directory will contain the script output from the tracking algorithm i.e. if your tracking fails - or you want to see how it is progressing - then the information will be stored in here.</p>
<pre>python2.7 create_track_directories.py --config=config/my_config.cfg
ls outdat/
ls outdat/track_scr/
</pre>
<p></p>
<h4><a name="2.5 Check tracking programs are"></a> 2.5 Check tracking programs are present</h4>
<p>As soon as you have set your variables you need to check that all the TRACK programs and files are present for the resolution of the data you are running. You can find this out by running <strong>check_track_programs.py</strong>. This will run through all the TRACK directories and make sure the files you need are there. If there are missing files then speak to <a href="mailto:joanne.camp@metoffice.gov.uk">Joanne Camp</a> or <a href="mailto:malcolm.roberts@metoffice.gov.uk">Malcolm Roberts</a>as these may need to be created for the resolution you are running. If all the files are present then you're ready to start getting your data.</p>
<p></p>
<p><code>python2.7 check_track_programs.py --config=config/my_config.cfg</code></p>
<p></p>
<p></p>
<h2><a name="3. Getting data"></a> 3. Getting data</h2>
<p>TRACK requires <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> data in order to run. <strong>The files should contain 6-hourly MSLP and u and v winds at 925, 850, 500, 300, 200hPa (plus the extra vorticity data if you have it - see section 1). You need ONE FILE per ensemble member and year.</strong> TRACK cannot work with small files and then join the results together. Unless you're lucky and already have <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> data, you will need to create it. An example program, which retrieves <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/GloSea5?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="GloSea5 (this topic does not yet exist; you can create it)">GloSea5</a></span> pp data from MASS-R, is <strong>get_tracking_data.py</strong>. Take a look at this and modify it for your needs. You may want to take a copy first so that you always have one working version. To run this program and download some <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/GloSea5?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="GloSea5 (this topic does not yet exist; you can create it)">GloSea5</a></span>data, type:</p>
<p></p>
<p><code>python2.7 get_tracking_data.py --config=config/my_config.cfg</code></p>
<p></p>
<p>This will download pp data into your <code>PP_DATA_DIR</code>. As soon as you have some pp data then you need to convert it to <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> using the program <strong>convert_pp_to_netcdf.py</strong>. This goes through each of the pp files in your <code>PP_DATA_DIR</code> converting any files which do not already have <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> output. The <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> data are placed in your <code>NC_DATA_DIR</code>. The program also creates output directories for each <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span>file (these directories are used to store TRACK data later on).</p>
<p></p>
<p><code>python2.7 convert_pp_to_netcdf.py  --config=config/my_config.cfg</code></p>
<p></p>
<p></p>
<h2><a name="4. Running TRACK"></a> 4. Running TRACK</h2>
<p>Once you have some <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> data you are ready to run TRACK. The main script for running TRACK is called <strong>run_track.py</strong>. If you run this script it will automatically run TRACK on all the <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> files in your <code>NC_DATA_DIR</code> which do not already have tracking output. You can monitor the progress of TRACK for each <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> file by checking the script output in <code>/outdat/track_scr</code> (there is one file per member per hemisphere). All TRACK output is placed in your <code>OUTPUT_DIR</code> (defined in <code>my_config.cfg</code>) and (if defined) a copy of the final tracking file is also placed in your <code>RESULTS_DIR</code> (defined in <code>my_config.cfg</code>).</p>
<p></p>
<pre>python2.7 run_track.py --config=config/my_config.cfg
ls outdat/track_scr/
</pre>
<p></p>
<p></p>
<h2><a name="5. <strong>*USEFUL SCRIPTS**"></a> 5. **USEFUL SCRIPTS*</h2>
<p>For testing purposes it was necessary to set up some scripts that could test each stage of the TRACK process (e.g. the pp to <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> converter, tracking script etc.) on one (or a select number of) files at a time. I have therefore written a couple of new scripts, which are stored in <code>TRACK/scripts</code> to help this process. Note: These should be run directly from the <code>TRACK</code>directory:</p>
<ol>
<li><code>cd TRACK</code></li>
<li><strong>scripts/convert_pp_file_to_netcdf.py</strong>
<ul>
<li>Script for converting pp file(s) to <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> . Input: the full pathname of a pp file. This can work on one or more files at the same time.</li>
<li>
<pre> python2.7 scripts/convert_pp_file_to_netcdf.py --config=config/my_config.cfg fname.pp </pre>
</li>
<li>
<pre> python2.7 scripts/convert_pp_file_to_netcdf.py --config=config/my_config.cfg fname1.pp fname2.pp fname3.pp </pre>
</li>
</ul>
</li>
</ol>
<p></p>
<ol>
<li><strong>scripts/track_a_file.py</strong>
<ul>
<li>Script for running TRACK on a given <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> file(s). Input: the full pathname of a <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> file. This can work on one or more files at the same time.</li>
<li>
<pre> python2.7 scripts/track_a_file.py --config=config/my_config.cfg fname.nc </pre>
</li>
<li>
<pre> python2.7 scripts/track_a_file.py --config=config/my_config.cfg fname1.nc fname2.nc fname3.nc </pre>
</li>
</ul>
</li>
</ol>
<p></p>
<ol>
<li><strong>scripts/convert_and_track_file.py</strong>
<ul>
<li>Script for testing the whole TRACK process. Input: the full pathname of a pp file. Script process: 1) converts pp file to <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> , 2) runs <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> file through TRACK, 3) copies results to results directory, 4) performs housekeeping.</li>
<li>
<pre>python2.7 scripts/convert_and_track_file.py --config=config/my_config.cfg fname.pp </pre>
</li>
</ul>
</li>
</ol>
<p></p>
<p></p>
<h2><a name="6. TRACK output"></a> 6. TRACK output</h2>
<p>TRACK outputs a lot of files - you probably only need to keep 2 of them. These files are the final tracking output: they provide the position and intensity (mslp, vorticity maxima and wind speed) of each warm-cored tropical storm feature in the model. There are two output files per <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> file: one for the Northern Hemisphere and one for the Southern Hemisphere. These files are placed in your <code>OUTPUT_DIR</code> (defined in <code>my_config.cfg</code>) in the NH and SH sub-directories:</p>
<p></p>
<pre>ls ${OUTPUT_DIR}/NH/
ls ${OUTPUT_DIR}/SH/
</pre>
<p></p>
<p>The files you are after are of the format:</p>
<pre>${NC_FNAME}.warm_core.NH.tracks
${NC_FNAME}.warm_core.SH.tracks
</pre>
<p></p>
<p>where $NC_FNAME is the <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> filename. Open one of these files and take a look at the output. If you have set your <code>RESULTS_DIR</code> (defined in <code>my_config.cfg</code>), then a copy of these final tracking files will be placed in here automatically.</p>
<p></p>
<p>The output from these files is quite complex. Details about what is contained in the TRACK output files can be found on Malcolm's Twiki page: <a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/CAPTIVATE/TCAnalysisTRACKDetails" target="_top">TRACK output details</a>. To analyse your tracking data you need two other Python modules called <code>ts_model</code> and <code>ts_obs</code>. To get a copy of this code see the <a href="http://www-twiki/Main/JoanneCampTSModel" target="_top">TSModel</a> and <a href="http://www-twiki/Main/JoanneCampTSObs" target="_top">TSObs</a>Twiki help pages. This will help you plot the tracking data and compare it with observations.</p>
<p></p>
<h2><a name="7. Housekeeping"></a> 7. Housekeeping</h2>
<p>When you have finished running TRACK you can delete a lot of the output/data files which are no longer needed. The program <strong>housekeeping.py</strong> will go through the <code>TRACK</code>, <code>/programs</code>, <code>/indat</code> and <code>/outdat</code> directories and remove any unnecessary files. If you've set a <code>RESULTS_DIR</code> in your config file (i.e. a central location to store the final tracking output files), you can also get <strong>housekeeping.py</strong> to automatically delete the original tracking output directories which are created for each <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span>file. This is recommended if you are running lots of data as TRACK takes up a large(!!!) amount of space.</p>
<p></p>
<ul>
<li><code>python2.7 housekeeping.py --config=config/my_config.cfg</code></li>
</ul>
<p></p>
<h2><a name="8. Useful Twiki pages"></a> 8. Useful Twiki pages</h2>
<p>List other useful Twiki pages related to TRACK here. Note these may need password access.</p>
<ul>
<li>Testing TRACK with Claudio's vorticity diagnostics and changes to <code>track_vort.scr</code> to get these working with <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/GloSea5?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="GloSea5 (this topic does not yet exist; you can create it)">GloSea5</a></span> data: <a href="http://collab.metoffice.gov.uk/twiki/bin/view/Development/TestingClaudioMethod" target="_top">http://collab.metoffice.gov.uk/twiki/bin/view/Development/TestingClaudioMethod</a></li>
<li>TRACK output information: <a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/CAPTIVATE/TCAnalysisTRACKDetails" target="_top">http://collab.metoffice.gov.uk/twiki/bin/view/Project/CAPTIVATE/TCAnalysisTRACKDetails</a></li>
<li>Compiling track on different platforms: <a href="http://www-twiki/Main/MalcolmRobertsTCTracking" target="_top">http://www-twiki/Main/MalcolmRobertsTCTracking</a></li>
<li><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLJoanneCampTRACK/TRACK_processing.doc" target="_top">TRACK processing for GloSea5</a> (Word document)</li>
</ul>
<p></p>
<h2><a name="9. Who is using TRACK?"></a> 9. Who is using TRACK?</h2>
<p>Add your name to this list if you are using the TRACKing package:</p>
<ul>
<li>Joanne Camp, Malcolm Roberts, Ruth McDonald, Leon Hermanson, Richard Hattersley, Phil Davis (GloSea team).</li>
</ul>
<p></p>
<h2><a name="10. External platforms"></a> 10. External platforms</h2>
<p>Note any requirements for getting TRACK running on external platforms e.g. JASMIN, LOTUS here:</p>
<ul>
<li>The file config/default.cfg can be copied and modified for different machines. This allows a setup file for each configuration to be stored in FCM.</li>
<li>in track.scr, would prefer than for links in indat, these are remade rather than tested for existence - if the files exist, they will relink, but in case they are in error then would prefer to relink them. Important for a slower file system such as lotus.</li>
<li>for climate, need to do NH and SH as one job with loops within track.scr, since they both rely on the same vorticity etc fields being calculated but then do the tracking etc individually. In this case, also need the files in indat to reflect the hemisphere, since if running on a platform where the mv command takes time, the hemisphere files are the same name and can be confused.</li>
</ul>
<p></p>
<h2><a name="11. TRAC changes"></a> 11. TRAC changes</h2>
<p>List TRAC pages which document changes made to <code>TRACK-1.4.0</code>in FCM here:</p>
<ul>
<li>Creating and adding <code>TRACK-1.4.0</code> module: <a href="http://fcm1.metoffice.com/projects/GS/ticket/509" target="_top">http://fcm1.metoffice.com/projects/GS/ticket/509</a></li>
<li>Fixing <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> data conversion errors in <strong>convert_pp_to_netcdf</strong>: <a href="http://fcm1.metoffice.com/projects/GS/ticket/535" target="_top">http://fcm1.metoffice.com/projects/GS/ticket/535</a></li>
<li>Fixing memory and tracking problems in <strong>run_glosea5_track</strong>: <a href="http://fcm1.metoffice.com/projects/GS/ticket/537" target="_top">http://fcm1.metoffice.com/projects/GS/ticket/537</a></li>
<li>Major changes to TRACK including directory name change, addition of configuration files, simplified <strong>run_track</strong> and <strong>convert_pp_to_netcdf</strong> programs, created scripts to test data conversion <strong>convert_pp_file_to_netcdf</strong> and TRACK on individual files <strong>test_run_glosea5_track</strong>: <a href="http://fcm1.metoffice.com/projects/GS/ticket/603" target="_top">http://fcm1.metoffice.com/projects/GS/ticket/603</a></li>
<li>Bolting on Claudio's vorticity diagnostics: <a href="http://fcm1.metoffice.com/projects/GS/ticket/604" target="_top">http://fcm1.metoffice.com/projects/GS/ticket/604</a> (and also <a href="http://collab.metoffice.gov.uk/twiki/bin/view/Development/TestingClaudioMethod" target="_top">http://collab.metoffice.gov.uk/twiki/bin/view/Development/TestingClaudioMethod</a>)</li>
<li>Automating <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/GloSea5?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="GloSea5 (this topic does not yet exist; you can create it)">GloSea5</a></span> data retrieval and tracking: <a href="http://fcm1.metoffice.com/projects/GS/ticket/627" target="_top">http://fcm1.metoffice.com/projects/GS/ticket/627</a></li>
</ul>
<p></p>
<h2><a name="12. Troubleshooting"></a> 12. Troubleshooting</h2>
<p>List any problems and solutions when running <code>TRACK-1.4.0</code>here:</p>
<ul>
<li><code>NH/DJF_MAX_14/tdump: No such file or directory</code>
<ul>
<li>These errors appear if the length of your data is too short (e.g. this error appeared when testing on 10 day data). This is because it uses 14 processors for tracking, so if your data isn't long enough it can't allocate any data to this processor. Hence the directory is empty and no output is produced. Solution: we made the data length longer. Leon tried modifying the 14 processors part.</li>
</ul>
</li>
<li><code>Cannot remove file [filename], directory in use</code>
<ul>
<li>If the tracking script is trying to delete results in your output directory e.g. <code>output_dir/NH/DJF_MAX_1</code> and it doesn't work, then it is possible the directory has been locked. Do an <code>ls -la</code> in the problem directory. Do you have a file beginning with <code>.nfs</code>? If so, log onto another machine and delete this file. For some reasont the processor has got confused and it cannot delete this file itself. Then run the program <code>run_track.py</code> again. Hopefully it will now work.</li>
</ul>
</li>
<li>The program <strong>get_tracking_data.py</strong> appears to be missing from FCM. <code>Jo:</code> Program added to FCM.</li>
<li>Variables need to be renamed in <strong>check_track_programs.py</strong>: RESOL to RESOLUTION and NO_VERT_LEVELS to NLEVELS. <code>Jo:</code> Updated and added to FCM.</li>
<li><strong>TO DO</strong> Data length comment from Ruth: I see that you and Leon have had problems with files of 10 days. I used 6 days of data once for mid latitude tracks and had to change the call to master_ml. I used -n=1,24,1 for 3 months of 6 hourly data so the tracking was done in one process. I'm not sure if this will work for 10 days, it might need two processes. Kevin would know. <code>Jo:</code> It would be good to look at this as using short data lengths should be made possible e.g. for testing etc. Malcolm and I have just been running 7-day data using TRACK, like Ruth we modified the call to master_tc. I'll try and document this somewhere.</li>
<li><strong>TO DO</strong> track.tc error: <code>~TRACK-1.4.0/programs/track.tc: error while loading shared libraries: libnetcdf.so.7: cannot open shared object file: No such file or directory</code>. Ruth: I had to add <code>/project/ukmo/rhel6/netcdf4/ifort_composerxe/lib</code> to my <code>LD_LIBRARY_PATH</code>. <code>Jo:</code> Perhaps LD_LIBRARY_PATH should be set in <code>setup_track.py</code>?</li>
<li><strong>TO DO</strong> the package assumes a real day calendar rather than 360 day - need to replace the storm_date executable with the 360 day equivalent, and ideally test the nc file for which one is appropriate.</li>
<li>The function rstrip(".nc") used in various places has caused me problems - it does not simply remove ".nc" from the end of a filename, it removes all these characters in any order. I don't know if there is something better than my file[:-3] replacement? <code>Jo:</code> I have checked the documentation for rstrip and it should just remove the last characters in the string. I have tested it on a couple of filenames and i've not had any problems.</li>
<li><strong>FIXED</strong> the pp to <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> file conversion program <code>pp2nc.tcl</code> seems to wait for 20 minutes before actually converting the file. This is not necessary and can therefore be removed. This will speed up the data conversion substantially. <code>Jo:</code> This has been fixed andthe problem resolved.</li>
<li><strong>FIXED</strong> the script <code>track.scr</code> has a bug which meant thatm, when running the northern and southern hemisphere together, the files in /indat were not necessarily pointing to the correct hemisphere. As a result the NH files sometimes appeared in the SH directory. This is now fixed - all soft links that have been made previously are removed and then re-created. This seems to have solved the problem.</li>
<li><strong>TO DO</strong> <code>namelist_maker</code> needs to be linked to the config files and hard coded information removed.</li>
<li><strong>FIXED</strong> Field ID values incorrect when creating one <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NetCDF?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="NetCDF (this topic does not yet exist; you can create it)">NetCDF</a></span> file with extra vorticity data. <code>Jo:</code> fixes have been put in place which are viewable <a href="http://collab.metoffice.gov.uk/twiki/bin/view/Development/TestingClaudioMethod" target="_top">here</a>.</li>
<li><strong>TO DO</strong>. Add Malcolm's new track script to FCM ~hadom/workspace/track/tracking_script.py.</li>
</ul>
<p></p>
<h2><a name="13. References"></a> 13. References</h2>
<p><a href="http://www.tellusa.net/index.php/tellusa/article/download/15121/16940" target="_top">Bengtsson, L. et al (2007)</a>. How may tropical cyclones change in a warmer climate?. Tellus A, vol. 59, no. 4, 539-561. <br> <a href="http://www-hc/~hadjn/papers/Tropical_storms_GloSea5.pdf" target="_top">Camp, J. et al. (2015)</a>. Seasonal forecasting of tropical storms using the Met Office <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/GloSea5?topicparent=Project/HiResCL.HiResCLJoanneCampTRACK" rel="nofollow" title="GloSea5 (this topic does not yet exist; you can create it)">GloSea5</a></span> seasonal forecast system. Q. J. R. Meteorol. Soc. (In print). <br> <a href="http://journals.ametsoc.org/doi/pdf/10.1175/1520-0493%281995%29123%3C3458%3AFTOTUS%3E2.0.CO%3B2" target="_top">Hodges, K. (1995)</a>. Feature Tracking on the Unit Sphere. Mon. Wea. Rev., vol. 123, no. 12, 3458-3465. <br> <a href="http://journals.ametsoc.org/doi/pdf/10.1175/1520-0493%281996%29124%3C2914%3ASNEATT%3E2.0.CO%3B2" target="_top">Hodges, K. (1996)</a>. Spherical Nonparametric Estimators Applied to the UGAMP Model Integration for AMIP. Mon. Wea. Rev., vol. 124, no. 12, 2914-2932. <br> <a href="http://journals.ametsoc.org/doi/pdf/10.1175/1520-0493%281999%29127%3C1362%3AACFFT%3E2.0.CO%3B2" target="_top">Hodges, K. (1999)</a>. Adaptive Constraints for Feature Tracking. Mon. Wea. Rev., vol. 127, no. 6, 1362-1373. <br> <a href="http://journals.ametsoc.org/doi/full/10.1175/JCLI-D-14-00131.1" target="_top">Roberts, M. et al. (2015)</a>. Tropical cyclones in the UPSCALE ensemble of high resolution global climate models. J. Climate, 28, 574–596. <br> <a href="http://journals.ametsoc.org/doi/pdf/10.1175/JCLI-D-12-00012.1" target="_top">Strachan, J. et al (2013)</a>. Investigating Global Tropical Cyclone Activity with a Hierarchy of AGCMs: The Role of Model Resolution. J. Climate, vol. 26, no. 1, 133-152.</p>
<p></p>
<p>-- <a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/JoanneCamp">JoanneCamp</a>- 27 Jul 2015</p>
<p></p>
