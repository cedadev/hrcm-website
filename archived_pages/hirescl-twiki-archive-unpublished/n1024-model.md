---
date: 2020-09-23 18:34:47.812000
description: "\n N1024 model\n\n Introduction\n Jobs:\n GA4\n\n Parameterised convection\n\
  \n\n GA5#93 (+bug fix)\n GA6 (#95.13)\n\n Parameterised shallow convection only\n\
  \ GA4-only\n\n\n GA6\n\n Explicit convection\n GA4-only\n\n\n Results\n\n Diurnal\
  \ cycle\n Old plots\n Africa\n\n Diurnal Cycle over West Africa\n Diurnal Cycle\
  \ over Lake Victoria\n West African Monsoon and ITCZ over the Atlantic\n African\
  \ Easterly Waves\n\n\n USA\n MJO\n QBO\n\n\n\n\n\n QBO in N1024 parameterised:\n\
  \ QBO in N1024 explicit:\n\n\n\n\n\n\n Older plots\n\n\n\n\n\n"
layout: base_hrcm
order: 4
permalink: /hirescl-twiki-archive-unpublished/n1024-model/
title: N1024 model
---

<ul>
<li><a href="#N1024 model"> N1024 model</a>
<ul>
<li><a href="#Introduction"> Introduction</a></li>
<li><a href="#Jobs:"> Jobs:</a></li>
<li><a href="#GA4"> GA4</a>
<ul>
<li><a href="#Parameterised convection"> Parameterised convection</a></li>
</ul>
</li>
<li><a href="#GA5#93 (+bug fix)"> GA5#93 (+bug fix)</a></li>
<li><a href="#GA6 (#95.13)"> GA6 (#95.13)</a>
<ul>
<li><a href="#Parameterised shallow convection"> Parameterised shallow convection only</a></li>
<li><a href="#GA4-only"> GA4-only</a></li>
</ul>
</li>
<li><a href="#GA6"> GA6</a>
<ul>
<li><a href="#Explicit convection"> Explicit convection</a></li>
<li><a href="#GA4-only_AN1"> GA4-only</a></li>
</ul>
</li>
<li><a href="#Results"> Results</a>
<ul>
<li><a href="#Diurnal cycle"> Diurnal cycle</a></li>
<li><a href="#Old plots"> Old plots</a></li>
<li><a href="#Africa"> Africa</a>
<ul>
<li><a href="#Diurnal Cycle over West Africa"> Diurnal Cycle over West Africa</a></li>
<li><a href="#Diurnal Cycle over Lake Victoria"> Diurnal Cycle over Lake Victoria</a></li>
<li><a href="#West African Monsoon and ITCZ ov"> West African Monsoon and ITCZ over the Atlantic</a></li>
<li><a href="#African Easterly Waves"> African Easterly Waves</a></li>
</ul>
</li>
<li><a href="#USA"> USA</a></li>
<li><a href="#MJO"> MJO</a></li>
<li><a href="#QBO"> QBO</a>
<ul>
<li>
<ul>
<li>
<ul>
<li><a href="#QBO in N1024 parameterised:"> QBO in N1024 parameterised:</a></li>
<li><a href="#QBO in N1024 explicit:"> QBO in N1024 explicit:</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><a href="#Older plots"> Older plots</a></li>
</ul>
</li>
</ul>
</li>
</ul>
<p></p>
<h2><a name="Introduction"></a> Introduction</h2>
<p>This work aims to compare models at N1024 global resolution based on GA4 physics/dynamics including the PC2 cloud scheme (12km at mid-latitudes, 19km at equator) with and without a convective parameterisation. Work by CASCADE and others suggest that at this kind of resolution, we might hope to see improvements in the diurnal cycle of convection, and possibly propoagation of convective systems.</p>
<p></p>
<p>The main aim here would be to see if, in a global sense, there are obvious improvements in any aspects of the global circulation, radiation and feedbacks from any improvements in diurnal cycle etc, rather than simply repeating the runs like in CASCADE. In particular, we hope that it may lead to better understanding of processes and how they are influenced by the convective parameterisation, with a view to improving both the processes and parameterisations.</p>
<p></p>
<p>The current runs start in Mar 2008 (from a climatological initial condition, these are not initialised) and will hopefully run for several years (i.e. up to present day or so). They take about 1 wallclock hour / model day on about 70 IBM power 7 nodes. Both models have a 4 minute timestep.</p>
<p></p>
<p>The initial explicit convection run uses the blended scheme from Adrian Lock, which combines the 1D boundary layer with the 3D Smagorinsky subgrid-scale turbulence model (<a href="http://www-nwp.metoffice.com/~frlk/UM/blend/blend.html" target="_top">http://www-nwp.metoffice.com/~frlk/UM/blend/blend.html</a>, MO internal link). It is planned to do another experiment with a set-up more like CASCADE (parameterising shallow convection and doing deep convection explicitly).</p>
<p></p>
<p>Initial thoughts:</p>
<ul>
<li>low latitude diurnal cycle looks much better, particularly over land</li>
<li>initiation and propagation of systems over the Sahel looks pretty good</li>
<li>looks like the rainfall at mid-latitudes is rather less in the explicit run, and possibly rather more nearer the tropics. Is there any tuning in terms of the autoconversion/microphysics that might be needed?</li>
<li>not much improvement in propagation of systems over the US, and may well be even drier here.</li>
</ul>
<p></p>
<h2><a name="Jobs:"></a> Jobs:</h2>
<h2><a name="GA4"></a> GA4</h2>
<h3><a name="Parameterised convection"></a> Parameterised convection</h3>
<ul>
<li><a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/HiResCL/HadGEM3ampna" target="_top">ampna/d/p/r</a> - GA4 setup, using daily OSTIA SSTs/sea-ice. ampnd uses a shorter timestep (4 mins), as the model became unstable over Antarctica and I could not get it to go much past 2 months (though this may have been due to an initial bug in the CMIP5 ancillaries). The STASH list for this job (essentially the same in the explicit runs) is shown <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/JOBSHEET_stash" target="_top">here</a>, for the extra diagnostics the full stash list is <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/JOBSHEET_stash_ampnr" target="_top">here</a> and just the extra data is <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/JOBSHEET_stash_extra" target="_top">here</a>.</li>
</ul>
<p></p>
<p>VN (MAM 2008) vs GA4 N216 (1999-2008 MAM): Impact of resolution for GA4 models <br> Internal <a href="http://www-hc/~hadvg/valnote/ampna_v_xhcea/browser.html" target="_top">http://www-hc/~hadvg/valnote/ampna_v_xhcea/browser.html</a> <br> External <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampna_v_xhcea/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampna_v_xhcea/browser.html</a></p>
<p></p>
<p>VN N1024 (2008-9) vs GA4 N768 (2003-2010): Impact of resolution for GA4 models <br> Internal <a href="http://www-hc/~hadvg/valnote/ampna_v_alxgq/browser.html" target="_top">http://www-hc/~hadvg/valnote/ampna_v_alxgq/browser.html</a> <br> External <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampna_v_alxgq/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampna_v_alxgq/browser.html</a></p>
<p></p>
<p>VN N1024 (2008-10) vs GA4 N512 (1985-1999): Impact of resolution for GA4 models <br> Internal <a href="http://www-hc/~hadvg/valnote/ampnp_v_xgxqr/browser.html" target="_top">http://www-hc/~hadvg/valnote/ampnp_v_xgxqr/browser.html</a> <br> External <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnp_v_xgxqr/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnp_v_xgxqr/browser.html</a></p>
<p></p>
<p>VN (2008) vs GA4 N216 (1999-2008): Impact of resolution for GA4 models <br> Internal <a href="http://www-hc/~hadvg/valnote/ampna_v_xhcea/browser.html" target="_top">http://www-hc/~hadvg/valnote/ampna_v_xhcea/browser.html</a> <br> External <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampna_v_xhcea/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampna_v_xhcea/browser.html</a></p>
<p></p>
<h2><a name="GA5#93 (+bug fix)"></a> GA5#93 (+bug fix)</h2>
<p>Run id anbbp <br> VN N1024 (2008-2012) vs N512 (1991-2009): Internal: <a href="http://www-hc/~hadvg/valnote/anbbp_v_anbbd/browser.html" target="_top">http://www-hc/~hadvg/valnote/anbbp_v_anbbd/browser.html</a> <br> External <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/anbbp_v_anbbd/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/anbbp_v_anbbd/browser.html</a></p>
<p></p>
<h2><a name="GA6 (#95.13)"></a> GA6 (#95.13)</h2>
<p>Run id Run id <a href="http://collab.metoffice.gov.uk/trac/GA/wiki/GAJobs/answf" target="_top">answa and answf</a> <br>VN N1024 (2008-) vs N512 (1991-2009):</p>
<p></p>
<h3><a name="Parameterised shallow convection"></a> Parameterised shallow convection only</h3>
<h3><a name="GA4-only"></a> GA4-only</h3>
<ul>
<li><a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/HiResCL/HadGEM3ampnw" target="_top">ampnw/x</a> - as ampna but only parameterised shallow convection (like in CASCADE, with a grid-box scaled CAPE closure with a timescale of 20 mins), with the blended Smagorinsky scheme and effectively explicit deep convection (given the scaled CAPE). This model has fixed the bug in the scaled CAPE timescale (model ampno/v had the bug).</li>
</ul>
<p></p>
<p>VN (2008-10) vs ampnp (2008-11): Impact of shallow param vs full param convection <br> Internal <a href="http://www-hc/~hadvg/valnote/ampnw_v_ampnp/browser.html" target="_top">http://www-hc/~hadvg/valnote/ampnw_v_ampnp/browser.html</a> <br> External <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnw_v_ampnp/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnw_v_ampnp/browser.html</a> <br> VN (2008-9) vs ampna (2008-11): Impact of shallow param vs full param convection <br> Internal <a href="http://www-hc/~hadvg/valnote/ampnw_v_ampna/browser.html" target="_top">http://www-hc/~hadvg/valnote/ampnw_v_ampna/browser.html</a></p>
<p></p>
<h2><a name="GA6"></a> GA6</h2>
<p>Run id <a href="http://collab.metoffice.gov.uk/trac/GA/wiki/GAJobs/answc" target="_top">answc</a></p>
<p></p>
<h3><a name="Explicit convection"></a> Explicit convection</h3>
<h3><a name="GA4-only_AN1"></a> GA4-only</h3>
<ul>
<li><a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/HiResCL/HadGEM3ampnn" target="_top">ampnn/t</a> - as ampna, but switching off the convective parameterisation, and adding the blended Smagorinsky scheme (Adrian Lock), with fixes for the global model from Terry Davies/Adrian. ampnn - as ampng, include cloud erosion (missed in ampng/m as it now needs to be switched on since the convection scheme is bypassed). ampnn uses 4 min timestep from the start. With model instabilities so far, it has been found that setting the W_CONV_LIMIT higher and higher (25 currently) has helped, rather than the reverse with the parameterised run - so less limiting seems to be more stable. ampnt has the extra diagnostics for the 2nd year.</li>
</ul>
<p></p>
<p>VN (2008-11) vs ampna (2008-11): Impact of explicit convection <br> Internal <a href="http://www-hc/~hadvg/valnote/ampnn_v_ampna/browser.html" target="_top">http://www-hc/~hadvg/valnote/ampnn_v_ampna/browser.html</a> <br> External <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnn_v_ampna/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnn_v_ampna/browser.html</a></p>
<p></p>
<p>Notable differences (comments from experts):</p>
<ul>
<li>The trade cumulus areas are much brighter (and I think ISCCP is brighter than the preferred EBAF climatology so it would look worse against that) so that might still motivate a shallow cumulus parametrization. (Adrian Lock)</li>
<li>I was particularly struck by the change in ice cloud in the tropics. I guess that could just be too strong/wrong scale updraughts in a 20km grid getting the moisture transport wrong but I did wonder if the large scale microphysics might be saying something about where to do the phase change in the convection scheme? I didn't think the end product looked too bad, eg against the ISCCP diagnostics! (Adrian Lock)</li>
<li>Check out Waliser fig 5 for a comparison: <a href="http://www.agu.org/journals/jd/jd0902/2008JD010015/" target="_top">http://www.agu.org/journals/jd/jd0902/2008JD010015/</a> .He shows a peak of 24mg/m3 =~50mg/kg = 5e-5 kg/kg (assuming an air density of about 0.5 kg/m3), which agrees quite well - unless I have my arithmetic wrong! (from Paul Field). The Waliser figure is <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/waliser.jpeg" target="_top">here</a>, and the model figure is <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnn_v_ampna/pngi/0280qcftwodifjja.png" target="_top">here - note on model levels</a>. The cloud ice, averaged between 4900-12300m, is shown <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/cloud_ice_jja_4900_12300_mean.png" target="_top">here</a>.</li>
<li>I would have thought that all the extra cloud in the explicit convection run is the "convective cores" that the large scale cloud isn't including in the param convection run. There seems to be quite a lot of it!! I'm not sure if it tells you much about the phase change temperature in the convective plume, because what you are seeing in the diagnostic has had time to freeze. (Ian Boutle)</li>
<li>NICAM has an increase in ice like this, though they get increases in all high level clouds, while only the thick cloud increases here. (Yoko Tsushima)</li>
</ul>
<p></p>
<p>VN (2008/9) vs ampnw (2008): Impact of shallow param vs full param convection <br> Internal <a href="http://www-hc/~hadvg/valnote/ampnn_v_ampnw/browser.html" target="_top">http://www-hc/~hadvg/valnote/ampnn_v_ampnw/browser.html</a> <br> <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnn_v_ampnw/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnn_v_ampnw/browser.html</a></p>
<p></p>
<h2><a name="Results"></a> Results</h2>
<h3><a name="Diurnal cycle"></a> Diurnal cycle</h3>
<p>Using Reinhard Schiemann's R code to calculate the diurnal cycle from 3 hourly rainfall, with a harmonic fitted to smooth the results, the results from the 3 models and from TRMM observations is shown below. It is noticable that the shallow convection parameterisation looks much like the fully parameterised model for the diurnal cycle, which is not what was found in the CASCADE runs I think. The ocean continues to be interesting, given that the SST only updates every day, but the parameterised and explicit give very different results here (though may need to check for robustness and the cycle should be weaker over the ocean. Over land, the explicit model captures the observed cycle extremely well it seems. <br> <img alt="diurnal_ampnawn_trmm_ducmap3.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_ampnawn_trmm_ducmap3.png"></p>
<p></p>
<p>Looking at the fraction of precip that is large-scale vs convective (in model terms, explicit vs parameterised really) between GA4 and shallow runs, we see that over land nearly all the precip in the shallow run is large-scale, but there are regions over the ocean where the shallow run has a large proportion of its rainfall as convection. <img alt="fraction_precip.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/fraction_precip.png"></p>
<p></p>
<p>Looking at the precipitation and OLR characteristics over Africa, I chose 5 regions: central (0-2E, 10-12N), south (0-2E, 5-7N), east (8-10E, 10-12N), north (0-2E, 13-15N) and west (10-8W, 10-12N), and ocean (63-65E, 0-3N). The correlations for OLR vs precip for each region (Obs are TRMM and GridSat brightness temperature) using 3 hourly data for JJA 2008 are:</p>
<p></p>
<table border="1" cellpadding="0" cellspacing="0" class="twikiTable" id="table1" rules="rows">
<tbody>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0"><th class="twikiTableCol0 twikiFirstCol" valign="top"><span color="#ffffff" style="">N1024 run</span></th><th class="twikiTableCol1" valign="top"><span color="#ffffff" style="">Central</span></th><th class="twikiTableCol2" valign="top"><span color="#ffffff" style="">South</span></th><th class="twikiTableCol3" valign="top"><span color="#ffffff" style="">East</span></th><th class="twikiTableCol4" valign="top"><span color="#ffffff" style="">North</span></th><th class="twikiTableCol5" valign="top"><span color="#ffffff" style="">West</span></th>
<td class="twikiTableCol6 twikiLastCol" valign="top">IndianO</td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol" valign="top">ampnd GA4</td>
<td class="twikiTableCol1" valign="top">0.04</td>
<td class="twikiTableCol2" valign="top">-0.58</td>
<td class="twikiTableCol3" valign="top">-0.04</td>
<td class="twikiTableCol4" valign="top">-0.2</td>
<td class="twikiTableCol5" valign="top">-0.25</td>
<td class="twikiTableCol6 twikiLastCol" valign="top">-0.85</td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top">ampnw SP</td>
<td class="twikiTableCol1" valign="top">-0.34</td>
<td class="twikiTableCol2" valign="top">-0.48</td>
<td class="twikiTableCol3" valign="top">-0.31</td>
<td class="twikiTableCol4" valign="top">-0.40</td>
<td class="twikiTableCol5" valign="top">-0.32</td>
<td class="twikiTableCol6 twikiLastCol" valign="top">-0.52</td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol" valign="top">ampnn NP</td>
<td class="twikiTableCol1" valign="top">-0.46</td>
<td class="twikiTableCol2" valign="top">-0.45</td>
<td class="twikiTableCol3" valign="top">-0.45</td>
<td class="twikiTableCol4" valign="top">-0.29</td>
<td class="twikiTableCol5" valign="top">-0.44</td>
<td class="twikiTableCol6 twikiLastCol" valign="top">-0.61</td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol twikiLast" valign="top">TRMM/GridSat</td>
<td class="twikiTableCol1 twikiLast" valign="top">-0.66</td>
<td class="twikiTableCol2 twikiLast" valign="top">-0.59</td>
<td class="twikiTableCol3 twikiLast" valign="top">-0.63</td>
<td class="twikiTableCol4 twikiLast" valign="top">-0.62</td>
<td class="twikiTableCol5 twikiLast" valign="top">-0.71</td>
<td class="twikiTableCol6 twikiLastCol twikiLast" valign="top">-0.52</td>
</tr>
</tbody>
</table>
<p></p>
<p>And these are the precip spectra for these different regions. Where the diurnal cycle is the dominant part of the variability, the GA4 power spectra has a strong diurnal peak, but much weaker variability at other timescales (e.g. central, <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/olr_precip_ts_central.png" target="_top">here</a>). Where the diurnal cycle is small relative to the more extreme events (such as in the north), then the spectra looks more like that from the explicit models and observations (e.g. <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/olr_precip_ts_north.png" target="_top">here</a>). Over the ocean the GA4 model tends to have more sustained precipitation than the other models and obs (and the OLR variability is similarly longer timescale), e.g. <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/olr_precip_ts_ocean.png" target="_top">here</a>. The first plot uses the (recommended) window for the power spectra of 2*sqrt(no. points), and hence gives a smoother (and shorter) spectra than the second.</p>
<p></p>
<p><img alt="olr_precip_power_sm.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/olr_precip_power_sm.png"></p>
<p></p>
<p><img alt="olr_precip_power.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/olr_precip_power.png"></p>
<p></p>
<h3><a name="Old plots"></a> Old plots</h3>
<p><span class="twistyPlugin twikiMakeVisibleInline"> <span class="twistyTrigger twikiUnvisited twistyHidden twistyInited" id="twistyIdProject/HiResCLHiResCLN1024Model1show"><a href="#"><span class="twikiLinkLabel twikiUnvisited">unhide</span></a> </span> <span class="twistyTrigger twikiUnvisited twistyHidden twistyInited" id="twistyIdProject/HiResCLHiResCLN1024Model1hide"><a href="#"><span class="twikiLinkLabel twikiUnvisited">Close</span></a> </span> </span></p>
<!--/twistyPlugin twikiMakeVisibleInline-->
<p><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited" id="twistyIdProject/HiResCLHiResCLN1024Model1toggle"> The diurnal cycle, as calculated from 3hrly precipitation maxima, using idl, from MAM 2008 only. Places where the maximum precipitation lies below 0.02 mm/h are missing data. <br> MAM 2008 from N1024 parameterised and explicit convection (ampna and ampnn) and TRMM: <br> <img alt="diurnal_MAM_model_trmm_global.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_MAM_model_trmm_global.png"> <img alt="diurnal_MAM_model_trmm_amazon.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_MAM_model_trmm_amazon.png"> <img alt="diurnal_MAM_model_trmm_sahel.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_MAM_model_trmm_sahel.png"> <img alt="diurnal_MAM_model_trmm_EU.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_MAM_model_trmm_EU.png"> <img alt="diurnal_MAM_model_trmm_India.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_MAM_model_trmm_India.png"> <img alt="diurnal_MAM_model_trmm_US.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_MAM_model_trmm_US.png"> <img alt="diurnal_MAM_model_trmm_sahel.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_MAM_model_trmm_sahel.png"> </span></span></p>
<!--/twistyPlugin-->
<p></p>
<h3><a name="Africa"></a> Africa</h3>
<h4><a name="Diurnal Cycle over West Africa"></a> Diurnal Cycle over West Africa</h4>
<p></p>
<p>Over Africa, to compare with the CASCADE plots from Cathryn <a href="mailto:Birch@Leeds">Birch@Leeds</a>, are hovmuller plots of the rainfall averaged between 8-18N, both for a repeat mean diurnal cycle, and for the Jul-Aug period - note TRMM is 3hourly data while the model is hourly. It is clear that the shallow param run looks more like the full param run for the timing of the diurnal cycle, but seemingly has as good propagation of the systems as the explicit run, suggesting some interesting interactions between the shallow and deep convection - explicit deep apparently needed for the propagation. Looking at the full period below, the shallow param run again has this clear "shutter pattern" of the diurnal cycle that the fully param run has.</p>
<p></p>
<table border="1" cellpadding="0" cellspacing="0" class="twikiTable" id="table2" rules="rows">
<tbody>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top">Diurnal cycle</td>
<td class="twikiTableCol1" valign="top">Orography cross-section</td>
<td class="twikiTableCol2 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol twikiLast" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/africa_ampnd_ampnn_ampnw_trmm_1hrmn.png"><img align="left" alt="" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/africa_ampnd_ampnn_ampnw_trmm_1hrmn.png" width="550"></a></td>
<td class="twikiTableCol1 twikiLast" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/africa_orog_815n.png"><img align="left" alt="" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/africa_orog_815n.png" width="500"></a></td>
<td class="twikiTableCol2 twikiLastCol twikiLast" valign="top"><img align="left" alt="" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/africa_ampna_ampnn_ampnw_trmm_1hrmn_full.png" width="50"></td>
</tr>
</tbody>
</table>
<p></p>
<h4><a name="Diurnal Cycle over Lake Victoria"></a> Diurnal Cycle over Lake Victoria</h4>
<p></p>
<p>The diurnal cycle in the explicit runs isn't better than parameterised everywhere:</p>
<p></p>
<p>Lake Victoria has a strong diurnal cycle which is regulated by the lake-land breeze caused by diurnal temperature contrasts. Storms over the lake peak in the morning 06-12 Local time. The plots below show that the cycle is well captured by the parameterised convection model (ampna), which also appears to behave better than the explicit convection model (ampnn) at N1024. The explicit model has convection occurring slightly too late in the cycle, though there is a trace of increased convective activity over the mountains to the north-east at 15 UTC.</p>
<p></p>
<table border="1" cellpadding="0" cellspacing="0" class="twikiTable" id="table3" rules="rows">
<tbody>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol twikiLastCol" valign="top">TRMM rainfall observations</td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol twikiLastCol twikiLast" valign="top"><img align="left" alt="" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/trmmdiurnalcycle_LV.png" width="400"></td>
</tr>
</tbody>
</table>
<p></p>
<table border="1" cellpadding="0" cellspacing="0" class="twikiTable" id="table4" rules="rows">
<tbody>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top">ampna Parameterised N1024</td>
<td class="twikiTableCol1 twikiLastCol" valign="top">ampnn Explicit N1024</td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol twikiLast" valign="top"><img align="left" alt="" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnadiurnalcycle_LV.png" width="400"></td>
<td class="twikiTableCol1 twikiLastCol twikiLast" valign="top"><img align="left" alt="" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnndiurnalcycle_LV.png" width="400"></td>
</tr>
</tbody>
</table>
<p></p>
<p><em>Caroline Bain</em></p>
<p></p>
<h4><a name="West African Monsoon and ITCZ ov"></a> West African Monsoon and ITCZ over the Atlantic</h4>
<p></p>
<p>The West African Monsoon occurs July-Sept. In early summer the ITCZ shifts from it's location over the Guinea coast to more northern latitudes. In mean time-latitude plots this transition appears as a 'jump' in the location of the rains and is referred to as monsoon onset. The HADGEM3 models do a good job of representing this mean progression of monsoon rainfall. This is very encouraging considering that reanalysis tend to struggle with representation (e.g. see Vellinga et. al, 2012). Below are the monsoon progression plots for GPCP=satellite+gauge, GA4 and the N1024 experiments. The plots have been split into two components - the ITCZ/monsoon progression over the Gulf of Guinea and West Africa 0-20N, 18W-5E and another box over the Atlantic Ocean 0-20N, 50W-18W</p>
<p></p>
<p>The plots are made from daily mean rainfall which is then smoothed with a 5 day running mean. The GPCP and GA4 plots show multiple years (hence their smooth appearance). The N1024 plots are for one year only.</p>
<p></p>
<table border="1" cellpadding="0" cellspacing="0" class="twikiTable" id="table5" rules="rows">
<tbody>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top">GPCP rainfall observations 1997-2008</td>
<td class="twikiTableCol1 twikiLastCol" valign="top">GA4 N96 1997-2008</td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol twikiLast" valign="top"><img align="left" alt="" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/gpcpitcz_landoceanhov.png" width="500"></td>
<td class="twikiTableCol1 twikiLastCol twikiLast" valign="top"><img align="left" alt="" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliuritcz_landoceanhov.png" width="500"></td>
</tr>
</tbody>
</table>
<p></p>
<table border="1" cellpadding="0" cellspacing="0" class="twikiTable" id="table6" rules="rows">
<tbody>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top">ampna Parameterised N1024 2008, 2009, 2010, 2011 (4 years)</td>
<td class="twikiTableCol1 twikiLastCol" valign="top">ampnn Explicit N1024 2008 (1 year only)</td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol twikiLast" valign="top"><img align="left" alt="" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnaitcz_landoceanhov_4yrs.png" width="500"></td>
<td class="twikiTableCol1 twikiLastCol twikiLast" valign="top"><img align="left" alt="" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnnitcz_landoceanhov.png" width="500"></td>
</tr>
</tbody>
</table>
<p></p>
<p>One significant finding is that both versions of the N1024 model do not necessarily appear to have any more northward migration of rains in comparison to GA4. Though thing to note is that convection appears stronger in the N1024 model - this is a improvement over the land regions but makes the positive rainfall bias over the ocean worse. For more conversation on the ITCZ, its representation in observations and models go to: <a href="http://www-hc.metoffice.com/~hadlb/ITCZAfrica/">http://www-hc.metoffice.com/~hadlb/ITCZAfrica/</a> (internal only) <em>Caroline Bain</em></p>
<p></p>
<h4><a name="African Easterly Waves"></a> African Easterly Waves</h4>
<p></p>
<p>African Easterly Waves are westward propagating dynamical disturbances between 700-850hPa over West Africa during the monsoon. Rainfall over the continent is modulated by AEW events. The plots below are from tracking code developed by Caroline Bain. This is now available in Autoassess and can handle stash split files. All of the results for different versions of the climate model can be found at <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/PEGAfrica_GAEval/index.html#Sec_AEW">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/PEGAfrica_GAEval/index.html#Sec_AEW</a>.</p>
<p></p>
<p>The main deficiency in the N96 climate model (i.e. GA4) is that the AEWs are too weak and have too little rainfall coupling. There is also a reduction in the frequency of wave events compared to the ECMWF. The below experiments show that high resolution N1024 improves the dynamical strength of the waves. The waves are almost the same strength as the ERA-I waves in the explicit runs but the rainfall is far too strong and potentially too coupled to the AEWs (?? though it is difficult to know this for sure due to the resolution of the observations being lower than N1024... so the observations signal could be smoothed).</p>
<p></p>
<p>CLICK ON THE IMAGES TO VIEW ENLARGED VERSIONS</p>
<p></p>
<table border="1" cellpadding="0" cellspacing="0" class="twikiTable" id="table7" rules="rows">
<tbody>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top"> </td>
<td class="twikiTableCol1" valign="top">Example of AEW vorticity</td>
<td class="twikiTableCol2" valign="top">Example of AEW rainfall</td>
<td class="twikiTableCol3" valign="top">AEW to rainfall coupling</td>
<td class="twikiTableCol4 twikiLastCol" valign="top">AEW stats compared with ERAI</td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol" valign="top">ERAI reanalysis and GPCP rainfall</td>
<td class="twikiTableCol1" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/erai_egAEWhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/erai_egAEWhov.png"></a></td>
<td align="right" class="twikiTableCol2" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/erai_egAEWRAINhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/erai_egAEWRAINhov.png"></a></td>
<td align="right" class="twikiTableCol3" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/erai_raincoupling.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/erai_raincoupling.png"></a></td>
<td class="twikiTableCol4 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top">GA4 N96 aliur</td>
<td align="right" class="twikiTableCol1" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_egAEWhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_egAEWhov.png"></a></td>
<td class="twikiTableCol2" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_egAEWRAINhov.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_egAEWRAINhov.png"></a></td>
<td class="twikiTableCol3" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_raincoupling.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_raincoupling.png"></a></td>
<td class="twikiTableCol4 twikiLastCol" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_AEWstats.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_AEWstats.png"></a></td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol" valign="top">N1024 parameterised ampna</td>
<td align="right" class="twikiTableCol1" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampna_egAEWhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampna_egAEWhov.png"></a></td>
<td align="right" class="twikiTableCol2" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampna_egAEWRAINhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampna_egAEWRAINhov.png"></a></td>
<td class="twikiTableCol3" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampna_raincoupling.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampna_raincoupling.png"></a></td>
<td class="twikiTableCol4 twikiLastCol" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampna_AEWstats.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampna_AEWstats.png"></a></td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol twikiLast" valign="top">N1024 explicit ampnn</td>
<td align="right" class="twikiTableCol1 twikiLast" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_egAEWhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_egAEWhov.png"></a></td>
<td align="right" class="twikiTableCol2 twikiLast" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_egAEWRAINhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_egAEWRAINhov.png"></a></td>
<td align="right" class="twikiTableCol3 twikiLast" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_raincoupling.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_raincoupling.png"></a></td>
<td align="right" class="twikiTableCol4 twikiLastCol twikiLast" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_AEWstats.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_AEWstats.png"></a></td>
</tr>
</tbody>
</table>
<p></p>
<p><em>Caroline Bain</em></p>
<p></p>
<table border="1" cellpadding="0" cellspacing="0" class="twikiTable" id="table8" rules="rows">
<tbody>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top"> </td>
<td class="twikiTableCol1" valign="top">Example of AEW vorticity</td>
<td class="twikiTableCol2" valign="top">Example of AEW rainfall</td>
<td class="twikiTableCol3" valign="top">AEW to rainfall coupling</td>
<td class="twikiTableCol4 twikiLastCol" valign="top">AEW stats compared with ERAI</td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol" valign="top">ERAI reanalysis and GPCP rainfall</td>
<td class="twikiTableCol1" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/erai_egAEWhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/erai_egAEWhov.png"></a></td>
<td align="right" class="twikiTableCol2" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/erai_egAEWRAINhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/erai_egAEWRAINhov.png"></a></td>
<td align="right" class="twikiTableCol3" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/erai_raincoupling.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/erai_raincoupling.png"></a></td>
<td class="twikiTableCol4 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top">GA4 N96 aliur</td>
<td align="right" class="twikiTableCol1" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_egAEWhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_egAEWhov.png"></a></td>
<td class="twikiTableCol2" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_egAEWRAINhov.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_egAEWRAINhov.png"></a></td>
<td class="twikiTableCol3" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_raincoupling.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_raincoupling.png"></a></td>
<td class="twikiTableCol4 twikiLastCol" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_AEWstats.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_AEWstats.png"></a></td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol" valign="top">GA3 N96-UPSCALE xhqin 1992-11</td>
<td align="right" class="twikiTableCol1" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xhqin_egAEWhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xhqin_egAEWhov.png"></a></td>
<td class="twikiTableCol2" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xhqin_egAEWRAINhov.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xhqin_egAEWRAINhov.png"></a></td>
<td class="twikiTableCol3" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xhqin_raincoupling.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xhqin_raincoupling.png"></a></td>
<td class="twikiTableCol4 twikiLastCol" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xhqin_AEWstats.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xhqin_AEWstats.png"></a></td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top">GA3 N216-UPSCALE xgxqo 1992-11</td>
<td align="right" class="twikiTableCol1" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqo_egAEWhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqo_egAEWhov.png"></a></td>
<td class="twikiTableCol2" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqo_egAEWRAINhov.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqo_egAEWRAINhov.png"></a></td>
<td class="twikiTableCol3" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqo_raincoupling.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqo_raincoupling.png"></a></td>
<td class="twikiTableCol4 twikiLastCol" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqo_AEWstats.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqo_AEWstats.png"></a></td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol" valign="top">GA3 N512-UPSCALE xgxqe 1992-11</td>
<td align="right" class="twikiTableCol1" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqe_egAEWhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqe_egAEWhov.png"></a></td>
<td class="twikiTableCol2" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqe_egAEWRAINhov.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqe_egAEWRAINhov.png"></a></td>
<td class="twikiTableCol3" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqe_raincoupling.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqe_raincoupling.png"></a></td>
<td class="twikiTableCol4 twikiLastCol" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqe_AEWstats.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqe_AEWstats.png"></a></td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top">GA3 N512-UPSCALE xgxqk Timeslice 1992-11</td>
<td align="right" class="twikiTableCol1" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqk_egAEWhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqk_egAEWhov.png"></a></td>
<td class="twikiTableCol2" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqk_egAEWRAINhov.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqk_egAEWRAINhov.png"></a></td>
<td class="twikiTableCol3" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqk_raincoupling.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqk_raincoupling.png"></a></td>
<td class="twikiTableCol4 twikiLastCol" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqk_AEWstats.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqk_AEWstats.png"></a></td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol" valign="top">GA4 N1024 ampna 2008-11</td>
<td align="right" class="twikiTableCol1" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnr_egAEWhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnr_egAEWhov.png"></a></td>
<td class="twikiTableCol2" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnr_egAEWRAINhov.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnr_egAEWRAINhov.png"></a></td>
<td class="twikiTableCol3" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnr_raincoupling.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnr_raincoupling.png"></a></td>
<td class="twikiTableCol4 twikiLastCol" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnr_AEWstats.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnr_AEWstats.png"></a></td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol twikiLast" valign="top">Exp conv N1024 ampnn 2008-11</td>
<td align="right" class="twikiTableCol1 twikiLast" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_egAEWhov.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_egAEWhov.png"></a></td>
<td class="twikiTableCol2 twikiLast" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_egAEWRAINhov.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_egAEWRAINhov.png"></a></td>
<td class="twikiTableCol3 twikiLast" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_raincoupling.png"> <img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_raincoupling.png"></a></td>
<td class="twikiTableCol4 twikiLastCol twikiLast" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_AEWstats.png"><img align="left" alt="" height="250" src="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_AEWstats.png"></a></td>
</tr>
</tbody>
</table>
<p></p>
<h3><a name="USA"></a> USA</h3>
<p></p>
<p>Over the US between 35-45N, again for just 2008 July/Aug period, the hovmuller (comparable to that on page <a href="http://collab.metoffice.gov.uk/twiki/bin/view/Development/USWarmBias" target="_top">http://collab.metoffice.gov.uk/twiki/bin/view/Development/USWarmBias</a>), the mean diurnal cycle for the 3 runs is:</p>
<p></p>
<p><img alt="usa_ampnd_ampnn_ampnw_trmm_1hrmn.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/usa_ampnd_ampnn_ampnw_trmm_1hrmn.png"></p>
<p></p>
<p>with orography cross-section</p>
<p></p>
<p><img alt="usa_orog_3545n.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/usa_orog_3545n.png"></p>
<p></p>
<p>and for the full period over which the mean is taken, the rainfall looks like</p>
<p></p>
<p><img alt="usa_ampnd_ampnn_ampnw_trmm_1hrmn_full.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/usa_ampnd_ampnn_ampnw_trmm_1hrmn_full.png"></p>
<p></p>
<p>The explicit run here looks to be much drier than the parameterised, and although the time of convection is a little different, there seems to be few propagating events in this small dataset.</p>
<p></p>
<h3><a name="MJO"></a> MJO</h3>
<p>With only 12 months of data currently, the MJO plots only produce frequency/wave number plots, and these are very noisy, but shown here anyway (MO Internal link only for now):</p>
<p></p>
<p>N1024 explicit vs parameterised ampnn/ampna: (Internal) <a href="http://www-hc/~hadom/configman/MJO/ampnn/" target="_top">http://www-hc/~hadom/configman/MJO/ampnn/</a> <br> (External): <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/mjo_ampnn_ampna.pdf" target="_top">http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/mjo_ampnn_ampna.pdf</a></p>
<p></p>
<p>N1024 parameterised vs N512 10 years: (Internal) <a href="http://www-hc/~hadom/configman/MJO/ampna/" target="_top">http://www-hc/~hadom/configman/MJO/ampna/</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/mjo_ampna_xgxqe.pdf" target="_top">http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/mjo_ampna_xgxqe.pdf</a></p>
<p></p>
<p>for reference, the N512 vs N216, and N216 vs N96, MJO plots, for 10 years each, are at <br> N512 (xgxqe) vs N216 (xgxqo): (Internal) <a href="http://www-hc/~hadom/configman/MJO/xgxqe/" target="_top">http://www-hc/~hadom/configman/MJO/xgxqe/</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/mjo_xgxqe_xgxqo.pdf" target="_top">http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/mjo_xgxqe_xgxqo.pdf</a></p>
<p></p>
<p><br> N216 (xgxqo) vs N96 (ajqmo): <a href="http://www-hc/~hadom/configman/MJO/xgxqo/" target="_top">http://www-hc/~hadom/configman/MJO/xgxqo/</a></p>
<p></p>
<h3><a name="QBO"></a> QBO</h3>
<p></p>
<p>The QBO is a periodic disturbance on the equatorial stratospheric jet, with descending anomalies . Vertical propagation of a broad spectrum of waves is believed to be essential for this instability on the stratospheric jet to occur. Representing the QBO in models relies on parameterising subgrid-scale upward propagating waves into the stratosphere, essentially gravity waves as represented by the non-orographic gravity wave scheme (NOGWS). Both N1024 explicit and parameterised runs use the same NOGWS. Whereas in the case of parameterised convection this results in a relaistic QBO, in the explicit configuration the QBO is too weak, too shallow and has too high a period. Cumulus convection is an important source of GW and the different treatment of convection in both configurations suggests that the explicit configuration would have benefited from a retuned NOGWS (arguably reducing its amplitude as we expect explicit convection to be more efficient at generating resolved gravity waves). A complicating factor is that the QBO in models is also affected by biases in the Brwewer-Dobson circulation - which itself is forced by drag from upward propagating waves. <a href="https://code.metoffice.gov.uk/trac/GA/ticket/165" target="_top">Recent work by Andfrew Bushell</a> has shown the need to retune the NOGWS at GA7 for different resolutions to maintain the correct peiod of the QBO. In the case of the GA4 N1024 models clearly the resolution is the same, so the demise of the QBO in the explicit convection case is an example of non-resolution dependence. It would be worth to estimate the gravity wave forcing in the two (explicit/parameterised) cases to see if the different representation of cumulus convection results in a susbstantial difference in the resolved GW spectrum. Not sure if the available <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/JOBSHEET_stash_ampnr" target="_top">standard</a> or <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/JOBSHEET_stash_extra" target="_top">extra diagnostics</a>make this a straightforward thing to do.</p>
<h6><a name="QBO in N1024 parameterised:"></a> QBO in N1024 parameterised:</h6>
<p></p>
<p><img alt="QBO_N1024.param.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/QBO_N1024.param.png"></p>
<h6><a name="QBO in N1024 explicit:"></a> QBO in N1024 explicit:</h6>
<p></p>
<p><img alt="QBO_N1024.expl.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/QBO_N1024.expl.png"></p>
<p></p>
<h3><a name="Older plots"></a> Older plots</h3>
<p><span class="twistyPlugin twikiMakeVisibleInline"> <span class="twistyTrigger twikiUnvisited twistyHidden twistyInited" id="twistyIdProject/HiResCLHiResCLN1024Model2show"><a href="#"><span class="twikiLinkLabel twikiUnvisited">unhide</span></a> </span> <span class="twistyTrigger twikiUnvisited twistyHidden twistyInited" id="twistyIdProject/HiResCLHiResCLN1024Model2hide"><a href="#"><span class="twikiLinkLabel twikiUnvisited">Close</span></a> </span> </span></p>
<!--/twistyPlugin twikiMakeVisibleInline-->
<p><span class="twistyPlugin"><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited">These older plots made with the R script from Reinhard:</span></span></span></p>
<p></p>
<p><span class="twistyPlugin"><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited">Reinhard has an R script to calculate the local time of maximum precipitation. I've used this for the (Mar-Apr 2008) period, and this was also done for TRMM observations. Here are plots of various regions:</span></span></span></p>
<p></p>
<p><span class="twistyPlugin"><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited">Global <br> <img alt="diurnal_n1024_marapr2008_global.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_n1024_marapr2008_global.png"></span></span></span></p>
<p></p>
<p><span class="twistyPlugin"><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited">Europe<br> <img alt="diurnal_n1024_marapr2008_EU.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_n1024_marapr2008_EU.png"></span></span></span></p>
<p></p>
<p><span class="twistyPlugin"><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited">Maritime continent<br> <img alt="diurnal_n1024_marapr2008_MC.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_n1024_marapr2008_MC.png"></span></span></span></p>
<p></p>
<p><span class="twistyPlugin"><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited">India<br> <img alt="diurnal_n1024_marapr2008_India.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_n1024_marapr2008_India.png"></span></span></span></p>
<p></p>
<p><span class="twistyPlugin"><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited">Sahel<br> <img alt="diurnal_n1024_marapr2008_sahel.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_n1024_marapr2008_sahel.png"></span></span></span></p>
<p></p>
<p><span class="twistyPlugin"><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited">Amazon<br> <img alt="diurnal_n1024_marapr2008_amazon.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_n1024_marapr2008_amazon.png"></span></span></span></p>
<p></p>
<p><span class="twistyPlugin"><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited">Testing some settings of the N1024 model.</span></span></span></p>
<p></p>
<p><span class="twistyPlugin"><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited">5 day runs so far, with parameterised convection, and 3D Blended Smagorinsky (with convection scheme switched off).</span></span></span></p>
<p></p>
<p><span class="twistyPlugin"><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited">Parameterised convection (GA4 setup): OLR animation <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/n1024_pc_ampnd.mp4" target="_top">http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/n1024_pc_ampnd.mp4</a></span></span></span></p>
<p></p>
<p><span class="twistyPlugin"><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited">Explicit convection (3D blended Smagorinsky): OLR animation <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/n1024_ec_ampnf.mp4" target="_top">http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/n1024_ec_ampnf.mp4</a></span></span></span></p>
<p></p>
<p><span class="twistyPlugin"><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited">A comparison of the two: <a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HiResCLN1024Model/N1024.avi" target="_top">N1024.avi</a></span></span></span></p>
<p></p>
<p><span class="twistyPlugin"><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited">VN ampng (MAM 2008) vs ampna (MAM 2008): Impact of explicit convection (but with no cloud erosion in explicit run, so SW badly wrong) <br> Internal <a href="http://www-hc/~hadvg/valnote/ampnn_v_ampna/browser.html" target="_top">http://www-hc/~hadvg/valnote/ampnn_v_ampna/browser.html</a> <br> External <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnn_v_ampna/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnn_v_ampna/browser.html</a></span></span></span></p>
<p></p>
<ul>
<li><a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/HiResCL/HadGEM3ampno" target="_top">ampno</a> - as ampna but only parameterised shallow convection (like in CASCADE, with a grid-box scaled CAPE closure with a timescale of 20 mins), with the blended Smagorinsky scheme and effectively explicit deep convection (given the scaled CAPE). This model has a bug (the scaled CAPE timescale did not work properly), and hence is invalid.</li>
</ul>
<p></p>
<p><span class="twistyPlugin"><span class="twistyPlugin"><span class="twistyContent twikiMakeHidden twistyInited">VN (JJA 2008) vs ampna (2008): Impact of shallow param vs full param convection <br> Internal <a href="http://www-hc/~hadvg/valnote/ampno_v_ampna/browser.html" target="_top">http://www-hc/~hadvg/valnote/ampno_v_ampna/browser.html</a></span></span></span></p>
<p></p>
<p></p>
<!--/twistyPlugin-->
<p></p>
<p>-- Main.MalcolmRoberts - 2012-10-07</p>
<!-- /patternTopic-->
<div class="twikiContentFooter"></div>
<div class="twikiAttachments">
<div class="twistyPlugin twikiMakeVisibleInline"><span class="twistyRememberSetting twistyTrigger twikiUnvisited twistyHidden twistyInited1" id="topicattachmentslistshow"><a href="#"><img alt="" border="0" src="/twiki/pub/TWiki/TWikiDocGraphics/toggleopen.gif"><span class="twikiLinkLabel twikiUnvisited">Attachments</span></a> </span> <span class="twistyRememberSetting twistyTrigger twikiUnvisited twistyInited1" id="topicattachmentslisthide"><a href="#"><img alt="" border="0" src="/twiki/pub/TWiki/TWikiDocGraphics/toggleclose.gif"><span class="twikiLinkLabel twikiUnvisited">Attachments</span></a> </span></div>
<!--/twistyPlugin twikiMakeVisibleInline-->
<div class="twistyPlugin">
<div class="twistyRememberSetting twistyContent twistyInited1" id="topicattachmentslisttoggle">
<table border="1" cellpadding="0" cellspacing="0" class="twikiTable" id="twikiAttachmentsTable" rules="rows" summary="Topic attachments"><caption>Topic attachments</caption>
<tbody>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0"><th class="twikiTableCol0 twikiFirstCol" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HiResCLN1024Model?sortcol=0;table=9;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">I</span></a></th><th class="twikiTableCol1" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HiResCLN1024Model?sortcol=1;table=9;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Attachment</span></a></th><th class="twikiTableCol2" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HiResCLN1024Model?sortcol=2;table=9;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Action</span></a></th><th class="twikiTableCol3" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HiResCLN1024Model?sortcol=3;table=9;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Size</span></a></th><th class="twikiTableCol4" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HiResCLN1024Model?sortcol=4;table=9;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Date</span></a></th><th class="twikiTableCol5" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HiResCLN1024Model?sortcol=5;table=9;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Who</span></a></th><th class="twikiTableCol6 twikiLastCol" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HiResCLN1024Model?sortcol=6;table=9;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Comment</span></a></th></tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="else" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/else.gif" width="16"><span class="twikiHidden">EXT</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/JOBSHEET_stash">JOBSHEET_stash</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=JOBSHEET_stash;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">166.8 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-29 - 09:52</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="else" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/else.gif" width="16"><span class="twikiHidden">EXT</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/JOBSHEET_stash_ampnr">JOBSHEET_stash_ampnr</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=JOBSHEET_stash_ampnr;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">58.0 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-01-15 - 12:20</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="else" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/else.gif" width="16"><span class="twikiHidden">EXT</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/JOBSHEET_stash_extra">JOBSHEET_stash_extra</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=JOBSHEET_stash_extra;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">1.9 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-01-15 - 12:19</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="mov" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/mov.gif" width="16"><span class="twikiHidden">avi</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/N1024.avi">N1024.avi</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=N1024.avi;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">5598.4 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-10-08 - 13:29</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MatthewMizielinski">MatthewMizielinski</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/QBO_N1024.expl.png">QBO_N1024.expl.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=QBO_N1024.expl.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">39.9 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2016-01-12 - 09:48</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MichaelVellinga">MichaelVellinga</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top">QBO explicit</td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/QBO_N1024.param.png">QBO_N1024.param.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=QBO_N1024.param.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">77.7 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2016-01-12 - 09:47</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MichaelVellinga">MichaelVellinga</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top">QBO parameterised</td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/africa_ampnd_ampnn_ampnw_trmm_1hrmn.png">africa_ampnd_ampnn_ampnw_trmm_1hrmn.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=africa_ampnd_ampnn_ampnw_trmm_1hrmn.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">79.2 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-06-20 - 17:07</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/africa_ampnd_ampnn_ampnw_trmm_1hrmn_full.png">africa_ampnd_ampnn_ampnw_trmm_1hrmn_full.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=africa_ampnd_ampnn_ampnw_trmm_1hrmn_full.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">177.5 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-05 - 10:36</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/africa_orog_815n.png">africa_orog_815n.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=africa_orog_815n.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">5.9 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-26 - 09:44</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_AEWstats.png">aliur_AEWstats.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=aliur_AEWstats.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">37.4 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 14:36</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_egAEWRAINhov.png">aliur_egAEWRAINhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=aliur_egAEWRAINhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">248.6 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 14:36</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_egAEWhov.png">aliur_egAEWhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=aliur_egAEWhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">257.8 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 14:38</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliur_raincoupling.png">aliur_raincoupling.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=aliur_raincoupling.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">139.7 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 14:37</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/aliuritcz_landoceanhov.png">aliuritcz_landoceanhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=aliuritcz_landoceanhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">172.8 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 17:34</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampna_AEWstats.png">ampna_AEWstats.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampna_AEWstats.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">40.0 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 14:35</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampna_egAEWRAINhov.png">ampna_egAEWRAINhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampna_egAEWRAINhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">340.1 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 14:37</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampna_egAEWhov.png">ampna_egAEWhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampna_egAEWhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">312.1 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 14:39</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampna_raincoupling.png">ampna_raincoupling.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampna_raincoupling.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">179.5 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 14:38</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnadiurnalcycle_LV.png">ampnadiurnalcycle_LV.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampnadiurnalcycle_LV.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">123.5 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 14:09</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top">parameterised diurnal LV</td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnaitcz_landoceanhov.png">ampnaitcz_landoceanhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampnaitcz_landoceanhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">287.9 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 17:34</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnaitcz_landoceanhov_4yrs.png">ampnaitcz_landoceanhov_4yrs.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampnaitcz_landoceanhov_4yrs.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">242.6 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-25 - 17:29</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_AEWstats.png">ampnn_AEWstats.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampnn_AEWstats.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">79.3 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 11:50</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_egAEWRAINhov.png">ampnn_egAEWRAINhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampnn_egAEWRAINhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">516.6 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 11:51</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_egAEWhov.png">ampnn_egAEWhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampnn_egAEWhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">408.0 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 11:51</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnn_raincoupling.png">ampnn_raincoupling.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampnn_raincoupling.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">199.0 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 11:51</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnndiurnalcycle_LV.png">ampnndiurnalcycle_LV.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampnndiurnalcycle_LV.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">130.9 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 14:09</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnnitcz_landoceanhov.png">ampnnitcz_landoceanhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampnnitcz_landoceanhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">293.7 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 17:34</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnr_AEWstats.png">ampnr_AEWstats.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampnr_AEWstats.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">79.7 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 11:52</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnr_egAEWRAINhov.png">ampnr_egAEWRAINhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampnr_egAEWRAINhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">344.1 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 11:52</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnr_egAEWhov.png">ampnr_egAEWhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampnr_egAEWhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">317.1 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 11:56</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/ampnr_raincoupling.png">ampnr_raincoupling.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=ampnr_raincoupling.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">172.1 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:44</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/cloud_ice_jja_4900_12300_mean.png">cloud_ice_jja_4900_12300_mean.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=cloud_ice_jja_4900_12300_mean.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">70.7 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-28 - 11:57</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_MAM_model_trmm_EU.png">diurnal_MAM_model_trmm_EU.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_MAM_model_trmm_EU.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">219.3 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-23 - 16:42</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_MAM_model_trmm_India.png">diurnal_MAM_model_trmm_India.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_MAM_model_trmm_India.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">189.7 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-23 - 16:42</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_MAM_model_trmm_MC.png">diurnal_MAM_model_trmm_MC.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_MAM_model_trmm_MC.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">289.1 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-23 - 16:41</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_MAM_model_trmm_US.png">diurnal_MAM_model_trmm_US.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_MAM_model_trmm_US.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">258.1 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-23 - 16:40</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_MAM_model_trmm_amazon.png">diurnal_MAM_model_trmm_amazon.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_MAM_model_trmm_amazon.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">176.2 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-23 - 16:42</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_MAM_model_trmm_global.png">diurnal_MAM_model_trmm_global.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_MAM_model_trmm_global.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">375.4 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-23 - 16:40</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_MAM_model_trmm_sahel.png">diurnal_MAM_model_trmm_sahel.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_MAM_model_trmm_sahel.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">262.1 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-23 - 17:27</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_ampnapo_trmm_ducmap3.png">diurnal_ampnapo_trmm_ducmap3.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_ampnapo_trmm_ducmap3.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">267.2 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-12-20 - 10:56</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_ampnawn_trmm_ducmap3.png">diurnal_ampnawn_trmm_ducmap3.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_ampnawn_trmm_ducmap3.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">396.9 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-02-20 - 21:14</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_ampnw_mamjja.png">diurnal_ampnw_mamjja.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_ampnw_mamjja.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">300.4 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-02-15 - 08:37</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_n1024_marapr2008_EU.png">diurnal_n1024_marapr2008_EU.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_n1024_marapr2008_EU.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">103.5 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-08 - 14:22</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_n1024_marapr2008_India.png">diurnal_n1024_marapr2008_India.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_n1024_marapr2008_India.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">107.9 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-08 - 14:22</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_n1024_marapr2008_MC.png">diurnal_n1024_marapr2008_MC.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_n1024_marapr2008_MC.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">141.9 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-08 - 14:22</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_n1024_marapr2008_amazon.png">diurnal_n1024_marapr2008_amazon.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_n1024_marapr2008_amazon.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">100.5 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-08 - 14:22</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_n1024_marapr2008_global.png">diurnal_n1024_marapr2008_global.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_n1024_marapr2008_global.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">237.7 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-08 - 14:22</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/diurnal_n1024_marapr2008_sahel.png">diurnal_n1024_marapr2008_sahel.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=diurnal_n1024_marapr2008_sahel.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">140.3 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-08 - 14:22</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/erai_egAEWRAINhov.png">erai_egAEWRAINhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=erai_egAEWRAINhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">379.2 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 14:36</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/erai_egAEWhov.png">erai_egAEWhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=erai_egAEWhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">414.9 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 14:38</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/erai_raincoupling.png">erai_raincoupling.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=erai_raincoupling.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">145.1 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 14:37</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/fraction_precip.png">fraction_precip.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=fraction_precip.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">121.2 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-02-25 - 14:33</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/gpcpitcz_landoceanhov.png">gpcpitcz_landoceanhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=gpcpitcz_landoceanhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">161.4 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 17:34</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="pdf" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/pdf.gif" width="16"><span class="twikiHidden">pdf</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/mjo_ampna_xgxqe.pdf">mjo_ampna_xgxqe.pdf</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=mjo_ampna_xgxqe.pdf;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">4821.0 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-12-12 - 15:32</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="pdf" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/pdf.gif" width="16"><span class="twikiHidden">pdf</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/mjo_ampnn_ampna.pdf">mjo_ampnn_ampna.pdf</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=mjo_ampnn_ampna.pdf;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">4638.1 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-12-12 - 15:29</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="pdf" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/pdf.gif" width="16"><span class="twikiHidden">pdf</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/mjo_xgxqe_xgxqo.pdf">mjo_xgxqe_xgxqo.pdf</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=mjo_xgxqe_xgxqo.pdf;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">4943.5 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-12-12 - 15:36</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="mov" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/mov.gif" width="16"><span class="twikiHidden">mp4</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/n1024_ec_ampnf.mp4">n1024_ec_ampnf.mp4</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=n1024_ec_ampnf.mp4;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">6556.8 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-10-07 - 13:49</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="mov" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/mov.gif" width="16"><span class="twikiHidden">mp4</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/n1024_pc_ampnd.mp4">n1024_pc_ampnd.mp4</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=n1024_pc_ampnd.mp4;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">5653.0 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-10-07 - 13:46</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/olr_precip_power.png">olr_precip_power.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=olr_precip_power.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">35.8 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-02-28 - 16:49</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/olr_precip_power_sm.png">olr_precip_power_sm.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=olr_precip_power_sm.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">23.8 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-04 - 09:53</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/olr_precip_ts_central.png">olr_precip_ts_central.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=olr_precip_ts_central.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">10.2 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-02-28 - 16:59</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/olr_precip_ts_north.png">olr_precip_ts_north.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=olr_precip_ts_north.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">9.3 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-04 - 09:56</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/olr_precip_ts_ocean.png">olr_precip_ts_ocean.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=olr_precip_ts_ocean.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">11.5 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-04 - 09:56</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/trmmdiurnalcycle_LV.png">trmmdiurnalcycle_LV.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=trmmdiurnalcycle_LV.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">110.3 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-14 - 14:10</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/CarolineBain">CarolineBain</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top">TRMM diurnal LV</td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/usa_ampnd_ampnn_ampnw_trmm_1hrmn.png">usa_ampnd_ampnn_ampnw_trmm_1hrmn.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=usa_ampnd_ampnn_ampnw_trmm_1hrmn.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">34.7 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-05 - 10:39</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/usa_ampnd_ampnn_ampnw_trmm_1hrmn_full.png">usa_ampnd_ampnn_ampnw_trmm_1hrmn_full.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=usa_ampnd_ampnn_ampnw_trmm_1hrmn_full.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">120.1 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-03-05 - 10:39</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/usa_orog_3545n.png">usa_orog_3545n.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=usa_orog_3545n.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">5.8 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-26 - 09:44</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="jpg" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/jpg.gif" width="16"><span class="twikiHidden">jpeg</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/waliser.jpeg">waliser.jpeg</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=waliser.jpeg;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">84.1 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-23 - 17:44</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqe_AEWstats.png">xgxqe_AEWstats.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xgxqe_AEWstats.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">75.2 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:44</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqe_egAEWRAINhov.png">xgxqe_egAEWRAINhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xgxqe_egAEWRAINhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">325.5 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:45</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqe_egAEWhov.png">xgxqe_egAEWhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xgxqe_egAEWhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">365.7 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:45</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqe_raincoupling.png">xgxqe_raincoupling.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xgxqe_raincoupling.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">153.9 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:45</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqk_AEWstats.png">xgxqk_AEWstats.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xgxqk_AEWstats.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">76.0 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:46</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqk_egAEWRAINhov.png">xgxqk_egAEWRAINhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xgxqk_egAEWRAINhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">350.8 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:46</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqk_egAEWhov.png">xgxqk_egAEWhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xgxqk_egAEWhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">355.3 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:46</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqk_raincoupling.png">xgxqk_raincoupling.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xgxqk_raincoupling.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">156.9 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:46</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqo_AEWstats.png">xgxqo_AEWstats.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xgxqo_AEWstats.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">75.8 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:46</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqo_egAEWRAINhov.png">xgxqo_egAEWRAINhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xgxqo_egAEWRAINhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">238.8 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:46</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqo_egAEWhov.png">xgxqo_egAEWhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xgxqo_egAEWhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">274.9 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:47</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xgxqo_raincoupling.png">xgxqo_raincoupling.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xgxqo_raincoupling.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">147.4 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:47</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xhqin_AEWstats.png">xhqin_AEWstats.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xhqin_AEWstats.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">74.5 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:47</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xhqin_egAEWRAINhov.png">xhqin_egAEWRAINhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xhqin_egAEWRAINhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">225.0 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:47</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xhqin_egAEWhov.png">xhqin_egAEWhov.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xhqin_egAEWhov.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">258.7 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:47</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol twikiLast" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1 twikiLast" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HiResCLN1024Model/xhqin_raincoupling.png">xhqin_raincoupling.png</a></td>
<td align="left" class="twikiTableCol2 twikiLast" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HiResCLN1024Model?filename=xhqin_raincoupling.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3 twikiLast" valign="top">143.1 K</td>
<td align="left" class="twikiTableCol4 twikiLast" valign="top"><span class="twikiNoBreak">2013-05-01 - 12:50</span></td>
<td align="left" class="twikiTableCol5 twikiLast" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol twikiLast" valign="top"> </td>
</tr>
</tbody>
</table>
</div>
</div>
<!--/twistyPlugin--></div>
<!--//twikiAttachments--><!-- /patternContent-->
