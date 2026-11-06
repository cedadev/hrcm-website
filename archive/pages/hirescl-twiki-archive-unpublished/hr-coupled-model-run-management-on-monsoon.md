---
date: 2020-09-28 09:35:16.534000
description: 'Procedure for restarting an N216O025 coupled model following a (GPS)
  crash

  Examples below will be illustrated using the runid xfhhk(the high res coupled model
  from the second CAPTIVATE assessment)'
layout: base_hrcm
order: 9
permalink: /hirescl-twiki-archive-unpublished/hr-coupled-model-run-management-on-monsoon/
title: HR coupled model run management on MONSooN
---

<h1>Procedure for restarting an N216O025 coupled model following a (GPS) crash</h1>
<p>Examples below will be illustrated using the runid <a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/CAPTIVATE/HadGEM3Hxfhhk" target="_top">xfhhk</a>(the high res coupled model from the second CAPTIVATE assessment)</p>
<p></p>
<div class="twikiToc">
<ul>
<li><a href="#Procedure for Restarting the _N"> Procedure for Restarting the N216O025 coupled model following a crash</a>
<ul>
<li><a href="#1. Check reason for failure and"> 1. Check reason for failure and choose date to restart from</a></li>
<li><a href="#2. Prepare run directory for res"> 2. Prepare run directory for restart</a></li>
<li><a href="#3. Prepare NEMO and CICE restart"> 3. Prepare NEMO and CICE restart dumps</a></li>
<li><a href="#4. Edit the UMUI job"> 4. Edit the UMUI job</a></li>
<li><a href="#5. Submit the NRUN through the U"> 5. Submit the NRUN through the UMUI</a></li>
<li><a href="#6. Check on NRUN and submit CRUN"> 6. Check on NRUN and submit CRUN through UMUI</a></li>
<li><a href="#7. Check on production of annual"> 7. Check on production of annual and seasonal means by the UM</a></li>
<li><a href="#8. Final tidy up"> 8. Final tidy up</a></li>
</ul>
</li>
</ul>
</div>
<p></p>
<h2><a name="1. Check reason for failure and"></a> 1. Check reason for failure and choose date to restart from</h2>
<p></p>
<p>Look at output files and various fields in the restart dumps. Most of the time a crash is due to a grid point storm (GPS) and will show up as a divide by zero (SIGFPE error) in the UM output. Check the most recent restart dump; look at field 69 "W COMPNT OF WIND AFTER TIMESTEP" and plot data at around 3000m. Fields labelled "WBIG Set to 1 if w GT ?.?m/s" (typically 493 and 494) can also be useful when diagnosing strong GPS.</p>
<p></p>
<p>If there are strong, localised features then have a look at previous dumps to determine the spin up time of the problem (multiple dumps can be read into xconv and t-z plots can be produced for individual points to look at spin up of the problem). A strong GPS may require a job to be restarted from a few months back and given a significant "kick" to avoid repetition of the problem.</p>
<p></p>
<p>If there is no obvious problem in the restart dumps (more common than not) then the job can be restarted from dumps for the beginning of the current month with a weak &amp; brief "kick".</p>
<p></p>
<h2><a name="2. Prepare run directory for res"></a> 2. Prepare run directory for restart</h2>
<p></p>
<p>It is wise to clean up the ocean and ice output in the run directory before restarting the model. The UM is much better than NEMO &amp; CICE at coping with a restart so you shouldn't need to move its data around at all.</p>
<p></p>
<p>If you are intending to share the maintenance of this run with another user in your group it will make life easier if you run the command <code>umask 002</code>in each session in which you are working. This will set up the unix permissions such that anyone in your group will be able to manage the files you create.</p>
<p></p>
<p>Start by moving all ocean and ice output to a temporary directory, e.g.</p>
<p></p>
<pre>cd /projects/hirescm/msmizi/xfhhk/
mkdir tmp
mv xfhhko* xfhhki* tmp </pre>
<p></p>
<p>Then create a new directory to house the restart files for NEMO and CICE</p>
<p></p>
<p><code>mkdir restart_199902</code></p>
<p></p>
<h2><a name="3. Prepare NEMO and CICE restart"></a> 3. Prepare NEMO and CICE restart dumps</h2>
<p></p>
<p>The nemo dump needs to be reconstructed from the files produced by individual processors. The syntax is as follows;</p>
<p></p>
<p>~msmizi/bin/rebuild_nemo [stem of restart filename] [number of processors]</p>
<p></p>
<p>For example</p>
<p></p>
<p><code>~msmizi/bin/rebuild_nemo xfhhko_19990130_restart 80</code></p>
<p></p>
<p>will read in files named xfhhko_19990130_restart_00XX.nc (XX=00 to 79) and will merge each file together creating the file xfhhko_19990130_restart.nc in which each field is globally complete. This file should be moved to the restart directory created in the previous step.</p>
<p></p>
<p>Note: the path to rebuild_nemo above is simply a link to /projects/hirescm/hadgem3/scripts/vn7.7/nemo3.2/rebuild_nemo</p>
<p></p>
<p>Note 2: NEMO restart dumps are dated by the day just completed rather than by the day about to start (as used by CICE and the UM)</p>
<p></p>
<p>The CICE restart dump is dealt with differently; it is a single file which needs a slight alteration to the dates written into the file header in order to prevent new output files being written with incorrect dates. This alteration is performed by the modify_CICE_header program (Fortran). To run this tool you need to know the grid you are working on, the number of days per year (currently 360 for all coupled climate models), the date in the year to which the file relates and the length of the timestep used by NEMO-CICE (1350s for ORCA025 models).</p>
<p></p>
<p><code>$ ~msmizi/bin/modify_CICE_header</code> <br><span color="#800000" style="">Enter input file name: </span><br> <code>xfhhki.restart.1999-02-01-00000</code> <br><span color="#800000" style="">Enter output file name: </span><br> <code>xfhhki.restart.1999-02-01-00000.hacked</code> <br><span color="#800000" style="">Please enter the name of the grid used in this file choose from ORCA2, ORCA1, ORCA025, CUSTOM (note case) </span><br> <code>ORCA025</code> <br><span color="#800000" style="">Please enter the number of days in the year to which the restart dump relates </span><br> <code>360</code> <br><span color="#800000" style="">Please enter the day and month (format DD MM) to which the CICE restart dump relates (i.e. the date in the filename) </span><br> <code>01 02</code> <br><span color="#800000" style="">Please enter the length of the integration timestep in seconds </span><br> <code>1350</code></p>
<p></p>
<p><span color="#800000" style=""><span color="#800000" style="">Original time header variables: <br> istep0: 24960 <br> time: 33696000.0000000000 <br>time_forc: 20736000.0000000000</span></span></p>
<p></p>
<p><span color="#800000" style=""><span color="#800000" style="">Calculated time header variables: <br> istep0: 1920 <br> time: 2592000.00000000000 <br>time_forc: 20736000.0000000000</span></span></p>
<p></p>
<p><span color="#800000" style="">Enter Y to use these values or N to set them yourself </span><br> <code>Y</code></p>
<p></p>
<p><span color="#800000" style=""><span color="#800000" style="">Writing modified data to xfhhki.restart.1999-02-01-00000.hacked<br> istep0 changed from 24960 to 1920 <br>time changed from 33696000.0000000000 to 2592000.00000000000</span></span></p>
<p></p>
<p><span color="#800000" style="">Output complete.</span></p>
<p></p>
<p>Note: modify_CICE_header can also be found under /projects/hirescm/hadgem3/scripts/vn7.7/misc/</p>
<p></p>
<p>Move the new CICE restart file to the restart directory created in step 2.</p>
<h2><a name="4. Edit the UMUI job"></a> 4. Edit the UMUI job</h2>
<p></p>
<p>The following settings need to be changed in the UMUI;</p>
<ul>
<li><em>User information -&gt; General details</em> : chang the target machine user id if necessary</li>
<li><em>Input/Output control -&gt; User hand edits</em> : change the include flag beside crun.ed to N</li>
<li><em>Atmosphere -&gt; Ancillary and Input data files -&gt; Start dump</em> : set the date appropriately and enter the file name of the atmosphere dump to pick up, e.g. xfhhka.daj9210</li>
<li><em>NEMO -&gt; Scientific Parameters -&gt; Links to NEMO model</em> : Change the "NEMO start dump" field to point to the NEMO dump just created, e.g. enter <code>$DATAW/restart_199902/xfhhko_19990130_restart.nc</code></li>
<li>CICE -&gt; Scientific Parameters -&gt; Links to CICE model : Change the "CICE start dump" field to point to the CICE dump just created, e.g. <code>$DATAW/restart_199902/xfhhki.restart.1999-02-01-00000.hacked</code></li>
</ul>
<p></p>
<p>Save and Process the job, <strong>but do not submit</strong>.</p>
<p></p>
<p>Alter the W_CAPE_LIMIT and W_CONV_LIMIT variables in the CNTLATM file in the umui_jobs directory on PUMA. The hand edit ~matthew_miz/umui_jobs/hand_edits/W_cape_and_conv_from_0_5_to_0_3.ed can be used via the unix shell if deemed suitable.</p>
<h2><a name="5. Submit the NRUN through the U"></a> 5. Submit the NRUN through the UMUI</h2>
<p></p>
<p>Hit the submit button in the UMUI and enter login credentials when requested.</p>
<p></p>
<p>Once the job has started running, i.e. once the file time.step in the run directory has started updating every few second, the tmp directory can be dealt with; move the monthly/seasonal/annual ocean and ice mean output files from the tmp directory back into the run directory <strong>being careful to exclude any file containing data which will be overwritten by the model as it progresses</strong>. Any ocean/ice 10d files can be deleted from the tmp directory. Daily ice data from before the crash should be moved to the archive/ind.nc.file directory</p>
<p></p>
<p>If any restart data corresponding to the beginning of December or the beginning of September remains in the directory the restart files should be rebuilt as described in step 3 with the resulting output moved to $DATAW/archive/oda.file. Any other restart data <strong>not</strong>corresponding to the beginning of a month can be deleted. Restart files for the beginning of a month should be kept until the model has progressed a few months past the point of the original failure.</p>
<h2><a name="6. Check on NRUN and submit CRUN"></a> 6. Check on NRUN and submit CRUN through UMUI</h2>
<p></p>
<p>Verify that the NRUN was successful.</p>
<p></p>
<p>In the UMUI change the job to a CRUN by including the crun.ed hand edit (under <em>Input/Output control -&gt; User hand edits).</em>Save and process the job. If the GPS is strong enough reapply the changes to the W_CAPE and W_CONV limits in the CNTLATM file as in step 4*.</p>
<p></p>
<p>Resubmit the run.</p>
<p></p>
<p>* Note: if you want to run with this change for longer than the NRUN you'll need to keep a close eye on the progress of your job so that you know when to change these limits back.</p>
<h2><a name="7. Check on production of annual"></a> 7. Check on production of annual and seasonal means by the UM</h2>
<p></p>
<p>Depending on the date from which the model is restarted, the UM may fail to generate seasonal or annual mean files. To fill in the gaps you'll need to generate any missing seasonal mean files from the monthly output using the script ~msmizi/bin/FieldOp_mean_month_to_seas.pl and any annual means from seasonal data using ~msmizi/bin/FieldOp_mean_seas_to_annual.pl. In each case run the script without any arguments for a syntax guide.</p>
<p></p>
<p>Each file created in this way will need to be converted to pp format and uploaded to MASS-R by hand. The script ~msmizi/bin/convert_32pp_single.pl can be used to perform the conversion to pp.</p>
<p></p>
<p>The ocean and ice model tend to cope with the creation of seasonal and annual means better, but it is still worth checking that they appear. If not the nco tool ncea can be used to create seasonal/annual means from monthly/seasonal data.</p>
<h2><a name="8. Final tidy up"></a> 8. Final tidy up</h2>
<p></p>
<p>Once the model has progressed a few months past the failure clear out and delete any remaining files in the temporary directory.</p>
<p></p>
<p></p>
<h1>Setting up a run such that multiple users on the same unix group/project can edit and run it</h1>
<p>Procedure to share a umui job on MONSooN with another user <strong>in your unix group</strong></p>
<p></p>
<p><br>1. Open the PUMA umui <br> <br>2. Select the experiment you wish to share and select "Access list…" from the "Experiment" menu. Note that individual jobs cannot be independently shared; control over the sharing is at the experiment level.<br><br>3. Add in the PUMA user names of the people you wish to share write permissions with. <br> <br>4. Open the job you wish to share and make the following changes: <br> A) "Input/Output.." -&gt; "User hand edit files"; add "~matthew_miz/umui_jobs/hand_edits/vn7.7/set_group_permissions.ed" to your hand edits (don't forget to include it). <br> B) "Input/Output.." -&gt; "Time Convention…"; change DATAM and DATAW such that they are not dependent on the user id of the person who submits them. For example, I use "/projects/hirescm/msmizi/$RUNID". <br> <br>5. Set the permissions of the run directory to allow your group to write to it (if this is a new run you may need to wait until the first step begins before it exists).</p>
<p></p>
<p>If, or when, another user wants to run the job they will need to change the "Target Machine user-id" and "Mail-id" (optional) under "User information…" -&gt; "General details" in the UMUI.</p>
