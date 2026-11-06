---
date: 2020-09-28 16:07:47.303000
description: The FEBBRAIO campaign ran two 100 year N512-ORCA025 GC2 simulations on
  Archer (xkjej and xklrb in parallel to an earlier simulation answg) of the same
  length that was run on MONSooNusing the HCCP allocation of computing resource.
layout: base_hrcm
order: 11
permalink: /hirescl-twiki-archive-unpublished/febbraio/
title: FEBBRAIO
---

<p>The FEBBRAIO campaign ran two 100 year N512-ORCA025 GC2 simulations on Archer (<a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioRunXKJEJ">xkjej</a> and <a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioRunXKLRB">xklrb</a> in parallel to an earlier simulation <a href="http://collab.metoffice.gov.uk/trac/GA/wiki/GAJobs/answg" target="_top">answg</a>) of the same length that was run on <a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/MONSooN">MONSooN</a>using the HCCP allocation of computing resource.</p>
<p></p>
<p>The operation of the data management aspects of the FEBBRAIO project is documented in the attached draft report, which also contains references to the scripts and tools used to manage the FEBBRAIO data flow.</p>
<p></p>
<p>A full description of the data set is available in the reference document linked below.</p>
<p></p>
<h2><a name="Documents"></a> Documents</h2>
<p></p>
<table border="1" cellpadding="0" cellspacing="0" class="twikiTable" id="table1" rules="rows">
<tbody>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0"><th align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioDocumentation?sortcol=0;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#ffffff" style="">Link</span></a></th><th align="center" class="twikiTableCol1 twikiLastCol" valign="top"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioDocumentation?sortcol=1;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#ffffff" style="">Description</span></a></th></tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/FebbraioDocumentation/febbraio_data_protocols.pdf" target="_top">febbraio_data_protocols.pdf</a></td>
<td class="twikiTableCol1 twikiLastCol" valign="top">First draft of febbraio data protocols report/write up</td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol twikiLast" valign="top"><a href="https://collab.metoffice.gov.uk/twiki/pub/Project/HiResCL/FebbraioDocumentation/febbraio_reference.pdf" target="_top">febbraio_reference.pdf</a></td>
<td class="twikiTableCol1 twikiLastCol twikiLast" valign="top">Reference document for the febbraio data set</td>
</tr>
</tbody>
</table>
<h2><a name="Data locations"></a> Data locations</h2>
<p></p>
<p>JASMIN: /group_workspaces/jasmin2/hrcm/febbraio/ xkjej and xklrb</p>
<p></p>
<p>MASS: moose:/crum/xkjej , moose:/crum/xklrb, moose:/crum/answg</p>
<h2><a name="Known data issues"></a> Known data issues</h2>
<h3><a name="Diurnal cycle diagnostics (TMPMN"></a> Diurnal cycle diagnostics (TMPMN06 time profile)</h3>
<p></p>
<p>The TMPMN06 time profile was incorrectly altered when climate meaning was removed leading to the output of diagnostics every 30 months rather than 30 days. This was corrected at December 2031 in xkjej and May 2023 in xklrb.</p>
<p></p>
<h3><a name="TDAYMAX and TDAYMIN"></a> TDAYMAX and TDAYMIN</h3>
<p></p>
<p>Two diagnostics, 10m wind speed (stash 3227) and 1.5m temperature (stash 3236) are output as daily maximum and minimum values, but in standard model development configurations these diagnostics are only output for the first 30 years of a run. The "expiration" of these time profiles flagged up an issue in the checking scripts used to monitor data conversion on Archer. A subsequent change to the model reintroduced these fields but xkjej has a gap between 2037 and 2044. The fix was applied to xklrb before reaching 2037 leaving a complete time series. answg only has these diagnostics up to 2008.</p>
<p></p>
<h3><a name="T3HDMRV time profile"></a> T3HDMRV time profile</h3>
<p></p>
<p>The following diagnostics used the T3HDMRV time profile which in xkjej and xklrb had a fault introduced when the climate meaning system was replaced with STASH meaning.</p>
<p></p>
<p>The diagnostics below were output as a mean, sampled every 3 hours, over the final day of the month rather than every day of the month. The data from answg does not have this fault.</p>
<p></p>
<table border="1" cellpadding="0" cellspacing="0" class="twikiTable" id="table2" rules="rows">
<tbody>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0"><th class="twikiTableCol0 twikiFirstCol" valign="top"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioDocumentation?sortcol=0;table=2;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#ffffff" style="">Stash code</span></a></th><th class="twikiTableCol1 twikiLastCol" valign="top"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioDocumentation?sortcol=1;table=2;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#ffffff" style="">Diagnostic name</span></a></th></tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top">8245</td>
<td class="twikiTableCol1 twikiLastCol" valign="top">INLANDBASINFLOW ATM GRID (KG/M2/S )</td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol" valign="top">26001</td>
<td class="twikiTableCol1 twikiLastCol" valign="top">RIVER WATER STORAGE (KG)</td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top">26002</td>
<td class="twikiTableCol1 twikiLastCol" valign="top">GRIDBOX OUTFLOW (KG/S)</td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol" valign="top">26003</td>
<td class="twikiTableCol1 twikiLastCol" valign="top">GRIDBOX INFLOW (KG/S)</td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top">26004</td>
<td class="twikiTableCol1 twikiLastCol" valign="top">RIVER OUTFLOW (KG/M2/S)</td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol twikiLast" valign="top">26006</td>
<td class="twikiTableCol1 twikiLastCol twikiLast" valign="top">INLANDBASINFLOW TRIP GRID (KG/S)</td>
</tr>
</tbody>
</table>
<p></p>
<h3><a name="Diaptr files"></a> Diaptr files</h3>
<p></p>
<p>For some reason all diaptr files output by the ocean have not been correctly rebuilt with lines apparently matching the zonal domain decomposition through most fields. These data should be considered corrupt and recomputed where possible from the monthly mean full fields where possible. If there is an urgent need for these fields please contact me and we consider whether an attempt to rescue some of the data is suitable. Note that in later versions of NEMO these files are not produced as the non-linear free surface, introduced for GC3, has made the diaptr routines obsolete.</p>
<p></p>
<p>-- <a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MatthewMizielinski">MatthewMizielinski</a> - 2015-03-17</p>
<!-- /patternTopic-->
<div class="twikiContentFooter"></div>
<div class="twikiAttachments">
<div class="twistyPlugin twikiMakeVisibleInline"><span class="twistyRememberSetting twistyTrigger twikiUnvisited twistyHidden twistyInited1" id="topicattachmentslistshow"><a href="#"><img alt="" border="0" src="/twiki/pub/TWiki/TWikiDocGraphics/toggleopen.gif"><span class="twikiLinkLabel twikiUnvisited">Attachments</span></a> </span> <span class="twistyRememberSetting twistyTrigger twikiUnvisited twistyInited1" id="topicattachmentslisthide"><a href="#"><img alt="" border="0" src="/twiki/pub/TWiki/TWikiDocGraphics/toggleclose.gif"><span class="twikiLinkLabel twikiUnvisited">Attachments</span></a> </span></div>
<!--/twistyPlugin twikiMakeVisibleInline-->
<div class="twistyPlugin">
<div class="twistyRememberSetting twistyContent twistyInited1" id="topicattachmentslisttoggle">
<table border="1" cellpadding="0" cellspacing="0" class="twikiTable" id="twikiAttachmentsTable" rules="rows" summary="Topic attachments"><caption>Topic attachments</caption>
<tbody>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0"><th class="twikiTableCol0 twikiFirstCol" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioDocumentation?sortcol=0;table=3;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">I</span></a></th><th class="twikiTableCol1" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioDocumentation?sortcol=1;table=3;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Attachment</span></a></th><th class="twikiTableCol2" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioDocumentation?sortcol=2;table=3;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Action</span></a></th><th class="twikiTableCol3" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioDocumentation?sortcol=3;table=3;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Size</span></a></th><th class="twikiTableCol4" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioDocumentation?sortcol=4;table=3;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Date</span></a></th><th class="twikiTableCol5" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioDocumentation?sortcol=5;table=3;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Who</span></a></th><th class="twikiTableCol6 twikiLastCol" valign="middle"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioDocumentation?sortcol=6;table=3;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#0066cc" style="">Comment</span></a></th></tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><img align="top" alt="pdf" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/pdf.gif" width="16"><span class="twikiHidden">pdf</span></td>
<td align="left" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/FebbraioDocumentation/febbraio_data_protocols.pdf">febbraio_data_protocols.pdf</a></td>
<td align="left" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/FebbraioDocumentation?filename=febbraio_data_protocols.pdf;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3" valign="top">516.3 K</td>
<td align="left" class="twikiTableCol4" valign="top"><span class="twikiNoBreak">2015-03-17 - 12:26</span></td>
<td align="left" class="twikiTableCol5" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MatthewMizielinski">MatthewMizielinski</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol" valign="top">First draft of febbraio data protocols report/write up</td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td align="center" class="twikiTableCol0 twikiFirstCol twikiLast" valign="top"><img align="top" alt="pdf" border="0" height="16" src="/twiki/pub/TWiki/TWikiDocGraphics/pdf.gif" width="16"><span class="twikiHidden">pdf</span></td>
<td align="left" class="twikiTableCol1 twikiLast" valign="top"><a href="{{ site.baseurl }}/twiki/pub/Project/HiResCL/FebbraioDocumentation/febbraio_reference.pdf">febbraio_reference.pdf</a></td>
<td align="left" class="twikiTableCol2 twikiLast" valign="top"><a href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/FebbraioDocumentation?filename=febbraio_reference.pdf;revInfo=1" rel="nofollow" title="change, update, previous revisions, move, delete...">manage</a></td>
<td align="right" class="twikiTableCol3 twikiLast" valign="top">121.7 K</td>
<td align="left" class="twikiTableCol4 twikiLast" valign="top"><span class="twikiNoBreak">2015-03-17 - 12:27</span></td>
<td align="left" class="twikiTableCol5 twikiLast" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MatthewMizielinski">MatthewMizielinski</a></td>
<td align="left" class="twikiTableCol6 twikiLastCol twikiLast" valign="top">Reference document for the febbraio data set</td>
</tr>
</tbody>
</table>
</div>
</div>
<!--/twistyPlugin--></div>
<!--//twikiAttachments--><!-- /patternContent-->
<p><a name="topic-actions"></a></p>
<div class="patternTopicActions" style="">
<div class="patternTopicAction"><span class="patternActionButtons"><span><a accesskey="e" href="https://collab.metoffice.gov.uk/twiki/bin/edit/Project/HiResCL/FebbraioDocumentation?t=1601309168" rel="nofollow" title="Edit this topic text"><span class="twikiAccessKey">E</span>dit</a></span><span class="twikiSeparator"> | </span><span><a accesskey="a" href="{{ site.baseurl }}/twiki/bin/attach/Project/HiResCL/FebbraioDocumentation" rel="nofollow" title="Attach an image or document to this topic"><span class="twikiAccessKey">A</span>ttach</a></span><span class="twikiSeparator"> | </span><span><a accesskey="p" href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioDocumentation?cover=print" rel="nofollow" title="Printable version of this topic"><span class="twikiAccessKey">P</span>rint version</a></span><span class="twikiSeparator"> | </span><span><span><a accesskey="h" href="{{ site.baseurl }}/twiki/bin/rdiff/Project/HiResCL/FebbraioDocumentation?type=history" rel="nofollow" title="View total topic history"><span class="twikiAccessKey">H</span>istory</a></span>: r2 <a href="{{ site.baseurl }}/twiki/bin/rdiff/Project/HiResCL/FebbraioDocumentation?rev1=2;rev2=1" rel="nofollow">&lt;</a> <a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioDocumentation?rev=1" rel="nofollow">r1</a></span><span class="twikiSeparator"> | </span><span><a accesskey="b" href="{{ site.baseurl }}/twiki/bin/oops/Project/HiResCL/FebbraioDocumentation?template=backlinksweb" rel="nofollow" title="Search the Project/HiResCL Web for topics that link to here"><span class="twikiAccessKey">B</span>acklinks</a></span><span class="twikiSeparator"> | </span><span><a accesskey="r" href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioDocumentation?raw=on" rel="nofollow" title="View raw text without formatting"><span class="twikiAccessKey">R</span>aw View</a></span><span class="twikiSeparator"> | </span><span><a accesskey="w" href="https://collab.metoffice.gov.uk/twiki/bin/edit/Project/HiResCL/FebbraioDocumentation?t=1601309168;nowysiwyg=1" rel="nofollow" title="Raw Edit this topic text">Ra<span class="twikiAccessKey">w</span> edit</a></span><span class="twikiSeparator"> | </span><span><a accesskey="m" href="{{ site.baseurl }}/twiki/bin/oops/Project/HiResCL/FebbraioDocumentation?template=oopsmore&amp;param1=2&amp;param2=2" rel="nofollow" title="Delete or rename this topic; set parent topic; view and compare revisions"><span class="twikiAccessKey">M</span>ore topic actions</a></span></span></div>
<!--/patternTopicAction--></div>
<!--/patternTopicActions-->
<div class="patternInfo twikiGrayText">
<div class="patternRevInfo">Topic revision: r2 - 2015-07-03 - 08:33:35 - <a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Main/MatthewMizielinski">MatthewMizielinski</a></div>
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
<div class="patternWebIndicator">
<table border="1" cellpadding="0" cellspacing="0" class="twikiTable" id="table1" rules="rows">
<tbody>
<tr class="twikiTableOdd twikiTableRowdataBgSorted0 twikiTableRowdataBg0"><th align="center" class="twikiTableCol0 twikiFirstCol" valign="top"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioRunLogs?sortcol=0;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#ffffff" style="">Runid</span></a></th><th align="center" class="twikiTableCol1" valign="top"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioRunLogs?sortcol=1;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#ffffff" style="">Owner</span></a></th><th align="center" class="twikiTableCol2" valign="top"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioRunLogs?sortcol=2;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#ffffff" style="">Status</span></a></th><th align="center" class="twikiTableCol3 twikiLastCol" valign="top"><a href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioRunLogs?sortcol=3;table=1;up=0#sorted_table" rel="nofollow" title="Sort by this column"><span color="#ffffff" style="">Log</span></a></th></tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol" valign="top">xkjej</td>
<td class="twikiTableCol1" valign="top">Karthee</td>
<td align="right" class="twikiTableCol2" valign="top">2007 -&gt; 2107 Complete</td>
<td class="twikiTableCol3 twikiLastCol" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioRunXKJEJ">FebbraioRunXKJEJ</a></td>
</tr>
<tr class="twikiTableOdd twikiTableRowdataBgSorted1 twikiTableRowdataBg1">
<td class="twikiTableCol0 twikiFirstCol" valign="top">xklrb</td>
<td class="twikiTableCol1" valign="top">Pier Luigi</td>
<td align="right" class="twikiTableCol2" valign="top">2007 -&gt; 2107 Complete</td>
<td class="twikiTableCol3 twikiLastCol" valign="top"><a class="twikiLink" href="{{ site.baseurl }}/twiki/bin/view/Project/HiResCL/FebbraioRunXKLRB">FebbraioRunXKLRB</a></td>
</tr>
<tr class="twikiTableEven twikiTableRowdataBgSorted0 twikiTableRowdataBg0">
<td class="twikiTableCol0 twikiFirstCol twikiLast" valign="top">(answg)</td>
<td class="twikiTableCol1 twikiLast" valign="top">Malcolm</td>
<td class="twikiTableCol2 twikiLast" valign="top">1978 -&gt; 2081 Complete</td>
<td class="twikiTableCol3 twikiLastCol twikiLast" valign="top">??</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
