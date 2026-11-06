---
date: 2020-09-23 18:36:07.769000
description: Building on work by Ruth Comer, Caroline Bain, Michael Vellinga on African
  processes. These results seem to be robust at GA3 and GA6 model configurations.
  GloSea5is very good at the AEJ and AEWs, and eastern Atlantic tropical cyclone genesis.
layout: base_hrcm
order: 5
permalink: /hirescl-twiki-archive-unpublished/africa-work/
title: Africa work
---

<p>Building on work by Ruth Comer, Caroline Bain, Michael Vellinga on African processes. These results seem to be robust at GA3 and GA6 model configurations. <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/GloSea5?topicparent=Project/HiResCL.AfricaSensitivity" rel="nofollow" title="GloSea5 (this topic does not yet exist; you can create it)">GloSea5</a></span>is very good at the AEJ and AEWs, and eastern Atlantic tropical cyclone genesis.</p>
<p></p>
<p>We are finding links, both from the UPSCALE ensemble and other versions, of Atlantic tropical cyclone performance. This was indicated by the much better African Easterly Jet structure in <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/GloSea5?topicparent=Project/HiResCL.AfricaSensitivity" rel="nofollow" title="GloSea5 (this topic does not yet exist; you can create it)">GloSea5</a></span>, and its much higher tropical cyclone formation on the eastern side of the Atlantic, than seen in the climate model. We have begun to link this to soil moisture and precipitation over the African monsoon region, linking to the placement of the jet, linking to African Easterly waves, which are a large component of tropical cyclone seeds.</p>
<p></p>
<p>If the jet is well defined to north and south, this enhances the baroclinic instability. Also the instabilities from north and south of the jet have different properties in terms of moisture etc, and hence tend to be precursors for either eastern or western Atlantic TCs.</p>
<p></p>
<p>For GA6 runs from N96 to N1024 (only 3 years for the latter), the AEJ improves with resolution: <br> <img alt="aej_ga6_n96_n1024.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/AfricaSensitivity/aej_ga6_n96_n1024.png"></p>
<p></p>
<p>The frequency of TCs in the Atlantic gradually improves (note N1024 is 3 years including 2005 which was very big in reality): <br> <img alt="barchart_n96_n1024_ga6.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/AfricaSensitivity/barchart_n96_n1024_ga6.png"></p>
<p></p>
<p>The track density in the Atlantic is not quite so obvious, though N1024 has more genesis in the east (here I've used the full vorticity TRACK, not the warm core): <br> <img alt="track_density_na_n96_n1024.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/AfricaSensitivity/track_density_na_n96_n1024.png"></p>
<p></p>
<p>This goes together with a gradual improvement in African rainfall in JJA: <br> <img alt="precip_resolution.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/AfricaSensitivity/precip_resolution.png"></p>
<p></p>
<p>and is also seen in the UPSCALE ensemble GA3 runs: <br> <img alt="precip_resolution_upscale.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/AfricaSensitivity/precip_resolution_upscale.png"></p>
<p></p>
<p>The position of the AEJ seems to be strongly related to the soil moisture (and hence likely to the rainfall and how far north the monsoon moves). An ensemble of experiments done at previous model versions by Ruth, with analysis by Ruth and Caroline, in which the soil moisture was constrained in June shown (see <a href="http://www-hc/~hadru/GLACE/WAM_summary.html" target="_top">http://www-hc/~hadru/GLACE/WAM_summary.html</a>), have these AEJ spread over the first 8 members each - where S is drier soil and W is wetter. In general the W members have an improved AEJ position. Unfortunately the diagnostics only cover the African region, so I can't do TC tracking.</p>
<p></p>
<p><img alt="aej_8members.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/AfricaSensitivity/aej_8members.png"></p>
<p></p>
<p></p>
<h3><a name="Relation to AEJ"></a> Relation to AEJ</h3>
<p>Consider just N96 GA3, and look at Gill's run which excluded the Light Rain Package - see <a href="http://www-hc/~hadgi/CSRP2_GMM.html" target="_top">http://www-hc/~hadgi/CSRP2_GMM.html</a>. Gill said: "We do tend to have our AEJ too far south, though the strength isn't too bad (it can vary between configurations though). For comparison, see attached plot of <span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/HadGEM2?topicparent=Project/HiResCL.AfricaSensitivity" rel="nofollow" title="HadGEM2 (this topic does not yet exist; you can create it)">HadGEM2</a></span>versus 3 other EMBRACE models and ERA-I and MERRA. We are no worse than any of them, even EC-Earth which is based on the same model as ERA-I. There's also a noticeable difference between the reanalyses.</p>
<p></p>
<p>We do have a "defined" AEJ but it is just too spread out and the centre too far south so that the min in the wind gradient is at around 10S. To be fair, ERA and MERRA have something of this broad structure at least over the sea but the southern part is much weaker so it looks more focussed.</p>
<p></p>
<p>The location of the AEJ is related to the Saharan heat low also being centred too far south. I'm currently comparing our model with ARPEGE (where everything's too far north) - we have quite different radiative heating over the Sahara and over the Atlantic (in fact, NH in general) and different temperature profiles (theirs is much warmer) which is probably related to different aerosol properties/concentrations (esp dust). The val note suggests that we overdo our incoming SW and underdo our incoming LW at the surface at least over the Sahara suggesting perhaps a lack of absorbing aerosol. ARPEGE probably has too much."</p>
<p></p>
<p>The AEJ is improved in the GA3 run without the LRP (akmkk is this run, akkvg is default GA3, and xhqin is UPSCALE GA3 N96 and xgxqe is UPSCALE N512 GA3): <br> <img alt="aej_n96_ga3_noLRP.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/AfricaSensitivity/aej_n96_ga3_noLRP.png"> </p>
<p></p>
<p>and the TC frequency in the Atlantic is slightly improved <br> <img alt="barchart_n96_ga3_noLRP.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/AfricaSensitivity/barchart_n96_ga3_noLRP.png"></p>
<p></p>
<p>along with the AEW frequency <br> <img alt="aew_n96_ga3_noLRP.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/AfricaSensitivity/aew_n96_ga3_noLRP.png"></p>
<p></p>
<p>and then the track density in the Atlantic <br> <img alt="track_den_n96_ga3.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/AfricaSensitivity/track_den_n96_ga3.png"></p>
<p></p>
<p>The other element of this process may be the moisture contained in the AEWs, so both the frequency and the fact that the surface is more moist may help in generating TC vorticity structure. This would be linked to the increased precip found in the run without the LRP: <br> <img alt="0821precipfourupjja_akmkk_akkvg_lrp.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/AfricaSensitivity/0821precipfourupjja_akmkk_akkvg_lrp.png"></p>
<p></p>
<p>And these are the full length tracks plotted for the period 1982-2008 from each of the N96 GA3 runs with and without the LRP. <br> <img alt="akkvg_na_tracks.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/AfricaSensitivity/akkvg_na_tracks.png"> <br> <img alt="akmkk_na_tracks.png" src="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/AfricaSensitivity/akmkk_na_tracks.png"> </p>
<p></p>
<p></p>
<p>-- <a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a> - 2014-03-20</p>
<!-- /patternTopic-->
<div class="twikiContentFooter"></div>
<div class="twikiAttachments">
<div class="twistyPlugin twikiMakeVisibleInline"><span class="twistyRememberSetting twistyTrigger twikiUnvisited twistyInited0" id="topicattachmentslistshow"><a href="#"><img alt="" border="0" src="/twiki/pub/TWiki/TWikiDocGraphics/toggleopen.gif"><span class="twikiLinkLabel twikiUnvisited">Attachments</span></a> </span> <span class="twistyRememberSetting twistyTrigger twikiUnvisited twistyHidden twistyInited0" id="topicattachmentslisthide"><a href="#"><img alt="" border="0" src="/twiki/pub/TWiki/TWikiDocGraphics/toggleclose.gif"><span class="twikiLinkLabel twikiUnvisited">Attachments</span></a> </span></div>
<!--/twistyPlugin twikiMakeVisibleInline-->
<div class="twistyPlugin">
<div class="twistyRememberSetting twistyContent twikiMakeHidden twistyInited0" id="topicattachmentslisttoggle">
<table border="1" cellpadding="0" cellspacing="0" class="twikiTable" id="twikiAttachmentsTable" rules="rows" summary="Topic attachments"><caption>Topic attachments</caption>
<tbody>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0"><th class="twikiTableCol0 twikiFirstCol" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/AfricaSensitivity?sortcol=0;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">I</span></a></th><th class="twikiTableCol1" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/AfricaSensitivity?sortcol=1;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Attachment</span></a></th><th class="twikiTableCol2" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/AfricaSensitivity?sortcol=2;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Action</span></a></th><th class="twikiTableCol3" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/AfricaSensitivity?sortcol=3;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Size</span></a></th><th class="twikiTableCol4" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/AfricaSensitivity?sortcol=4;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Date</span></a></th><th class="twikiTableCol5" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/AfricaSensitivity?sortcol=5;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Who</span></a></th><th class="twikiTableCol6 twikiLastCol" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/AfricaSensitivity?sortcol=6;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Comment</span></a></th></tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/AfricaSensitivity/0821precipfourupjja_akmkk_akkvg_lrp.png">0821precipfourupjja_akmkk_akkvg_lrp.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/AfricaSensitivity?filename=0821precipfourupjja_akmkk_akkvg_lrp.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">273.5 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2014-03-24 - 10:28</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/AfricaSensitivity/aej_8members.png">aej_8members.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/AfricaSensitivity?filename=aej_8members.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">206.4 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2014-03-20 - 16:06</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/AfricaSensitivity/aej_ga6_n96_n1024.png">aej_ga6_n96_n1024.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/AfricaSensitivity?filename=aej_ga6_n96_n1024.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">143.7 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2014-03-20 - 16:09</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/AfricaSensitivity/aej_n96_ga3_noLRP.png">aej_n96_ga3_noLRP.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/AfricaSensitivity?filename=aej_n96_ga3_noLRP.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">136.0 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2014-03-24 - 10:03</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/AfricaSensitivity/aew_n96_ga3_noLRP.png">aew_n96_ga3_noLRP.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/AfricaSensitivity?filename=aew_n96_ga3_noLRP.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">93.4 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2014-03-24 - 10:04</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/AfricaSensitivity/akkvg_na_tracks.png">akkvg_na_tracks.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/AfricaSensitivity?filename=akkvg_na_tracks.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">480.2 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2014-03-24 - 10:31</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/AfricaSensitivity/akmkk_na_tracks.png">akmkk_na_tracks.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/AfricaSensitivity?filename=akmkk_na_tracks.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">514.2 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2014-03-24 - 10:31</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/AfricaSensitivity/barchart_n96_ga3_noLRP.png">barchart_n96_ga3_noLRP.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/AfricaSensitivity?filename=barchart_n96_ga3_noLRP.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">41.4 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2014-03-24 - 10:04</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/AfricaSensitivity/barchart_n96_n1024_ga6.png">barchart_n96_n1024_ga6.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/AfricaSensitivity?filename=barchart_n96_n1024_ga6.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">54.4 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2014-03-20 - 16:18</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/AfricaSensitivity/precip_resolution.png">precip_resolution.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/AfricaSensitivity?filename=precip_resolution.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">186.0 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2014-03-21 - 08:38</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/AfricaSensitivity/precip_resolution_upscale.png">precip_resolution_upscale.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/AfricaSensitivity?filename=precip_resolution_upscale.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">112.5 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2014-03-25 - 15:53</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/AfricaSensitivity/track_den_n96_ga3.png">track_den_n96_ga3.png</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/AfricaSensitivity?filename=track_den_n96_ga3.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">324.5 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2014-03-24 - 10:04</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol twikiLast" valign="top"><img align="top" alt="png" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/png.gif" width="16"><span class="twikiHidden">png</span></td>
<td align="left" class="twikiTableCol1 twikiLast" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/AfricaSensitivity/track_density_na_n96_n1024.png">track_density_na_n96_n1024.png</a></td>
<td align="left" class="twikiTableCol2 twikiLast" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/AfricaSensitivity?filename=track_density_na_n96_n1024.png;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3 twikiLast" valign="top">345.3 K</td>
<td align="left" class="twikiTableCol4 twikiLast" valign="top"><span class="twikiNoBreak">2014-03-20 - 16:19</span></td>
<td align="left" class="twikiTableCol5 twikiLast" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol twikiLast" valign="top"> </td>
</tr>
</tbody>
</table>
</div>
</div>
<!--/twistyPlugin--></div>
<!--//twikiAttachments--><!-- /patternContent-->
