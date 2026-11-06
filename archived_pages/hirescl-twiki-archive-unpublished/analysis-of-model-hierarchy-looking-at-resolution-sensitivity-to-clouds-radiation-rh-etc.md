---
date: 2020-09-28 16:23:29.704000
description: 'Resolution sensitivity and climate modelling

  This work will look at aspects of the model hierarchy where model resolution seems
  to play some role, and link this through to potential consequences for climate modelling
  for present day and future.'
layout: base_hrcm
order: 17
permalink: /hirescl-twiki-archive-unpublished/analysis-of-model-hierarchy-looking-at-resolution-sensitivity-to-clouds-radiation-rh-etc/
title: Analysis of model hierarchy looking at resolution sensitivity to clouds, radiation,
  RH etc
---

<h3>Resolution sensitivity and climate modelling</h3>
<p>This work will look at aspects of the model hierarchy where model resolution seems to play some role, and link this through to potential consequences for climate modelling for present day and future.</p>
<p></p>
<p><a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/WebHome/HadGEM3_runs_Oct_2014.xlsx" target="_top">This table</a>shows all our various runs, at GA3 and GA4, at different resolutions, together with any climate change-style runs.</p>
<p></p>
<!-- The <a href="http://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/HierarchyCloudsRadiation/Table_of_runs_Nov12_reinhard.xlsx" target="_top">Table</a> shows all our various runs, at GA3 and GA4, at different resolutions, together with any climate change-style runs. -->
<p></p>
<p>Useful links: <a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/CAPTIVATE/HadGEM3Evolution" target="_top">http://collab.metoffice.gov.uk/twiki/bin/view/Project/CAPTIVATE/HadGEM3Evolution</a> - GA3/4 model evolution, including those used for the CLIVAR Hurricane working group: <a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/CAPTIVATE/HadGEM3akztd" target="_top">N96 akztd</a>, <a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/CAPTIVATE/HadGEM3akztf" target="_top">akztf N96 +2K</a>, <a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/CAPTIVATE/HadGEM3akzti" target="_top">akzti N96 2xCO2</a>, <a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/CAPTIVATE/HadGEM3xgdfa" target="_top">N320 xgdfa</a></p>
<p></p>
<p><a href="http://collab.metoffice.gov.uk/trac/GA/wiki/GAJobs" target="_top">http://collab.metoffice.gov.uk/trac/GA/wiki/GAJobs</a>- GA3/4 final jobs</p>
<p></p>
<p><a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/HiResCL/HiResCLGA4CoupledModelSuite" target="_top">http://collab.metoffice.gov.uk/twiki/bin/view/Project/HiResCL/HiResCLGA4CoupledModelSuite</a>- some coupled and atmosphere-only jobs</p>
<p></p>
<p><a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/CAPTIVATE/CAPTIVATETimeSlice" target="_top">http://collab.metoffice.gov.uk/twiki/bin/view/Project/CAPTIVATE/CAPTIVATETimeSlice</a>- Description of the Timeslice future climate setup</p>
<p></p>
<p><a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/HiResCL/ModelEvolutionUPSCALE" target="_top">http://collab.metoffice.gov.uk/twiki/bin/view/Project/HiResCL/ModelEvolutionUPSCALE</a> - UPSCALE runs, with the standard STASH setup shown at the bottom of <a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/HiResCL/UPSCALEWorkingWithJASMIN" target="_top">http://collab.metoffice.gov.uk/twiki/bin/view/Project/HiResCL/UPSCALEWorkingWithJASMIN</a></p>
<p></p>
<p><a href="http://collab.metoffice.gov.uk/twiki/bin/view/Project/HiResCL/HiResCLN1024Model" target="_top">http://collab.metoffice.gov.uk/twiki/bin/view/Project/HiResCL/HiResCLN1024Model</a>- N1024 run information</p>
<p></p>
<h3><a name="Validation notes"></a> Validation notes</h3>
<h4><a name="GA3"></a> GA3</h4>
<p></p>
<p>3xN512 vs 3xN216: (Internal) <a href="http://www-hc/~hadvg/valnote/3n512_v_3n216/browser.html" target="_top">http://www-hc/~hadvg/valnote/3n512_v_3n216/browser.html</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/3n512_v_3n216/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/3n512_v_3n216/browser.html</a></p>
<p></p>
<p>5xN512 vs 4xN96: (Internal) <a href="http://www-hc/~hadvg/valnote/5n512_v_4xn96/browser.html" target="_top">http://www-hc/~hadvg/valnote/5n512_v_4xn96/browser.html</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/5n512_v_4xn96/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/5n512_v_4xn96/browser.html</a></p>
<p></p>
<p>3xN216 vs 4xN96: (Internal) <a href="http://www-hc/~hadvg/valnote/3n216_v_4xn96/browser.html" target="_top">http://www-hc/~hadvg/valnote/3n216_v_4xn96/browser.html</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/3n216_v_4xn96/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/3n216_v_4xn96/browser.html</a></p>
<p></p>
<p>3xN512 Timeslice vs 5xN512 Control: (Internal) <a href="http://www-hc/~hadvg/valnote/fc512_v_5n512/browser.html" target="_top">http://www-hc/~hadvg/valnote/fc512_v_5n512/browser.html</a></p>
<p></p>
<p>1xN216 Timeslice vs 3xN216 Control: (Internal) <a href="http://www-hc/~hadvg/valnote/xgyie_v_3n216/browser.html" target="_top">http://www-hc/~hadvg/valnote/xgyie_v_3n216/browser.html</a></p>
<p></p>
<p>1xN96 Timeslice vs 4xN96 Control: (Internal) <a href="http://www-hc/~hadvg/valnote/xgyip_v_4xn96/browser.html" target="_top">http://www-hc/~hadvg/valnote/xgyip_v_4xn96/browser.html</a></p>
<p></p>
<p><span class="twikiNewLink"><a href="{{ site.baseurl }}/twiki/bin/edit/Project/HiResCL/HadGEM2?topicparent=Project/HiResCL.HierarchyCloudsRadiation" rel="nofollow" title="HadGEM2 (this topic does not yet exist; you can create it)">HadGEM2</a></span> -ES 2100-2114 (RCP8.5) vs 1976-2005 Impact of climate change (and same delta SST as used in timeslice runs): (Internal) <a href="http://www-hc/~hadvg/valnote/ajnjp_v_ajhoh/browser.html" target="_top">http://www-hc/~hadvg/valnote/ajnjp_v_ajhoh/browser.html</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ajnjp_v_ajhoh/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ajnjp_v_ajhoh/browser.html</a></p>
<p></p>
<p>1xN96 CO2 (not SST) vs 4xN96 Control: (Internal) <a href="http://www-hc/~hadvg/valnote/xhqip_v_4xn96/browser.html" target="_top">http://www-hc/~hadvg/valnote/xhqip_v_4xn96/browser.html</a></p>
<p></p>
<p>Radiation VN output for individual UPSCALE runs: <a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/UpscaleRadiationNotes">UpscaleRadiationNotes</a></p>
<p></p>
<h4><a name="GA4"></a> GA4</h4>
<p></p>
<p>N1024 (2008) explicit vs N1024 (2008) GA4: (internal) <a href="http://www-hc/~hadvg/valnote/ampnn_v_ampna/browser.html" target="_top">http://www-hc/~hadvg/valnote/ampnn_v_ampna/browser.html</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnn_v_ampna/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnn_v_ampna/browser.html</a></p>
<p></p>
<p>N1024 (2008) shallow param vs N1024 (2008) GA4: (internal) <a href="http://www-hc/~hadvg/valnote/ampnw_v_ampna/browser.html" target="_top">http://www-hc/~hadvg/valnote/ampnw_v_ampna/browser.html</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnw_v_ampna/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnw_v_ampna/browser.html</a></p>
<p></p>
<p>N1024 (2008) GA4 vs N768 (2003-2010) GA4: (internal) <a href="http://www-hc/~hadvg/valnote/ampna_v_alxgq/browser.html" target="_top">http://www-hc/~hadvg/valnote/ampna_v_alxgq/browser.html</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampna_v_alxgq/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampna_v_alxgq/browser.html</a></p>
<p></p>
<p>N1024 (2008-11) GA4 vs N512 (1985-2010) GA4: (internal) <a href="http://www-hc/~hadvg/valnote/ampnp_v_xgxpr/browser.html" target="_top">http://www-hc/~hadvg/valnote/ampnp_v_xgxpr/browser.html</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnp_v_xgxpr/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/ampnp_v_xgxpr/browser.html</a></p>
<p></p>
<p>N768 (2003-2010) vs N512 (1985-1999): <a href="http://www-hc/~hadvg/valnote/alxgq_v_xgxqr/browser.html" target="_top">http://www-hc/~hadvg/valnote/alxgq_v_xgxqr/browser.html</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/alxgq_v_xgxqr/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/alxgq_v_xgxqr/browser.html</a></p>
<p></p>
<p>N512 (1985-2010) vs N216 (1982-2007): <a href="http://www-hc/~hadvg/valnote/xgxpr_v_xhcea/browser.html" target="_top">http://www-hc/~hadvg/valnote/xgxpr_v_xhcea/browser.html</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/xgxpr_v_xhcea/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/xgxpr_v_xhcea/browser.html</a></p>
<p></p>
<p>N216 (1982-2007) vs N96 (1982-2006): <a href="http://www-hc/~hadvg/valnote/xhcea_v_aliur/browser.html" target="_top">http://www-hc/~hadvg/valnote/xhcea_v_aliur/browser.html</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/xhcea_v_aliur/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/xhcea_v_aliur/browser.html</a></p>
<p></p>
<h4><a name="GA5 + bug fix"></a> GA5 + bug fix</h4>
<p>N1024e (anbbp, 2008-12) vs N512e (anbbd, 1989-2009): <a href="http://www-hc/~hadvg/valnote/anbbp_v_anbbd/browser.html" target="_top">http://www-hc/~hadvg/valnote/anbbp_v_anbbd/browser.html</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/anbbp_v_anbbd/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/anbbp_v_anbbd/browser.html</a></p>
<p></p>
<p>N512e (anbbd) vs N96e (angma): <a href="http://www-hc/~hadvg/valnote/anbbp_v_anbbd/browser.html" target="_top">http://www-hc/~hadvg/valnote/anbbp_v_anbbd/browser.html</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/anbbd_v_angma/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/anbbd_v_angma/browser.html</a></p>
<p></p>
<h4><a name="GA6ish"></a> GA6ish</h4>
<p>N512e vn N96e (#95.12): <a href="http://www-hc/~hadvg/valnote/anbbj_v_anhpq/browser.html" target="_top">http://www-hc/~hadvg/valnote/anbbj_v_anhpq/browser.html</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/anbbj_v_anhpq/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/anbbj_v_anhpq/browser.html</a></p>
<p></p>
<p>N96e (#95.12) vs 4xN96 (GA3 UPSCALE): <a href="http://www-hc/~hadvg/valnote/anhpq_v_4xn96/browser.html" target="_top">http://www-hc/~hadvg/valnote/anhpq_v_4xn96/browser.html</a> <br> (External) <a href="http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/anhpq_v_4xn96/browser.html" target="_top">http://collab.metoffice.gov.uk/twiki/bin/viewfile/Static/development/valid/anhpq_v_4xn96/browser.html</a></p>
<p></p>
<p>-- <a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a> - 2012-11-30</p>
<!-- /patternTopic-->
<div class="twikiContentFooter"></div>
<div class="twikiAttachments">
<div class="twistyPlugin twikiMakeVisibleInline"><span class="twistyRememberSetting twistyTrigger twikiUnvisited twistyHidden twistyInited1" id="topicattachmentslistshow"><a href="#"><img alt="" border="0" src="/twiki/pub/TWiki/TWikiDocGraphics/toggleopen.gif"><span class="twikiLinkLabel twikiUnvisited">Attachments</span></a> </span> <span class="twistyRememberSetting twistyTrigger twikiUnvisited twistyInited1" id="topicattachmentslisthide"><a href="#"><img alt="" border="0" src="/twiki/pub/TWiki/TWikiDocGraphics/toggleclose.gif"><span class="twikiLinkLabel twikiUnvisited">Attachments</span></a> </span></div>
<!--/twistyPlugin twikiMakeVisibleInline-->
<div class="twistyPlugin">
<div class="twistyRememberSetting twistyContent twistyInited1" id="topicattachmentslisttoggle">
<table border="1" cellpadding="0" cellspacing="0" class="twikiTable" id="twikiAttachmentsTable" rules="rows" summary="Topic attachments"><caption>Topic attachments</caption>
<tbody>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0"><th class="twikiTableCol0 twikiFirstCol" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HierarchyCloudsRadiation?sortcol=0;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">I</span></a></th><th class="twikiTableCol1" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HierarchyCloudsRadiation?sortcol=1;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Attachment</span></a></th><th class="twikiTableCol2" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HierarchyCloudsRadiation?sortcol=2;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Action</span></a></th><th class="twikiTableCol3" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HierarchyCloudsRadiation?sortcol=3;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Size</span></a></th><th class="twikiTableCol4" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HierarchyCloudsRadiation?sortcol=4;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Date</span></a></th><th class="twikiTableCol5" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HierarchyCloudsRadiation?sortcol=5;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Who</span></a></th><th class="twikiTableCol6 twikiLastCol" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HierarchyCloudsRadiation?sortcol=6;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Comment</span></a></th></tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="else" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/else.gif" width="16"><span class="twikiHidden">xlsx</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HierarchyCloudsRadiation/Table_of_runs_Nov12.xlsx">Table_of_runs_Nov12.xlsx</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HierarchyCloudsRadiation?filename=Table_of_runs_Nov12.xlsx;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">14.5 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2012-11-30 - 09:59</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top"> </td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol twikiLast" valign="top"><img align="top" alt="else" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/else.gif" width="16"><span class="twikiHidden">xlsx</span></td>
<td align="left" class="twikiTableCol1 twikiLast" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/HierarchyCloudsRadiation/Table_of_runs_Nov12_reinhard.xlsx">Table_of_runs_Nov12_reinhard.xlsx</a></td>
<td align="left" class="twikiTableCol2 twikiLast" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HierarchyCloudsRadiation?filename=Table_of_runs_Nov12_reinhard.xlsx;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3 twikiLast" valign="top">14.8 K</td>
<td align="left" class="twikiTableCol4 twikiLast" valign="top"><span class="twikiNoBreak">2012-12-06 - 17:01</span></td>
<td align="left" class="twikiTableCol5 twikiLast" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol twikiLast" valign="top"> </td>
</tr>
</tbody>
</table>
</div>
</div>
<!--/twistyPlugin--></div>
<!--//twikiAttachments--><!-- /patternContent-->
<p><a name="topic-actions"></a></p>
<div class="patternTopicActions" style="">
<div class="patternTopicAction"><span class="patternActionButtons"><span><a accesskey="e" href="https://collab.metoffice.gov.uk/twiki/bin/edit/Project/HiResCL/HierarchyCloudsRadiation?t=1601310084" rel="nofollow" title="Edit this topic text"><span class="twikiAccessKey">E</span>dit</a></span><span class="twikiSeparator"> | </span><span><a accesskey="a" href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/HierarchyCloudsRadiation" rel="nofollow" title="Attach an image or document to this topic"><span class="twikiAccessKey">A</span>ttach</a></span><span class="twikiSeparator"> | </span><span><a accesskey="p" href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HierarchyCloudsRadiation?cover=print" rel="nofollow" title="Printable version of this topic"><span class="twikiAccessKey">P</span>rint version</a></span><span class="twikiSeparator"> | </span><span><span><a accesskey="h" href="{{ site.baseurl }}/twiki/bin/rdiff/Project/HiResCL/HierarchyCloudsRadiation?type=history" rel="nofollow" title="View total topic history"><span class="twikiAccessKey">H</span>istory</a></span>: r23 <a href="{{ site.baseurl }}/twiki/bin/rdiff/Project/HiResCL/HierarchyCloudsRadiation?rev1=23;rev2=22" rel="nofollow">&lt;</a> <a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HierarchyCloudsRadiation?rev=22" rel="nofollow">r22</a> <a href="{{ site.baseurl }}/twiki/bin/rdiff/Project/HiResCL/HierarchyCloudsRadiation?rev1=22;rev2=21" rel="nofollow">&lt;</a> <a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HierarchyCloudsRadiation?rev=21" rel="nofollow">r21</a> <a href="{{ site.baseurl }}/twiki/bin/rdiff/Project/HiResCL/HierarchyCloudsRadiation?rev1=21;rev2=20" rel="nofollow">&lt;</a> <a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HierarchyCloudsRadiation?rev=20" rel="nofollow">r20</a> <a href="{{ site.baseurl }}/twiki/bin/rdiff/Project/HiResCL/HierarchyCloudsRadiation?rev1=20;rev2=19" rel="nofollow">&lt;</a> <a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HierarchyCloudsRadiation?rev=19" rel="nofollow">r19</a></span><span class="twikiSeparator"> | </span><span><a accesskey="b" href="{{ site.baseurl }}/twiki/bin/oops/Project/HiResCL/HierarchyCloudsRadiation?template=backlinksweb" rel="nofollow" title="Search the Project/HiResCL Web for topics that link to here"><span class="twikiAccessKey">B</span>acklinks</a></span><span class="twikiSeparator"> | </span><span><a accesskey="r" href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/HierarchyCloudsRadiation?raw=on" rel="nofollow" title="View raw text without formatting"><span class="twikiAccessKey">R</span>aw View</a></span><span class="twikiSeparator"> | </span><span><a accesskey="w" href="https://collab.metoffice.gov.uk/twiki/bin/edit/Project/HiResCL/HierarchyCloudsRadiation?t=1601310084;nowysiwyg=1" rel="nofollow" title="Raw Edit this topic text">Ra<span class="twikiAccessKey">w</span> edit</a></span><span class="twikiSeparator"> | </span><span><a accesskey="m" href="{{ site.baseurl }}/twiki/bin/oops/Project/HiResCL/HierarchyCloudsRadiation?template=oopsmore&amp;param1=23&amp;param2=23" rel="nofollow" title="Delete or rename this topic; set parent topic; view and compare revisions"><span class="twikiAccessKey">M</span>ore topic actions</a></span></span></div>
<!--/patternTopicAction--></div>
<!--/patternTopicActions-->
<div class="patternInfo twikiGrayText">
<div class="patternRevInfo">Topic revision: r23 - 2015-09-29 - 14:08:24 - <a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MalcolmRoberts">MalcolmRoberts</a></div>
<!-- /patternRevInfo-->
<div class="patternMoved"></div>
<!-- /patternMoved--></div>
<!-- /patternInfo-->
<p></p>
<!-- /patternMainContents-->
<p></p>
<!-- /patternMain-->
<div id="patternLeftBar">
<div id="patternClearHeaderLeft"></div>
<div id="patternLeftBarContents">
<div class="patternWebIndicator"></div>
</div>
</div>
