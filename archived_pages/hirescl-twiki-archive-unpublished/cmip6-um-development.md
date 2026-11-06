---
date: 2020-09-23 18:23:18.592000
description: These pages will try and document the process of generating a suite for
  the CMIP6 HighResMIP project, also core simulations for PRIMAVERA.  Initial experiment
  documentation at https://code.metoffice.gov.uk/trac/ukcmip6/wiki/MIPDocumentation
layout: base_hrcm
order: 3
permalink: /hirescl-twiki-archive-unpublished/cmip6-um-development/
title: CMIP6 UM development
---

<p>These pages will try and document the process of generating a suite for the CMIP6 <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/HighResMIP?topicparent=Project/HiResCL.CMIP6HighResMIPmain" rel="nofollow" title="HighResMIP (this topic does not yet exist; you can create it)">HighResMIP</a></span> project, also core simulations for PRIMAVERA. <br> Initial experiment documentation at <a href="https://code.metoffice.gov.uk/trac/ukcmip6/wiki/MIPDocumentation" target="_top">https://code.metoffice.gov.uk/trac/ukcmip6/wiki/MIPDocumentation</a></p>
<p></p>
<h4><a name="Development of future SST and se"></a> Development of future SST and sea-ice</h4>
<p><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HighResMIPFutureSSTSeaiceDevelopment">HighResMIPFutureSSTSeaiceDevelopment</a></p>
<p></p>
<h4><a name="Requirements:"></a> Requirements:</h4>
<ul>
<li>GC3.1.x configuration suite - initial suite u-ad705 from Jamie Rae, as u-ad905</li>
<li>- initial suite u-ac695 (GC3), since this is at UM10.4 (without shorter ocean timestep)
<ul>
<li>CMIP6 metadata
<ul>
<li>cd to suite directory, do: export ROSE_VERSION=next ; export ROSE_META_PATH=/home/h06/hadom/roses/u-ROSIE/rose-meta</li>
</ul>
</li>
</ul>
</li>
<li>NEMO output definition, iodef etc
<ul>
<li>Some of this seems to be contained in this suite anyway, need to check if more is needed - Tim thinks there may be another bit to include</li>
<li></li>
</ul>
</li>
<li>SIMIP-compliant output definition
<ul>
<li>Several branches are added, but may need to change STASH setup to get new ice-related diagnostics (heat fluxes etc)</li>
</ul>
</li>
<li><span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/EasyAerosol?topicparent=Project/HiResCL.CMIP6HighResMIPmain" rel="nofollow" title="EasyAerosol (this topic does not yet exist; you can create it)">EasyAerosol</a></span>implementation
<ul>
<li>Not yet</li>
</ul>
</li>
<li>CMIP6 data request translated to STASH
<ul>
<li>Later, needs post-proc branch for streams</li>
</ul>
</li>
<li>Suite post-processing with: extra streams, ..</li>
<li>CMIP6 historic forcings
<ul>
<li>Ozone – timeseries and repeat 1950</li>
<li>Solar – timeseries and repeat 1950</li>
<li>GHG concentrations – timeseries and repeat 1950</li>
<li>SST and sea-ice from <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/HadISST2?topicparent=Project/HiResCL.CMIP6HighResMIPmain" rel="nofollow" title="HadISST2 (this topic does not yet exist; you can create it)">HadISST2</a></span>(MJR)
<ul>
<li>Now have the 1940-2009 period data, test and then release this on JASMIN - ask if any demand for the pre-1950 part</li>
</ul>
</li>
</ul>
</li>
<li>Initial conditions
<ul>
<li>EN4 temperature and salinity for 1950, on 1degree grid (processed like Pierre, no mask etc), with remapping file for NEMO online initialisation
<ul>
<li>PM has given me the way to do this using sosie - need the EN4 data on the L75 grid and filled first</li>
<li>Would like to do in one script and 2 parts
<ul>
<li>take the EN4 data on its native grid, fill the land and vertically interpolate to give 1 degree, L75 set (as Dave Storkey has done already)</li>
<li>then generate the remap weights for the EN4 to NEMO grid to use in the suite</li>
</ul>
</li>
<li>Could use Mirek's suite to generate the weights</li>
</ul>
</li>
<li>Sea-ice - going to use the 1979 IC - may need to remap to ORCA1 too, check what Till's suite uses for sea-ice.
<ul>
<li>Unclear what the source of the CICE IC is in the eORCA1 run</li>
</ul>
</li>
<li>ERA-20C 1950 initial file – done</li>
</ul>
</li>
<li>Future forcings
<ul>
<li>SST and sea-ice – to be done using CMIP5 models under RCP8.5</li>
<li>Ozone, solar – from CMIP6 using SSP5-8.5 close to RCP8.5</li>
<li>GHG – either from CMIP5 and fix join ~2014 with RCP8.5, or CMIP6</li>
</ul>
</li>
</ul>
<p></p>
<h4><a name="Pre-requisites"></a> Pre-requisites</h4>
<ul>
<li>Needs preindustrial AMIP-style simulation to generate background aerosol concentration fields for use with <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/EasyAerosol?topicparent=Project/HiResCL.CMIP6HighResMIPmain" rel="nofollow" title="EasyAerosol (this topic does not yet exist; you can create it)">EasyAerosol</a></span> * Which also needs new diagnostics in order to produce the <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/EasyAerosol?topicparent=Project/HiResCL.CMIP6HighResMIPmain" rel="nofollow" title="EasyAerosol (this topic does not yet exist; you can create it)">EasyAerosol</a></span> climatologies - Nicholas and Steve to do this</li>
</ul>
<p></p>
<h4><a name="To do"></a> To do</h4>
<ul>
<li>NEMO restart - add remap weights to namelist/NEMO namelist/Run settings/Climatology, and use EN4 1 degree file (unmasked) as input.
<ul>
<li>This file will come from processing the EN4 data using sosie offline, and will be an unmasked lat-long input</li>
<li>This seemed promising, but another package to make weights is not attractive. Hence generate EN4 conditions from python script ~workspace/HighResMIP/remap_EN4_NEMO.py, or better the suite.</li>
<li>Can NEMO simply read in a netcdf file, or does it need to be "formatted" - it can read nc file, but need care with calendar, time interp etc. Have some code that can make a better calendar header.</li>
</ul>
</li>
<li>Atmos restart - use ERA-20C 1950 condition</li>
<li>Add atmos branches for GC3.1 (some/all, at UM10.4):
<ul>
<li>branches/dev/janemulcahy/vn10.3_Liu2008_spectral_dispersion</li>
<li>branches/dev/benjohnson/vn10.3_UKCA_RADAER_LUT_upgrade</li>
<li>branches/dev/andyjones/vn10.3_ACTIVATE_Off_fix</li>
</ul>
</li>
<li>Sea-ice tuning(s)
<ul>
<li>Parameter changes ...</li>
</ul>
</li>
<li>Optimisations
<ul>
<li>Change solver (mixed/precision), IO server settings</li>
</ul>
</li>
<li>Ancillaries
<ul>
<li>Switch to 1950/historic ancillaries</li>
</ul>
</li>
<li>Test IO server in atmosphere ready for N512 run</li>
<li>For <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/HadISST2?topicparent=Project/HiResCL.CMIP6HighResMIPmain" rel="nofollow" title="HadISST2 (this topic does not yet exist; you can create it)">HadISST2</a></span> SST and sea-ice, need to revision control ANTS script.</li>
<li>However we do the ozone interpolation, need to revision control the source code, ideally using ANTS.</li>
<li>Age tracer:
<ul>
<li>Restart filename needs YYYYMMDD format - I missed this from merge, now in</li>
<li>It needs to be moved to the <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/HistoryData?topicparent=Project/HiResCL.CMIP6HighResMIPmain" rel="nofollow" title="HistoryData (this topic does not yet exist; you can create it)">HistoryData</a></span> /NEMO directory at the end of the job step (post-processing?)</li>
<li>And then check that it does indeed get read in during the next step</li>
</ul>
</li>
<li>Ocean timestep to 900 secs (future proof)</li>
<li>Remove daily SIMIP diagnostics (added for testing)</li>
<li>Archiving of daily fields from NEMO and CICE (the NEMO ones get to NEMOhist, the CICE ones stay in the work directory)</li>
<li>Check NEMO values used for advection/diffusion in the age tracer</li>
<li>NEMO diagnostics: add in udiff_heattr (is it really worth outputting the sum too?)
<ul>
<li>Typo on: sea_water_age_since_first_contact (should be surface_contact)</li>
<li>all temperature_fluxes expressed as out of sea water: temperature_flux_due_to_rain_expressed_as_heat_flux_out_of_sea_water - not true of CMIP5 list</li>
<li>have shortwave but not other heat fluxes * do not have integral of density * salinity, density * temperature (what are they for?)</li>
</ul>
</li>
<li>Remove 90 day initialisation</li>
<li>Sort out packing for 5208</li>
<li>Add required components for daily CICE: branch, upgrade macro, diagnostics</li>
<li>Fix 6hr and 3hr of same diagnostics (if any)</li>
<li>Keep heaviside in same package as other diagnostics - if on own inst_heavi can produce massive output with no corresponding variable</li>
<li>On the variable list, somehow associate the heaviside function with the variable for cmorization</li>
<li>I've edited the STASHmaster to change the packing of 5208 - this seems to work.</li>
<li>Lookup headers - max in rose is 50000, just putting in ozone ancil 1850-2014 this is not enough. 600000 was enough (with ozone, sst and sea-ice).</li>
<li>The new postprocessing seems not to build icb_pp.py to post-process the icebergs</li>
<li>Iceberg trajectory naming - on timestep currently, this is only diagnostic so don't care.</li>
<li>Should we land mask the ocean output fields - noticed that e.g. heat flux has very odd values but these are on land points. Maybe do this post-process, as might be cost in masking?</li>
<li>Turn off chunking for NEMO in suite, and in iodef make sure to use 10d split for 1d files - think this will allow them to match the file naming for rebuilding
<ul>
<li>This seems to be because the rebuild was not working, because the filename matching was off (need 10d split on the 1d files). With this working the chunking looks OK.</li>
</ul>
</li>
<li>Change LIMITED in data spreadsheets to distinguish space and time limited (if different). I've added a D_EUROPE domain, need to check the lat/long with the 2.2km model.</li>
<li>Sort out correct NEMO and CICE bathy, KMT, remapping files etc.</li>
<li>Sea-ice diags: down solar flux, upward solar flux, sensible heat flux seem to be zero.</li>
<li>remove f_uvel, f_vvel (replaced by siu, siv?)</li>
<li>Check revisions of UM branches atmos only vs coupled</li>
<li>For iodef, Erica recommends that it gets checked out of moci repo for different resolutions, rather than being file in /file subdirectory. Apparently similar to STASHMASTER in GC3.</li>
<li>Remap the geothermal file (as used in ORCA1) to all resolutions using suite (generated weights).</li>
<li>Add STASHMASTER to atmos-only job, for stash 208 and to allow processing of SIMIP diagnostics</li>
<li>Need N512 version of /data/d01/frjy/AEROSOL_EMS/DMS/Lana_DMS_ocean_N96_eg.N96 (or Lana_DMS_ocean_N216_eg.N96) - don't since <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/EasyAerosol?topicparent=Project/HiResCL.CMIP6HighResMIPmain" rel="nofollow" title="EasyAerosol (this topic does not yet exist; you can create it)">EasyAerosol</a></span>does not use this
<ul>
<li>Added this into the /data/d05/hadom/ancil/data/ancil_versions/n96e_orca025/GA7.1_CMIP6_HRMIP/v1/ancils file, and linked /data/d05/hadom/ancil/atmos/n96e/orca025_cmip6/AEROSOL_EMS/DMS/qrclim.sulpdms to the above file (I really don't want to have the suite be specific to a resolution/dataset)</li>
</ul>
</li>
<li>Setting questions (differences u-af269 and my GA&amp;-based 10.4 u-af746)
<ul>
<li>l_albedo_obs=.false. in GA7.1 - but true in GA7. This also needs ancil to be ignored. Done</li>
<li>l_full_lambdas=.false., l_lambdam2=.false., prandtl=1, subs_couple_fix=1, - not sure of these</li>
<li>cca_sh_knob=0.50 (vs 0.2 GA7), mp_dz_scal=2.0 (vs 1.0 in GA7), - done</li>
<li>/data/d02/hadtq/ancil/ukca_emiss/andres_kasgnoc/v2/ukca_emiss_SO2_nat_r2428.nc (but this is all zero!)</li>
<li>For Radaer changes, if I simply change the ukcaaclw etc values and point to the 10.5 directories and ga7_1, is this correct?</li>
</ul>
</li>
<li>GA7.1 changes summarised in: <a href="https://code.metoffice.gov.uk/trac/roses-u/changeset?reponame=&amp;new=18325%40a%2Ff%2F7%2F4%2F6%2Ftrunk&amp;old=18163%40a%2Ff%2F0%2F9%2F4%2Ftrunk" target="_top">https://code.metoffice.gov.uk/trac/roses-u/changeset?reponame=&amp;new=18325%40a%2Ff%2F7%2F4%2F6%2Ftrunk&amp;old=18163%40a%2Ff%2F0%2F9%2F4%2Ftrunk</a></li>
</ul>
<p></p>
<ul>
<li>Summary of GA7 to GA7.1 changes in u-af746 (N96):
<ul>
<li><a href="https://code.metoffice.gov.uk/trac/roses-u/changeset?reponame=&amp;new=18325%40a%2Ff%2F7%2F4%2F6%2Ftrunk&amp;old=18163%40a%2Ff%2F0%2F9%2F4%2Ftrunk" target="_top">https://code.metoffice.gov.uk/trac/roses-u/changeset?reponame=&amp;new=18325%40a%2Ff%2F7%2F4%2F6%2Ftrunk&amp;old=18163%40a%2Ff%2F0%2F9%2F4%2Ftrunk</a></li>
<li>note the 2 ancillary changes are "hidden" in the new ancil versions file</li>
</ul>
</li>
</ul>
<p></p>
<ul>
<li><span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/EasyAerosol?topicparent=Project/HiResCL.CMIP6HighResMIPmain" rel="nofollow" title="EasyAerosol (this topic does not yet exist; you can create it)">EasyAerosol</a></span> changes summarised in: (Nicolas' job ac283 vs af207): <a href="https://code.metoffice.gov.uk/trac/roses-u/changeset?reponame=&amp;new=18134%40a%2Ff%2F2%2F0%2F7%2Ftrunk&amp;old=13252%40a%2Fc%2F2%2F8%2F3%2Ftrunk" target="_top">https://code.metoffice.gov.uk/trac/roses-u/changeset?reponame=&amp;new=18134%40a%2Ff%2F2%2F0%2F7%2Ftrunk&amp;old=13252%40a%2Fc%2F2%2F8%2F3%2Ftrunk</a> ; my job(on top of GA7.1 changes, af746 vs af770): <a href="https://code.metoffice.gov.uk/trac/roses-u/changeset?reponame=&amp;new=18426%40a%2Ff%2F7%2F7%2F0%2Ftrunk&amp;old=18325%40a%2Ff%2F7%2F4%2F6%2Ftrunk" target="_top">https://code.metoffice.gov.uk/trac/roses-u/changeset?reponame=&amp;new=18426%40a%2Ff%2F7%2F7%2F0%2Ftrunk&amp;old=18325%40a%2Ff%2F7%2F4%2F6%2Ftrunk</a>
<ul>
<li>note I had to make a merge of SIMIP and <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/EasyAerosol?topicparent=Project/HiResCL.CMIP6HighResMIPmain" rel="nofollow" title="EasyAerosol (this topic does not yet exist; you can create it)">EasyAerosol</a></span> branches in order to get a merged STASHmaster file, and meta data change for rose: vn10.4_merge_SIMIP_EasyAerosol_stashmaster</li>
<li>Advised by Erica, I have made the job use the STASHmaster on the repo and it should check it out - but I will also keep a copy locally for the data request processing</li>
</ul>
</li>
</ul>
<p></p>
<ul>
<li>GC3.1 changes
<ul>
<li>Sea-ice: CICE branch fcm:cice_br/test/hadjs/vn5.1.2_dragio_change@1152</li>
<li>kappai_snow = .255 (from 0.5) namelist:jules_sea_seaice</li>
</ul>
</li>
</ul>
<p></p>
<ul>
<li>NEMO square diagnostics - see <a href="https://code.metoffice.gov.uk/trac/gmed/ticket/264#comment:8" target="_top">https://code.metoffice.gov.uk/trac/gmed/ticket/264#comment:8</a>(and ticket #268)
<ul>
<li>Upgraded branch fcm:NEMO.xm/branches/UKMO/dev_r5518_GO6_package_MEDUSA_extra_CMIP6_diags@6899</li>
</ul>
</li>
</ul>
<p></p>
<ul>
<li>NEMO iodef to include new transport diagnostics from Tim</li>
<li>Bug in coupled model code (in NEMO) ticket #1766, summary below. Need to fix in my version of the GO6 package branch</li>
</ul>
<p></p>
<h4><a name="Changes made to suite"></a> Changes made to suite</h4>
<ul>
<li>Changes to rev 13280
<ul>
<li>Added metadata entries</li>
<li>Changed project name to highres</li>
<li>Changed dump time to January - do NEMO and CICE follow this and save at the same time?</li>
</ul>
</li>
<li>Changes to rev
<ul>
<li>SIMIP-compliant output definition and JULES diagnostics, following suite u-ad565 diffs <a href="https://code.metoffice.gov.uk/trac/roses-u/changeset?reponame=&amp;new=12920%40a%2Fd%2F5%2F6%2F5%2Ftrunk&amp;old=11905%40a%2Fd%2F2%2F3%2F3%2Ftrunk" target="_top">https://code.metoffice.gov.uk/trac/roses-u/changeset?reponame=&amp;new=12920%40a%2Fd%2F5%2F6%2F5%2Ftrunk&amp;old=11905%40a%2Fd%2F2%2F3%2F3%2Ftrunk</a></li>
<li>Should I remove branch branches/dev/hadax/vn5.1.2_new_budget_diags@1132? Yes I think so, and have done since it clashed.</li>
<li>Added the icefields_nml fields from suite u-ad565</li>
<li>Added new STASHmaster_A to app/coupled/file (coped from u-ad565), and STASHMST=. in app/coupled/rose-app.conf - and added meta data path /data/cr1/hadjs/FCM_working/MOCI/r733_SIMIP_diagnostics/rose-meta/GA7/HEAD/
<ul>
<li>I assume this will become a standard path</li>
</ul>
</li>
<li>Added new STASH diagnostics for JULES:
<ul>
<li>I have put these in a conf file /home/h06/hadom/roses/reference/simip_jules_diagnostics.conf in case we can automate this</li>
</ul>
</li>
</ul>
</li>
<li>Changes for NEMO diagnostics from Tim:</li>
</ul>
<p><span class="twistyPlugin twikiMakeVisibleInline"> <span class="twistyTrigger twikiUnvisited twistyHidden twistyInited" id="twistyIdProject/HiResCLCMIP6HighResMIPmain1show"><a href="#"><span class="twikiLinkLabel twikiUnvisited">unhide</span></a> </span> <span class="twistyTrigger twikiUnvisited twistyHidden twistyInited" id="twistyIdProject/HiResCLCMIP6HighResMIPmain1hide"><a href="#"><span class="twikiLinkLabel twikiUnvisited">Close</span></a> </span> </span></p>
<!--/twistyPlugin twikiMakeVisibleInline-->
<p></p>
<ul>
<li>
<ul>
<li>Branch fcm:nemo.xm/branches/UKMO/v3_6_extra_CMIP6_diagnostics - this clashes with (at least) dev_r5518_GC3p0_package_v2 - looks like Dan merged these up to rev 6433, so need to find out how to merge up to 6674. Do this by (with NEMO login):
<ul>
<li>fcm checkout svn+ssh://forge.ipsl.jussieu.fr/ipsl/forge/projets/nemo/svn/branches/UKMO/dev_r5518_GC3p0_package_v2 ./dev_r5518_GC3p0_package_v2</li>
<li>cd dev_r5518_GC3p0_package_v2</li>
<li>svn merge -r 6433:6674 svn+ssh://forge.ipsl.jussieu.fr/ipsl/forge/projets/nemo/svn/branches/UKMO/v3_6_extra_CMIP6_diagnostics</li>
<li>fcm commit (make a note in the log that we have gone up to revision 6674 of v3_6_extra_CMIP6_diagnostics)</li>
</ul>
</li>
<li>Going to try this a different way - start with the GO6 package branch (which includes a bunch of the other branches), to try and remove all the clashes that I had in merging.
<ul>
<li>Include fcm:NEMO.xm/branches/UKMO/dev_r5518_GO6_package@6618 which includes:
<ul>
<li><a href="mailto:dev_r5021_nn_etau_revision@6238">dev_r5021_nn_etau_revision@6238</a>, <a href="mailto:dev_r5107_mld_zint@5534">dev_r5107_mld_zint@5534</a>, <a href="mailto:dev_r5107_eorca025_closea@6390">dev_r5107_eorca025_closea@6390</a>, <a href="mailto:icebergs_latent_heat@5821">icebergs_latent_heat@5821</a>, <a href="mailto:icebergs_restart_single_file_corrected@6480">icebergs_restart_single_file_corrected@6480</a>, <a href="mailto:antarctic_partial_slip@5961">antarctic_partial_slip@5961</a>, <a href="mailto:nemo_v3_6_STABLE_copy@6237">nemo_v3_6_STABLE_copy@6237</a> (looks like 6486 in the GO6 package),</li>
<li><a href="mailto:restart_datestamp@5539">restart_datestamp@5539</a> (note using rev 6336 in current job, so need to upgrade this), <a href="mailto:product_diagnostics@5971">product_diagnostics@5971</a> (I already took out because I think this is in the CMIP6 branch), <a href="mailto:dev_r5518_coupling_GSI7_GSI8_landice_bitcomp@6363">dev_r5518_coupling_GSI7_GSI8_landice_bitcomp@6363</a> (the GO6 package only has dev_r5518_coupling_GSI7_GSI8_landice/NEMOGCM@6487, so this may need upgrading?)</li>
</ul>
</li>
<li>Include <a href="mailto:dev_r5518_GC3_couple_pkg@6615">dev_r5518_GC3_couple_pkg@6615</a>, which replaces:
<ul>
<li><a href="mailto:dev_r5518_hadgem3_cplfld@6561">dev_r5518_hadgem3_cplfld@6561</a>, <a href="mailto:dev_r5518_hadgem3_cplseq@6562">dev_r5518_hadgem3_cplseq@6562</a>, <a href="mailto:dev_r5518_hadgem3_mct@6571">dev_r5518_hadgem3_mct@6571</a> (+extra upgrade for land suppression), <a href="mailto:dev_r5518_xios_initialize_toyoce@6556">dev_r5518_xios_initialize_toyoce@6556</a></li>
<li>Seems I need to change key oasis3mct to oasis3 with this</li>
<li>Get error right at start - Richard Hill tracked it down to the GC3.conf file, and it suggests a problem with the land suppression somewhere.</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p></p>
<!--/twistyPlugin-->
<p></p>
<ul>
<li>
<ul>
<li>Need a new iodef file - for ORCA1 this can be coped from ~hadtd/roses/mi-aj246_diaar5/app/nemo_cice/file/iodef.xml (to deal with GM) - put in app/coupled/file directory</li>
<li>In fcm_make_ocean:
<ul>
<li>Change fcm_make_ocean meta data to point to /home/h05/hadtd/MOCI_branches/r209_GO6_fcm_configs_test_path_exclude/rose-meta/nemo-cice-fcm-make/HEAD</li>
<li>Change the config root path to point to fcm:moci.xm/branches/dev/timgraham/r209_GO6_fcm_configs_test_path_exclude</li>
<li>Under NEMO sources add TOP_SRC to nemo_path_incl</li>
<li>You should also be able to add a nemo_path_excl field where you need to add NEMOGCM/NEMO/OPA_SRC/TRD/trdtrc.F90 (need to find latent panel and activate)</li>
<li>Add keys: key_top, key_age (for age tracer), key_diaar5 and if using GM add key_diaeiv and key_ldfeiv</li>
<li>Removed branch fcm:NEMO.xm/branches/UKMO/product_diagnostics@5971 since this seemed to be contained within the part of <a href="mailto:v3_6_extra_CMIP6_diagnostics@6647">v3_6_extra_CMIP6_diagnostics@6647</a> which I just merged into UKMO/dev_r5518_GC3p0_package_v2@6679 - this merge was odd in sbccpl, I had to re-add some lines near the #if defined key_lim3 since they were missing.</li>
</ul>
</li>
<li>In coupled app, add namelists:
<ul>
<li>namage to include rn_age_depth=10 and rn_age_kill_rate=-0.000138888, this needs to go in a file called namelist_age_cfg. (I'm not quite sure here, do I need a file in app/coupled/file, and/or in the rose-app.conf namelists)</li>
<li>namtrc to include sn_tracer(1)= 'Age','Ideal age tracer','Years',.false.,.true. This needs to go in a file called namelist_top_cfg</li>
<li>You also need to include the namelist_top_ref and namelist_age_ref from the branch above. I would suggest checking these out and putting them in the coupled/app/file directory for now (ideally we should modify the fcm_make app to include these).- Again not quite sure I understand this</li>
</ul>
</li>
<li>Ocean starting conditions - made the EN4 1950 (well, 1950-1954, start date 1952), and simply use the netcdf file for the NEMO input - started running once I took off the time interpolation option in the suite (need to check this does indeed get the Jan value)
<ul>
<li>Changed the ocean ancil file app/install_ancil ancil source=/data/d05/hadom/ancil/coupled/NEMO_ancils_N96_eORCA1_GC3.0_UM10.4_1950</li>
<li>Need to check that this did use the Jan values - i.e. that it interprets the calendar correctly, since EN4 nc files have gregorian but model is 360.</li>
</ul>
</li>
</ul>
</li>
</ul>
<p></p>
<h4><a name="Changes made to suite mk 2"></a> Changes made to suite mk 2</h4>
<ul>
<li>Starting from u-ad388 (UM10.4, with coupling package branch, N96-ORCA025)</li>
<li>Replaced other NEMO branches with a GO6 package branch from Richard Hill
<ul>
<li>fcm:NEMO.xm/branches/UKMO/dev_r5518_GO6_package_MEDUSA_temporary@6708 - this includes some MEDUSA code for the ocean biogeo as well. This ran fine.</li>
<li>Merge in Tim's CMIP6 diagnostics branch fcm:nemo.xm/branches/UKMO/v3_6_extra_CMIP6_diagnostics
<ul>
<li>This took some work, both hand merging several routines, and dealing with some issues in sbccpl.F90 and traadv_tvd.F90. I took Tim's hand-merged code (my copy at /data/users/hadom/branches/NEMO/dev_r5518_GO6_package from his datalocal) as the correct version when dealing with issues.</li>
</ul>
</li>
<li>The model runs, ocean.output has warning since I have not changed the namelists yet
<ul>
<li>W A R N I N G: end of record or file while reading namelist namsto in configuration namelist iostat = <strong>**</strong></li>
</ul>
</li>
</ul>
</li>
<li>Next try adding the meta data, config path, keys etc - suspect that key key_trdtrc may need to come out since adding NEMOGCM/NEMO/OPA_SRC/TRD/trdtrc.F90 to exclusion list - indeed I did need to do this to make it compile
<ul>
<li>this then worked, with <a href="mailto:u-ae187@14077">u-ae187@14077</a></li>
</ul>
</li>
<li>There were some issues with getting the field_def and iodef to work - this was mainly my fault in not merging the mldzint branch changed to field_def in properly. Also the iodef frim Tim's (ocean-only) job needed modifying for coupled.</li>
</ul>
<p><span class="twistyPlugin twikiMakeVisibleInline"> <span class="twistyTrigger twikiUnvisited twistyHidden twistyInited" id="twistyIdProject/HiResCLCMIP6HighResMIPmain2show"><a href="#"><span class="twikiLinkLabel twikiUnvisited">unhide</span></a> </span> <span class="twistyTrigger twikiUnvisited twistyHidden twistyInited" id="twistyIdProject/HiResCLCMIP6HighResMIPmain2hide"><a href="#"><span class="twikiLinkLabel twikiUnvisited">Close</span></a> </span> </span></p>
<!--/twistyPlugin twikiMakeVisibleInline-->
<p></p>
<ul>
<li>
<ul>
<li>It ran fine for 4 months, however the diagnostics are not right yet (I suspect because I was not using the iodef file from ~hadtd/roses/mi-aj246_diaar5/app/nemo_cice/file/)
<ul>
<li>Many of the diaptr fields are 3D, which makes the diaptr file 10x bigger than the grid files, and all the fields are 0</li>
<li>trend diagnostics are all missing, no age tracer, not sure what the 2nd sea water x velocity is (seems to be almost all +ve), in W grid the lateral eddy diffusion is all missing</li>
<li>With Tim's iodef, the model fails immediately (no ocean.output or anything). Try copying the field_def.xml file from /data/users/hadom/branches/NEMO/dev_r5518_GO6_package_MEDUSA_temporary/NEMOGCM/CONFIG/SHARED to the app/coupled/file directory - also need to recompile, since this file gets linked from the fcm directory - this didn't help, still does nothing, writes nothing</li>
<li>New field_def.xml does not work with old iodef.xml - actually crashes model and gives error [ ref_name = mldzint_1] invalid field name - since this field is not in the new field_def.xml</li>
<li>With new field_def and empty iodef (no files), this failed. Figured out it was my fault - when merging the field_def.xml, I had omitted the mldzint_? changed from the GO6 package (from the mld_zint branch), and the suite specifically asks for these (via nn_mld_diag=2) - this was not in Tim's suite</li>
<li>With this, an empty iodef works fine, and the GC3 iodef also works, but the one from Tim's suite gives the lock-up still. So start from the GC3 one and evolve. Possible the problem was with the 1mo frequency in the CMIP6 (from Tim's ORCA1 job) - need to use 10d for coupled. In fact I suspect it was that Tim's had "using_oasis" set to false in it. Indeed this now runs.</li>
</ul>
</li>
</ul>
</li>
</ul>
<p></p>
<!--/twistyPlugin-->
<ul>
<li>
<ul>
<li>
<ul>
<li>Made some typo changes to field_def.xml</li>
</ul>
</li>
<li>Took a fresh suite u-ae344 to test all of this together
<ul>
<li>Needed a fix to the postprocessing - to re-include the nccatted command to fix the zonal mean files, and then to cope with 1d ocean output files</li>
<li>Made a NEMO branch with the code: fcm:NEMO.xm/branches/UKMO/dev_r5518_GO6_package_MEDUSA_extra_CMIP6_diags@6731 and this seems to work fine</li>
<li>In iodef.xml, u_heattr and v_heattr were output as missing data, I suspect because they seem to have an operation associated with them, and maybe one component of this is missing? I try with simple output</li>
<li>Daley told me that I need key_diahth to output mldr0_3, but this does not have the right CMOR name (currently mlost, should be mlotst, and the square mlotstsq)</li>
<li>Also modified the mld requests in iodef.xml - there was mldzint, but I think only mldzint_? are allowed, so included these 2.</li>
<li>I changed the u_heattr and v_heattr - initially they included a function in iodef to add advection + diffusion, but this came out missing.
<ul>
<li>Should there be a 3D heat transport too, or good enough to have UT and VT?</li>
<li>Do we really need 3D short wave penetration, or is this more for biology?</li>
</ul>
</li>
<li>Note: may need to make sure the restart file for the age tracer gets moved to the <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/HistoryData?topicparent=Project/HiResCL.CMIP6HighResMIPmain" rel="nofollow" title="HistoryData (this topic does not yet exist; you can create it)">HistoryData</a></span> /NEMO directory, and tidued up or archived as appropriate.</li>
<li>Question - does the 1d files get archived, or will this need adding? May also be true for the CICE 1d files.</li>
<li>Also scalar output files like ae344o_10d_19780901_19780910_scalar_19780901-19780910_0000.nc - do they need archiving too?</li>
<li>Need to remember to change the iodef file for ORCA1 in order to include the GM advection
<ul>
<li>Does the WT term include eddy-induced advection?</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>Leave u-ae344 at this point, has the NEMO CMIP6 diagnostics in. Make a new suite and add the SIMIP stuff.</li>
<li>Copy as u-ae368
<ul>
<li>Add SIMIP stuff - as above, viz:</li>
<li>SIMIP-compliant output definition and JULES diagnostics, following suite u-ad565 diffs <a href="https://code.metoffice.gov.uk/trac/roses-u/changeset?reponame=&amp;new=12920%40a%2Fd%2F5%2F6%2F5%2Ftrunk&amp;old=11905%40a%2Fd%2F2%2F3%2F3%2Ftrunk" target="_top">https://code.metoffice.gov.uk/trac/roses-u/changeset?reponame=&amp;new=12920%40a%2Fd%2F5%2F6%2F5%2Ftrunk&amp;old=11905%40a%2Fd%2F2%2F3%2F3%2Ftrunk</a></li>
<li>Should I remove branch branches/dev/hadax/vn5.1.2_new_budget_diags@1132? Yes I think so, and have done since it clashed.</li>
<li>Added the icefields_nml fields from suite u-ad565</li>
<li>Added new STASHmaster_A to app/coupled/file (coped from u-ad565), and STASHMST=. in app/coupled/rose-app.conf - and added meta data path /data/cr1/hadjs/FCM_working/MOCI/r733_SIMIP_diagnostics/rose-meta/GA7/HEAD/
<ul>
<li>I assume this will become a standard path</li>
</ul>
</li>
<li>Added new STASH diagnostics for JULES:
<ul>
<li>I have put these in a conf file /home/h06/hadom/roses/reference/simip_jules_diagnostics.conf in case we can automate this</li>
</ul>
</li>
<li>Tried to run this - it failed with a COEX packing error when trying to make the monthly mean</li>
<li>Then tried to switch on the PRINT_STATUS = extra diagnostic messages - this fails after 3 timesteps, with error
<ul>
<li>lib-4212 : UNRECOVERABLE library error</li>
<li>An internal WRITE tried to write beyond the end of an internal file.</li>
</ul>
</li>
<li>It runs OK with operational status messages - assume this is from new JULES branch?
<ul>
<li>Try new revision 4008 - this makes no difference to COEX error. Include UM branch and this works fine - include the packed STASHMASTER again</li>
</ul>
</li>
<li>Update ocean branch to fix restart date on age tracer</li>
<li>Reduce ocean and cice timestep to 900s (+960 and 2880 for writes respectively)</li>
</ul>
</li>
<li>Took copy of u-ae368/trunk@14698 - u-ae418
<ul>
<li>Differences from here to a version that
<ul>
<li>Runs, seems to pass the age tracer from restart to restart (certainly the deeper values increase, and can see deep convection in the Labrador Sea), and outputs</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><a href="https://code.metoffice.gov.uk/trac/roses-u/changeset?reponame=&amp;new=14843%40a%2Fe%2F4%2F1%2F8%2Ftrunk&amp;old=14698%40a%2Fe%2F3%2F6%2F8%2Ftrunk" target="_top">https://code.metoffice.gov.uk/trac/roses-u/changeset?reponame=&amp;new=14843%40a%2Fe%2F4%2F1%2F8%2Ftrunk&amp;old=14698%40a%2Fe%2F3%2F6%2F8%2Ftrunk</a></p>
<ul>
<li>
<ul>
<li>
<ul>
<li>Incorporating the age tracer required the code changes previously, together with some code that Juliene has done for MEDUSA
<ul>
<li>added L_BGC=.true., NEMO_NL_TOP=namelist_top_cfg, RH_iodef=/home/d02/frrh/NEMO/iodef, TOP_START= in the [env] coupled namelist</li>
<li>made [file:namelist_top_cfg] contain source=namelist:namtrc_run namelist:namtrc namelist:namtrc_adv namelist:namtrc_dia - this is what the new UM update_top_nl (in bin) updates at each resubmit</li>
<li>Added branch branches/dev/julienpalmieri/vn10.4_submit_medusa@24080, and config file config_root_path=fcm:um.xm_br/dev/julienpalmieri/vn10.4_submit_medusa to include the update_top_nl</li>
</ul>
</li>
<li>Changed ice diagfreq to agree with the 900s timestep</li>
<li>Also added lots of opt files to be used in future for switching between model resolutions (as atmosphere suites do)</li>
</ul>
</li>
</ul>
</li>
</ul>
<p></p>
<h4><a name="Changes Mk3"></a> Changes Mk3</h4>
<ul>
<li>Testing the stash translation system - need to increase max size of stash request in branch
<ul>
<li>try with just section 4+5 CMIP diagnostics</li>
<li>Error from COEX packing (added print to branch
<ul>
<li>Stash 5208 - pressure at convective cloud top switch off - this caused the problem</li>
</ul>
</li>
<li>Stash 5222 (pressure at lowest conv cloud base) - comes out with mix of values e.g. ~-1.05e+9 as well as missing data -1.0737e+09 - so rubbish</li>
<li>Otherwise runs 10 days fine (with 2 day mean month) - fails on next step due to STWORK: Number of fields exceeds reserved headers for unit 16 - think this because UP5 (monthly mean) currently outputting every 2 days for month</li>
<li>Sections 0, 1 and 3 work OK</li>
<li>Section 2 fails the model right at the start - examine further</li>
<li>Need to trap zonal mean better (maybe put all into upv if monthly)</li>
<li>If going to get COSP_LIDAR, need to add 2320 for the heaviside weighting</li>
<li>Should diagnostics 2308-2315 be diagnosed on radiation timesteps only? (they have RADIATION in the name)</li>
<li>2310 and 2311 come out all zero</li>
</ul>
</li>
<li>Test N512 with these diagnostics
<ul>
<li>Make sure that the COSP_LIDAR ones are switched off (also the new ones of these from CMIP6) - using optional files, need to do explicitly in package</li>
<li>Model failed at 3 hours - suspect a 3hr diagnostic, either mean or instant. The last stash code written is 0409, the last line in one of the pe files is about setting up Fv matrix for filtered output
<ul>
<li>Switching off the 30457 (3hr, <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/PLEV7H?topicparent=Project/HiResCL.CMIP6HighResMIPmain" rel="nofollow" title="PLEV7H (this topic does not yet exist; you can create it)">PLEV7H</a></span> ) allowed the model to run to 6 hours. Then switched off rest of 30455-30458 - then model runs to 1 day and fails with COEX error</li>
<li>The last stash printed is 5206, so this packing error seems to be on this or the next (5208 is on again, switch off)</li>
</ul>
</li>
</ul>
</li>
</ul>
<p></p>
<h4><a name="Changes Mk4"></a> Changes Mk4</h4>
<ul>
<li>At this point I ran suite u-ae660 for 1 year with the Priority 1 (Met Office agreed) diagnostic list, and this worked OK.</li>
<li>A meeting to discuss the CMIP6 output recommended to produce instantaneous heaviside output as well, so need to keep this switched on</li>
<li>Model failed with xios error writing diaptr variable zosrfglo - indeed the zonal mean surface does seem to have strange values at the bottom in this (and other) runs. Is it a <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/NaN?topicparent=Project/HiResCL.CMIP6HighResMIPmain" rel="nofollow" title="NaN (this topic does not yet exist; you can create it)">NaN</a></span> issue too?</li>
</ul>
<p></p>
<h4><a name="Post-processing"></a> Post-processing</h4>
<ul>
<li>check out suite from repo for cmor-directory and metadata names</li>
</ul>
